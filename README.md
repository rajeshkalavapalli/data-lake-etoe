Data Lake End-to-End Project (data-lake-etoe)

This project is a practice project to understand how data is generated and stored in a data lake.
I wrote a Python script that creates fake data for three parts:

Users

Transactions

Events

Each dataset is saved into files (CSV or JSON), which can later be used for data engineering practice like ETL pipelines, analytics, or machine learning.

📂 Project Structure
data-lake-etoe/
│
├── data/                 # This folder will contain the generated files
│   ├── user.csv
│   ├── transection.csv
│   └── events.json
│
├── generate_data.py      # The Python script I wrote
└── README.md

🛠️ What the Script Does
1. Users Data (user.csv)

Creates 100 users.

Each user has:

user_id → a number from 1 to 100

name → like "user_1", "user_2", …

country → randomly chosen from UK, US, GM, DE, FR

👉 File created: user.csv

2. Transactions Data (transection.csv)

Creates 500 transactions.

Each transaction has:

tsx_id → a unique ID (UUID)

user_id → linked to one of the users

amount → random value between 10 and 500

tsx_date → random date within 1 year from 22-Sep-2025

👉 File created: transection.csv

3. Events Data (events.json)

Creates 300 events.

Each event has:

event_id → a unique ID (UUID)

user_id → linked to one of the users

event_type → randomly one of: click, view, purchase, addtocart

event_time → random timestamp within 1 year from 22-Sep-2025

👉 File created: events.json (JSON Lines format, easy for big data tools)

▶️ How to Run

Clone this project or copy the script.

Install Python (3.8 or above).

Install required library:

pip install pandas


Run the script:

python generate_data.py


After running, you will see the files inside the data/ folder:

user.csv

transection.csv

events.json

🌩️ Step 2: Create an S3 Bucket

After generating local data (CSV & JSON files), the next step is to create an AWS S3 bucket to store them.
I used boto3 (AWS SDK for Python) to create the bucket.

Code: Create S3 Bucket
import boto3 

# Connect to S3
s3 = boto3.client('s3')

# Bucket name
Bucket_name = "rajesh-datalake-5432"

# Create bucket
s3.create_bucket(
    Bucket=Bucket_name,
    # If region is NOT us-east-1, uncomment below:
    # CreateBucketConfiguration={
    #     'LocationConstraint': 'ap-south-1'
    # }
)

print(f"Bucket {Bucket_name} created successfully")

Notes:

If you are using us-east-1 region, you don’t need CreateBucketConfiguration.

For other regions (like Mumbai ap-south-1), you must include it.

Bucket names must be globally unique in AWS. If the name already exists, you’ll get an error.

## 📂 Step 3: Create Folders and Upload Data to S3

After creating the S3 bucket, the next step is to set up a **folder structure** and upload the generated data files.

---

### Create Folder Structure in S3

```python
# create folders 
folders = ["raw/user/", "raw/transection/", "raw/event/"]

for folder in folders:
    s3.put_object(Bucket=Bucket_name, Key=folder)

print("folders created successfully")
```

This will create three "folders" (actually prefixes in S3):

* `raw/user/`
* `raw/transection/`
* `raw/event/`

---

### Upload Files into S3

```python
# upload files
s3.upload_file(r"D:\data-lake-etoe\data\user.csv", 
               "rajesh-datalake-5432", 
               "raw/user/user.csv")

s3.upload_file(r"D:\data-lake-etoe\data\transection.csv", 
               "rajesh-datalake-5432", 
               "raw/transection/transection.csv")

s3.upload_file(r"D:\data-lake-etoe\data\events.json", 
               "rajesh-datalake-5432", 
               "raw/event/events.json")
```

---

### ✅ What Happens Here

* Creates a **`raw/` layer** inside the bucket.
* Uploads:

  * `user.csv` → stored in **raw/user/**
  * `transection.csv` → stored in **raw/transection/**
  * `events.json` → stored in **raw/event/**

---

### 📌 Why This Matters

* Organizing data into layers (`raw/`, `processed/`, `analytics/`) is a **best practice** in data lake projects.
* The **raw layer** keeps the original data exactly as generated.
* Later steps can build **ETL pipelines** to process and move this data into other layers.

---
