import pandas as pd 


import random 
import uuid
from datetime import datetime, timedelta

# generate users 

users = []

for i in range(1,101):
    users.append(
        {
            'user_id':i,
            'name':f'user_{i}',
            'country': random.choice(['UK','US','GM','DE','FR'])
        }
    )


df_users = pd.DataFrame(users)
df_users.to_csv(r"D:\data-lake-etoe\data\user.csv", index=False)

# genearete transection 
transection = []
start_date = datetime(2025,9, 22)

for i in range(1,500):
    transection.append({
        'tsx_id':str(uuid.uuid4()),
        'user_id':random.randint(1,100),
        'amount':round(random.uniform(10,500),2),
        'tsx_date':(start_date+timedelta(days=random.randint(0,365))).strftime("%Y-%m-%d")
    })

df_txn =pd.DataFrame(transection)
df_txn.to_csv(r"D:\data-lake-etoe\data\transection.csv", index=False)

# events generate 

events = []
start_date = datetime(2025, 9, 22)

for i in range(1, 300):
    events.append({
        'event_id': str(uuid.uuid4()),
        'user_id': random.randint(1, 100),
        'event_type': random.choice(['click', 'view', 'purchase', 'addtocart']),
        'event_time': (start_date + timedelta(days=random.randint(0, 365))).isoformat()
    })

df_event = pd.DataFrame(events)
df_event.to_json(r"D:\data-lake-etoe\data\events.json", orient="records", lines=True)
