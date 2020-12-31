import io
import boto3
from boto3.session import Session
import pandas as pd
import os

ACCESS_KEY = ''
SECRET_KEY = ''
BUCKET_NAME = "farasbuckettest"

s3_resource = boto3.resource(service_name='s3',
    region_name='eu-west-3',aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)


s3_client = boto3.client(
    's3',
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY,
    region_name = 'eu-west-3'
)

def download_rep_from_s3(s3_resource,bucketName, path_in_s3):
    """
    Fonction permettant de télécharger un dossier depuis AWS S3 
    en local avec le meme arborescence
    """
    bucket = s3_resource.Bucket(bucketName) 
    for obj in bucket.objects.filter(Prefix = path_in_s3):
        if not os.path.exists(os.path.dirname(obj.key)):
            os.makedirs(os.path.dirname(obj.key))
        bucket.download_file(obj.key, obj.key) # save to same path


def upload_files_from_local_to_s3(s3_resource, bucketName, local_path,s3_path):
    """
    Fonction permettant de charger les fichiers local vers AWS S3
    avec le meme arborescence
    """
    bucket = s3_resource.Bucket(bucketName)
 
    for subdir, dirs, files in os.walk(local_path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                #print(data)
                #print(data)
                bucket.put_object(Key= os.path.join(s3_path,full_path[len(local_path)+1:]), Body=data)
                #print("file %s ok" %(file))
                
#Test connexion                 
clientResponse = s3_client.list_buckets()
    
# Print the bucket names one by one
print('Printing bucket names...')
for bucket in clientResponse['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')


