import os
import sqlalchemy
import pandas as pd

# Get the files
os.system("wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz")
os.system("wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv")

# Unzip the file
# Move the file to the data folder
# Remove the file
os.mkdir("data")

# taxi data
os.system("gunzip green_tripdata_2019-09.csv.gz")
os.system("mv green_tripdata_2019-09.csv data/")
# zone lookup table
os.system("mv taxi+_zone_lookup.csv data/")


# Load data to df
df_green_tripdata_2019_09 = pd.read_csv("data/green_tripdata_2019-09.csv")
df_green_tripdata_2019_09.tpep_pickup_datetime = pd.to_datetime(df_green_tripdata_2019_09.lpep_pickup_datetime)
df_green_tripdata_2019_09.tpep_dropoff_datetime = pd.to_datetime(df_green_tripdata_2019_09.lpep_dropoff_datetime)

# Load the taxi zone lookup table
df_taxi_zone_lookup = pd.read_csv("data/taxi+_zone_lookup.csv")

# Create the connection
engine = sqlalchemy.create_engine("postgresql://root:root@pgdatabase:5432/ny_taxi")
connection = engine.connect()

# Upload the data
df_green_tripdata_2019_09.to_sql("green_tripdata_2019_09", engine, if_exists="replace")
df_taxi_zone_lookup.to_sql("taxi_zone_lookup", engine, if_exists="replace")