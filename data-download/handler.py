import json
import boto3
import os
from datetime import datetime, date, timedelta

s3=boto3.client('s3')
bucket='lawpath-data-lake-raw-data'
prefix='segment-logs-events/'

def getContent(bucket, prefix):
    paginator = s3.get_paginator('list_objects_v2')
    kwargs = {'Bucket': bucket, 'Prefix': prefix}

    for page in paginator.paginate(**kwargs):
        #print(page)
        content=page.get('Contents')
        yield content

def getKeys(content):
    key=[]
    for line in content:
        entry=line.get('Key')
        key.append(entry)
    return key

#def getData(keylist):
    

def dataDownload(event, context):
    endDate=date.today()
    startDate=endDate-timedelta(days=30)

    for content in getContent(bucket, prefix):
        for key in getKeys(content):
            if key != prefix:
                a=(key[38:-4])
                filename='./download'+key[19:]
                filedate=datetime.strptime(a, '%Y-%m-%d').date()
                if filedate >=startDate and filedate <=endDate:
                    s3.download_file(Bucket='bucket', Key=key, Filename=filename)

    return None