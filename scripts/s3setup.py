import boto3 

# connect to s3
s3 = boto3.client('s3')

#bucket name 
Bucket_name = "rajesh-datalake-5432"

#create bucket 
s3.create_bucket(
    Bucket = Bucket_name,
    # CreateBucketConfiguration= {
    #     'LocationConstraint': 'us-east-1'
    # }
)

print(f"bucket{Bucket_name}created sucessfully")