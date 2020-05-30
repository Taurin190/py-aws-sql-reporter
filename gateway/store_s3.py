import boto3


class StoreS3:

    def __init__(self, config):
        self.config = config

    def upload_file(self, key, file_path):
        s3 = boto3.resource('s3')
        data = open(file_path, 'rb')
        s3.Bucket(self.config['bucket']).put_object(Key=key, Body=data)

    def download_file(self, key):
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.config['bucket'])
        bucket.download_file(key, './tmp/' + key)
