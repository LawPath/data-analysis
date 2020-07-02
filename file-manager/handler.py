import json
import boto3
import gzip
from io import BytesIO
import inspect

s3=boto3.resource('s3')
bucket_name="lawpath-data-lake"
key = "segment-logs/6Q2N6sz6Aq/1544572800000/1553116119647.b27b420ba21e.f4c8ef3.420dbd6d-9228-474b-9e11-1744e7626cb8.gz"

def hello(event, context):
    print("hello world!")
    json_list=[]
    json_return = []
    
    #Access Object from S3
    obj = s3.Object(bucket_name, key)

    #Read Gzipfile
    body = obj.get()['Body'].read()
    gzipfile = BytesIO(body)
    gzipfile = gzip.GzipFile(fileobj=gzipfile)

    #Create List of JSON Objects
    with gzipfile as fin:
        for line in fin:
            json_line=json.loads(line)
            json_list.append(json_line)

    #iterate over the list of json object
    for i in json_list:
        if i["type"]=="track":
            print("Tracked Event: " + i["event"])
            json_return.append(i["event"])
            

    
    #print(json_list[0]["type"])
    #print(type(json_list[0]))

    
    #content = gzipfile.read()
    #json_data=[]
    #for line in content:
    #    json_line = json.loads(line)
    #    json_data.append(json_line)
    #print(json_data[0])
    #print(type(json_data[0]))
    return json_return
