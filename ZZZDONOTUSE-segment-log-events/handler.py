import json
import gzip
import csv
import os
import boto3
import dateutil.parser
from datetime import datetime, date, time, timedelta

s3=boto3.client('s3')
inputBucket='lawpath-data-lake'
inputPrefix='segment-logs/6Q2N6sz6Aq/'
outputBucket='lawpath-data-lake-raw-data'
outputPrefix='segment-logs-events'
header=['Received', 'Event', 'User ID', 'User Email']

def getContent(bucket, prefix):
    paginator = s3.get_paginator('list_objects_v2')
    kwargs = {'Bucket': bucket, 'Prefix': prefix}

    for page in paginator.paginate(**kwargs):
        #print(page)
        content=page.get('Contents')
        yield content

def getKeyValue(content):
    for line in content:
        key=line.get('Key')
        date = line.get('LastModified')
        keyValue=(key,date)
    yield keyValue

def createDatedFile(name, lastModified, prefix=None):
    fileName=str(name)+str(lastModified.date())
    fileKey=str(prefix)+str(fileName)
    keyValue={fileName:fileKey}
    yield keyValue

def getLastFileKey(bucket, prefix):
    obj_dict={}
    for content in getContent(bucket, prefix):
        for keyValue in getKeyValue(content):
            obj_dict.update(keyValue)
            
    #sort obj_dict{}        
    sorted_obj=sorted(obj_dict.items(), key=lambda p:p[1], reverse=True)
    lastfileKey=sorted_obj[0][0]
    return lastfileKey

def getData(bucket,prefix, start=date.today(), end=date.today()-timedelta(days=30)):
    for content in getContent(bucket, prefix):
        for key in getKeys(content):
            yield key

def getKeys(content):
    keylist=[]
    for line in content:
        key=line.get('Key')
        keylist.append(key)
    return keylist

def getEntry(key):
    obj=s3.get_object(Bucket=inputBucket, Key=key)
    body=obj['Body']
    with gzip.open(body,'rt') as gf:
        for line in gf:
            json_line=json.loads(line)
            if json_line['type'] == 'track':
                date= json_line.get('receivedAt')
                date=dateutil.parser.parse(date)
                date_epoch=float(date.timestamp())
                file_date=date.date()
                entry = {
                    'FileDate': str(file_date),
                    'Date': date_epoch,
                    'Event': json_line.get('event'),
                    'UserID': json_line.get('userId'),
                    'UserEmail': json_line.get('properties',{}).get('UserEmail')
                }
                yield entry

def processOldData(event, context):
    
    for content in getContent(inputBucket, inputPrefix):
        for key in getKeys(content):
            for entry in getEntry(key):
                fileDate=entry['FileDate']
#
                filename='segment-log-entry-'+fileDate+'.json'
                print('./tmp/'+filename)

                if os.path.isfile('./tmp/'+filename)==False:
                    try:
                        a=os.listdir('./tmp/')
                        uploadfile='./tmp/'+a[0]
                        filekey=outputPrefix+'/'+a[0]
                        print(filekey)
                        s3.upload_file(Filename=uploadfile, Bucket=outputBucket, Key=filekey)
                        os.remove(uploadfile)
                        
                    except Exception:
                        pass

                    with open('./tmp/'+filename, 'w') as file:
                        json.dump(entry, file)

                with open('./tmp/'+filename,'a') as file:
                    json.dump(entry, file)
    
    a=os.listdir('./tmp/')
    uploadfile='./tmp/'+a[0]
    filekey=outputPrefix+'/'+a[0]
    print(filekey)
    s3.upload_file(Filename=uploadfile, Bucket=outputBucket, Key=filekey)
    os.remove(uploadfile)

    return None
