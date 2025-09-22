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

# create folders 

folders = ["raw/user/", "raw/transection/", "raw/event/"]

for folder in folders:
    s3.put_object(Bucket=Bucket_name, Key=folder)

print(f"folders create sucessfully")

# upload file

s3.upload_file(r"D:\data-lake-etoe\data\user.csv","rajesh-datalake-5432", "raw/user/user.csv")

s3.upload_file(r"D:\data-lake-etoe\data\transection.csv","rajesh-datalake-5432", "raw/transection/transection.csv")

s3.upload_file(r"D:\data-lake-etoe\data\events.json","rajesh-datalake-5432", "raw/events/events.json")