# Module 2 Homework: Workflow orchestration

de-zoomcamp
Docker workshop using codespaces

## Question 1

First do a backfill in Kestra with dates of 2020-12-01 00:00:00 - 2021-01-01 00:00:00 for the flow 09_gcp_taxi_scheduled.
Then check the `yellow_tripdata_2020-12.csv` file in the GCS bucket. The file size is 134.5MB.

## Question 2

Executing the 08_gcp_taxi flow in kestra, the file label on the Execution tab shows `green_tripdata_2020-04.csv`.

## Question 3

First do a backfill in Kestra with dates of 2020-01-01 00:00:00 - 2021-01-01 00:00:00 for the flow 09_gcp_taxi_scheduled on yellow taxi data.
Then check the row count in BigQuery for the table of `yellow_tripdata`. The yellow taxi data row count for the year 2020 is 24,648,499.

## Question 4

First do a backfill in Kestra with dates of 2020-01-01 00:00:00 - 2021-01-01 00:00:00 for the flow 09_gcp_taxi_scheduled on green taxi data.
Then check the row count in BigQuery for the table of `green_tripdata`. The green taxi data row count for the year 2020 is 1,734,051.

## Question 5

First do a backfill in Kestra with dates of 2021-03-01 00:00:00 - 2021-04-01 00:00:00 for the flow 09_gcp_taxi_scheduled on yellow taxi data.
Then check the row count in BigQuery for the table of `yellow_tripdata_2021_03`. The yellow taxi data row count for the March of 2021 is 1,925,152.

## Question 6

Looking up the `Schedule` trigger `timezone` property documentation, the correct answer is:
Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration