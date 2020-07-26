import json
import boto3
import stripe
import os

stripe.api_key='sk_live_DE6t4W2I8gVFO9FTgYpjJGip'
s3=boto3.client('s3')
bucket='lawpath-data-lake'
prefix='stripe/customers/'
lambdaTemp='/tmp/'

#get customer list from Stripe API
def getCustomerListData(limit, start):
    customerList=[]

    if start=='none':
        input=stripe.Customer.list(limit=limit)
    else:
        input=stripe.Customer.list(starting_after=start, limit=limit)
              
    while(input.get('has_more')):
        customerList.append(input.get('data'))
        lastcustomer=input.get('data')[-1]['id']
        print(lastcustomer)
        input=stripe.Customer.list(starting_after=lastcustomer, limit=limit)

    yield customerList

#extract customers from customer list
def getCustomers(customerList):
    for line in customerList:
        for i in line:
            print(i)
            yield i

#create JSON file for each customer extracted
def createCustomerId(i):
    id=i.get('id')
    yield id

#list all contents in a bucket subfolder
def getContent(bucket, prefix):
    paginator = s3.get_paginator('list_objects_v2')
    kwargs = {'Bucket': bucket, 'Prefix': prefix}

    for page in paginator.paginate(**kwargs):
        #print(page)
        content=page.get('Contents')
        yield content

#extract key value pairs for each file list of s3 files
def getKeyValue(content):
    for line in content:
        key=line.get('Key')
        date = line.get('LastModified')
        keyValue={key:date}
    yield keyValue

def getLastFileKey(bucket, prefix=None):
    obj_dict={}
    for content in getContent(bucket, prefix):
        for keyValue in getKeyValue(content):
            obj_dict.update(keyValue)
            
    sorted_obj=sorted(obj_dict.items(), key=lambda p:p[1], reverse=True)
    lastfileKey=sorted_obj[0][0]
    return lastfileKey

def getStripeCustomers(event, context):
    #initiate local vars
    limit=75
    lastCustomer=''
    
    #retreive last file key from s3
    lastFileKey=getLastFileKey(bucket,prefix)
    
    #if s3 is empty, then last file key is 'none'
    if lastFileKey== prefix:
        lastCustomer='none'
    else:
        lastCustomer=lastFileKey[17:-5]        

    filecounter=0

    for data in getCustomerListData(limit, lastCustomer):
        for i in getCustomers(data):            
            for id in createCustomerId(i):
                filename= lambdaTemp+ str(id)+'.json'
                print(filename)
                with open(filename, 'w') as fp:
                    json.dump(i, fp)
                fileKey=prefix+filename
                s3.upload_file(Filename=filename, Bucket=bucket, Key=fileKey)
                filecounter=filecounter+1
                print(filecounter)
                os.remove(filename)
                

    
    return filecounter