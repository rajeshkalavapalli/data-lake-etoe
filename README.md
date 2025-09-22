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