import os

def download_data(base_url_green: str, base_url_yellow: str):
    import requests
    
    directory = "/mnt/ny_taxi"
    os.makedirs(directory, exist_ok=True)

    # for base_url in [base_url_green, base_url_yellow]:
    #     if base_url == base_url_yellow:
    #         for year in range(2019, 2021):
    #             for month in range(1, 13):
    #                 url = f"{base_url}yellow_tripdata_{year}-{month:02}.csv.gz"
    #                 response = requests.get(url)
    #                 response.raise_for_status()
    #                 with open(f"/mnt/ny_taxi/yellow_tripdata_{year}-{month:02}.csv.gz", "wb") as f:
    #                     f.write(response.content)

    #     else:
    #         for year in range(2019, 2021):
    #             for month in range(1, 13):
    #                 url = f"{base_url}green_tripdata_{year}-{month:02}.csv.gz"
    #                 response = requests.get(url)
    #                 response.raise_for_status()
    #                 with open(f"/mnt/ny_taxi/green_tripdata_{year}-{month:02}.csv.gz", "wb") as f:
    #                     f.write(response.content)
                        
                 
    # Download the FHV data
    base_url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/"
    for month in range(1, 13):
        url = f"{base_url}fhv_tripdata_2019-{month:02}.csv.gz"
        response = requests.get(url)
        response.raise_for_status()
        with open(f"/mnt/ny_taxi/fhv_tripdata_2019-{month:02}.csv.gz", "wb") as f:
            f.write(response.content)
    
