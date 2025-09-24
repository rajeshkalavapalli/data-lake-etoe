from pyspark.sql import SparkSession

from pyspark.sql.functions import when 


spark = SparkSession.builder.appName('datalakeetl') .config("spark.jars.packages", 
            "org.apache.hadoop:hadoop-aws:3.3.4,com.amazonaws:aws-java-sdk-bundle:1.12.262") .getOrCreate()

user_df = spark.read.csv("s3a://rajesh-datalake-5432/raw/user/user.csv", header=True, inferSchema=True)

transection_df = spark.read.csv("s3a://rajesh-datalake-5432/raw/transection/", header=True, inferSchema=True)

merged_df=transection_df.join(user_df,on="user_id",how="inner")

merged_df = merged_df.withColumn("txn_category",when(merged_df. amount>250,"high").otherwise("low")
)

revenue_country=merged_df.groupby("country").sum('amount')
revenue_country.write.mode("overwrite").parquet("file:///D:/data-lake-etoe/data/revenue_country_spark.parquet")

#new 