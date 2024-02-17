def upload_to_pg():
    from sqlalchemy import create_engine
    import pandas as pd
    import os
    
    # Create the connection
    engine = create_engine("postgresql://root:root@pgdatabase:5432/ny_taxi")
    connection = engine.connect()
    
    # Set the chunksize
    chunksize = 10000
    
    for file in os.listdir("/mnt/ny_taxi"):
        if "green" in file:
            for chunk in pd.read_csv(f"/mnt/ny_taxi/{file}", compression="gzip", chunksize=chunksize):
                chunks = pd.read_csv(f"/mnt/ny_taxi/{file}", compression="gzip")
                # transform datetime columns
                chunks["lpep_pickup_datetime"] = pd.to_datetime(chunks["lpep_pickup_datetime"])
                chunks["lpep_dropoff_datetime"] = pd.to_datetime(chunks["lpep_dropoff_datetime"])
                chunks.to_sql("green_tripdata", connection, if_exists="append", index=False)
        elif "yellow" in file:
            for chunk in pd.read_csv(f"/mnt/ny_taxi/{file}", compression="gzip", chunksize=chunksize):
                chunks = pd.read_csv(f"/mnt/ny_taxi/{file}", compression="gzip")
                # transform datetime columns
                chunks["tpep_pickup_datetime"] = pd.to_datetime(chunks["tpep_pickup_datetime"])
                chunks["tpep_dropoff_datetime"] = pd.to_datetime(chunks["tpep_dropoff_datetime"])
                chunks.to_sql("yellow_tripdata", connection, if_exists="append", index=False)
        elif "fhv" in file:
            for chunk in pd.read_csv(f"/mnt/ny_taxi/{file}", compression="gzip", chunksize=chunksize):
                # Transform datetime columns
                chunk["pickup_datetime"] = pd.to_datetime(chunk["pickup_datetime"])
                chunk["dropOff_datetime"] = pd.to_datetime(chunk["dropOff_datetime"])
                chunk.to_sql("fhv_tripdata", connection, if_exists="append", index=False)