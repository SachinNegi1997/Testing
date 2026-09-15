from fastapi import FastAPI
from sysutil import all_detail
import boto3
from botocore.exceptions  import ClientError
#s3= boto3.resource("s3") # s3 is using boto3 resources
s3= boto3.client("s3") # when to do upload file and download us client 
# fastapi is file and FastAPI is class
# pip install fastapi
# pip install "fastapi [satandard]"
#  import all_detail function from sysutil file
app=FastAPI(title="utilities")

@app.get("/home")

def home():

 return {"Hello" : "testing for api " }



@app.get("/info")
# creatin app when type "/info"  fuction call
def info(): 

   return all_detail()

@app.get("/aws/s3")

def bucketlist():
  buckets = []
  for bucket in s3.buckets.all():
     buckets.append(bucket.name)

  return buckets



# To execute fastapi use  fastapi dev

file_name = "/home/sachin/myvenv/image.png" # upload file in s3 bucket  using boto3 
bucket ="s3balthi"
object_name = "image.png"

response = s3.upload_file(file_name,bucket,object_name)

