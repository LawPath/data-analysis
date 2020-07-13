import json
import boto3
import gzip
from io import BytesIO
import pandas as pd 


s3=boto3.client('s3')
prefix='segment-logs/6Q2N6sz6Aq/'
bucket='lawpath-data-lake'

##generates keys to iterate through
def generateKeys(prefix,bucket):
    keyList=[]
    for obj in s3.list_objects_v2(Bucket=bucket, Prefix=prefix)['Contents']:
        keyList.append(obj['Key'])
    return keyList

#generates objects to iterate through
def retrieveObjects(keyList):
    objectList=[]

    for key in keyList:
        obj=s3.get_object(Bucket=bucket, Key=key)
        body=obj['Body']
        with gzip.open(body,'rt') as gf:
            for line in gf:
                json_line=json.loads(line)
                if json_line['type'] == 'track':
                    date = json_line.get('receivedAt')[0:10]
                    objectList.append([
                        date,
                        json_line.get('receivedAt'),
                        json_line.get('event'),
                        json_line.get('userId'),
                        json_line.get('properties',{}).get('UserEmail')                       
                    ])

    return objectList

#lambda function
def dataCollector(event,context):
    datakeyList=generateKeys(prefix,bucket)
    extractedList=retrieveObjects(datakeyList)
    dataFrame = pd.DataFrame(extractedList,columns=['Date','Received At', 'Event', 'User ID', 'User Email'])
    dataFrame.to_csv(r'./data/data.csv', header=True)
       
    return []
