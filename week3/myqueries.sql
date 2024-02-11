-- Created bq table from Cloud Storage bucket (10 files loaded with *)
CREATE OR REPLACE EXTERNAL TABLE `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.external_green_trip`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-gcs-bucket-dawei7/green_tripdata/*']
);

-- Creaete a bq table from External Table
CREATE OR REPLACE TABLE `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.green_tripdata` AS
SELECT * FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.external_green_trip`;


-- Question 1: What is count of records for the 2022 Green Taxi Data??

SELECT COUNT(*) AS count_2022
FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.external_green_trip`
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2022;
-- Answer: 840'392

-- Question 2:
-- Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
-- What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

-- External Table
SELECT COUNT(*) AS count_2022
FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.external_green_trip`
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2022;

-- Table
SELECT COUNT(*) AS count_2022
FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.green_tripdata`
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2022;

--Aswer: 0 MB for the External Table and 6.41MB for the Materialized Table

-- Question 3:
-- How many records have a fare_amount of 0?
SELECT COUNT(*) AS count_fare_0
FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.green_tripdata`
WHERE fare_amount = 0;
-- Answer: 1'622

-- Question 4: What is the best strategy to make an optimized table in Big Query if your query will always order the results by PUlocationID and filter based on lpep_pickup_datetime? (Create a new table with this strategy)
-- Answer: Partition by lpep_pickup_datetime Cluster on PUlocationID

-- Create a partitioned and clustered table
CREATE OR REPLACE TABLE `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.green_tripdata_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.external_green_trip`;

-- Question 5:
-- Write a query to retrieve the distinct PULocationID between lpep_pickup_datetime 06/01/2022 and 06/30/2022 (inclusive)
-- Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values?

-- Materialized Table
SELECT COUNT(DISTINCT PULocationID) AS count_PULocationID
FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.green_tripdata`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';

-- Partitioned Table
SELECT COUNT(DISTINCT PULocationID) AS count_PULocationID
FROM `de-zoomcamp-412423.mage_zoomcamp_dataset_dawei7.green_tripdata_partitioned_clustered`
WHERE lpep_pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30';
-- Answer: 12.82 MB for non-partitioned table and 1.12 MB for the partitioned table

-- Question 6:
-- Where is the data stored in the External Table you created?
-- Answer: GCP Bucket

-- Question 7:
-- It is best practice in Big Query to always cluster your data:
-- Answer: True