from Cloud import Cloud

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    access_key = ''
    secret_key = ''
    bucket_name = ""
    c = Cloud(access_key, secret_key, bucket_name)
    c.download_rep_from_s3(c.bucket_name, "")