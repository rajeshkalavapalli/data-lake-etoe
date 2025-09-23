import pandas as pd 

event_df = pd.read_json(r"D:\data-lake-etoe\data\events.json", lines=True)

user_df = pd.read_csv(r"D:\data-lake-etoe\data\user.csv")

transection_df = pd.read_csv(r"D:\data-lake-etoe\data\transection.csv")

# merge transection with users 

merged = transection_df.merge(user_df, how="inner",on="user_id" )

# add derived colum 

merged["txn_catogery"] = merged["amount"].apply(lambda x:"high" if x> 250 else "low")

revenue_country= merged.groupby('country')["amount"].sum().reset_index()

revenue_country.to_parquet(r"D:\data-lake-etoe\data\revenue_country.parquet")