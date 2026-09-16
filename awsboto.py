import boto3
from botocore.exceptions  import ClientError

s3=boto3.client("s3")



file_name = "/home/sachin/myvenv/image.png"
object_name = "awsboto.py"
bucket ="s3balthi"


def upload_s3_bucket(file_name,object_name,bucket):
 try:
            s3.upload_file(file_name,bucket,object_name)
            return {"status": "success" ,"bucket": bucket ,"object_name": object_name}

     except ClientError as e:
            return {"status": "error" , "message": str(e)}
