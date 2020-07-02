import json
import boto3
import gzip
from io import BytesIO

s3=boto3.resource('s3')
bucket_name="lawpath-data-lake"
key = "segment-logs/6Q2N6sz6Aq/1544572800000/1553116119647.b27b420ba21e.f4c8ef3.420dbd6d-9228-474b-9e11-1744e7626cb8.gz"

def hello(event, context):
    print("hello world!")
    obj = s3.Object(bucket_name, key)
    body = obj.get()['Body'].read()
    gzipfile = BytesIO(body)
    gzipfile = gzip.GzipFile(fileobj=gzipfile)
    content = gzipfile.read()
    print (content)
    return content
