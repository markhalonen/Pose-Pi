import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
    
data = open('dog.jpg', 'rb')

s3.Bucket('pose-photos').put_object(Key='dog3.jpg', Body=data, ACL='public-read', ContentType='image/png')