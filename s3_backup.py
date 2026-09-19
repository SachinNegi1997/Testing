"""
    This  script take a backup form local and upload AWS S3
    using boto3
    install aws cli 
    command : aws config
    access key:
    secret key: 
"""
import boto3


s3 = boto3.resource("s3")
list_of =[]
bucket_name="python-for-devops"
region= "us-east-2"

def bucket_list(s3):
 for bucket in s3.buckets.all():
   list_of.append(bucket.name)
   print(list_of)



def create_bucket(s3):

  s3.create_bucket(Bucket= bucket_name,CreateBucketConfiguration={ 'LocationConstraint': 'region'},)
  print ("bucket is created sucessfully")

#create_bucket(s3)
#bucket_list(s3)

def backup_upload(s3,file_name,bucket_name,key_name): 
  data= open(file_name,'rb') #before uploading aws open and read file in binary form
  s3.Bucket(bucket_name).put_object(Key=key_name,Body=data) # function take bucketname,key,filename
  print("upload backup aws s3 bucket sucessfully")
file_name="/home/sachin/myvenv/api.py" #path of backup  file
backup_upload(s3,file_name,bucket_name,"new_file") #function call

