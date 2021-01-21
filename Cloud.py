import boto3
import os


class Cloud:

    access_key = ''
    secret_key = ''
    bucket_name = ''
    s3_ressource = boto3.resource('s3')
    S3_client = boto3.client('s3')

    def __init__(self, ak, sk, bn):
        self.access_key = ak
        self.secret_key = sk
        self.bucket_name = bn
        self.s3_resource = boto3.resource(service_name='s3',
                             region_name='eu-west-3', aws_access_key_id = ak,
                             aws_secret_access_key=sk
                             )
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=ak,
            aws_secret_access_key=sk,
            region_name='eu-west-3'
        )

    def download_rep_from_s3(self, bucketName, path_in_s3):
        """
        Fonction permettant de télécharger un dossier depuis AWS S3
        en local avec le meme arborescence
        """
        list_obj = self.s3_client.list_objects_v2(
            Bucket=bucketName,
            Prefix=path_in_s3)
        for file_path in list_obj['Contents']:
            if not os.path.exists(os.path.dirname(file_path['Key'])):
                os.makedirs(os.path.dirname(file_path['Key']))
            self.s3_client.download_file(bucketName, file_path['Key'], file_path['Key'])



    def upload_files_from_local_to_s3(self, bucketName, local_path, s3_path):
        """
        Fonction permettant de charger les fichiers en local vers AWS S3
        avec le meme arborescence
        """
        bucket = self.s3_resource.Bucket(bucketName)

        for subdir, dirs, files in os.walk(local_path):
            for file in files:
                full_path = os.path.join(subdir, file)
                with open(full_path, 'rb') as data:
                    # print(data)
                    # print(data)
                    key = os.path.join(s3_path, full_path[len(local_path) + 1:])
                    objs = list(bucket.objects.filter(Prefix=key))
                    # print(objs[0].key)
                    if ([w.key == s3_path for w in objs]):
                        print("The file %s already exists!" % (objs[0].key))

                    else:
                        print("The file %s doesn't exist so it will create" % (objs[0].key))
                        bucket.put_object(Key=os.path.join(s3_path, full_path[len(local_path) + 1:]), Body=data)
