import json
import gzip
import os
import boto3
from datetime import datetime, date, time, timedelta, tzinfo
import dateutil.parser
import pytz

s3=boto3.client('s3')

def getContent(bucket, prefix):
    paginator = s3.get_paginator('list_objects_v2')
    kwargs = {'Bucket': bucket, 'Prefix': prefix}

    for page in paginator.paginate(**kwargs):
        content=page.get('Contents')
        yield content

def getKeys(content):
    keylist=[]
    for line in content:
        key=line.get('Key')
        keylist.append(key)
    return keylist

def getKeyValue(content):
    #keyValue=[]
    for line in content:
        date=line.get('LastModified')
        key=line.get('Key')
        entry=[date,key]
    #    keyValue.append(entry)
    #return keyValue
        yield entry

def getLastFileKey(bucket,prefix):
    keys=[]
    for content in getContent(bucket, prefix):
        for keylist in getKeys(content):
            if keylist != prefix:
                keys.append(keylist)

    keys.sort(reverse=True)
    #print(len(keys))
    return keys

def getEntry(bucket,key):
    obj=s3.get_object(Bucket=bucket, Key=key)
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

def createFile(bucket, prefix, directory):
    a=os.listdir(directory)
    uploadfile=directory+a[0]
    filekey=prefix+a[0]
    s3.upload_file(Filename=uploadfile, Bucket=bucket, Key=filekey)
    os.remove(uploadfile)

def getData(event, context):
    rawBucket='lawpath-data-lake'
    rawPrefix='segment-logs/6Q2N6sz6Aq/'
    cleanBucket='lawpath-data-lake-raw-data'
    cleanPrefix='segment-logs-events/'
    directory='/tmp/'
    

    a = getLastFileKey(cleanBucket,cleanPrefix)
    lastFileDate=datetime.strptime(a[0][38:-5], '%Y-%m-%d')
    lastFileDate=lastFileDate.replace(tzinfo=pytz.UTC)

    #gets all keys to be processed in this round
    for content in getContent(rawBucket, rawPrefix):
        for kv in getKeyValue(content):
            kvnaive=kv[0].replace(tzinfo=pytz.UTC)
            key = kv[1]
            if kvnaive > lastFileDate:
                for entry in getEntry(rawBucket,key):
                    fileDate=entry['FileDate']
                    filename='segment-log-entry-'+fileDate+'.json'

                if os.path.isfile(directory+filename)==False:
                    try:
                        createFile(cleanBucket, cleanPrefix, directory)
                    except Exception:
                        pass
                    print(filename)
                    with open(directory+filename, 'w') as file:
                        json.dump(entry, file)

                with open(directory+filename,'a') as file:
                    json.dump(entry, file)
    
    createFile(cleanBucket, cleanPrefix, directory)

    return []