# Module 1 Homework: Docker & SQL

de-zoomcamp
Docker workshop using codespaces

## Question 1

Run the image with the specified python version:

```bash
docker run -it --rm --entrypoint=bash python:3.13-slim
```
The inside the interactive terminal of the running python container:

```bash
pip -V
```

## Question 3

```
SELECT COUNT(index) FROM public.green_taxi_data
WHERE lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01'
AND trip_distance <= 1
```

## Question 4

```
SELECT DATE(lpep_pickup_datetime) FROM public.green_taxi_data
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1
```

## Question 5

```
SELECT SUM(d.total_amount) AS total_amount_sum, z."Zone"
FROM public.green_taxi_data d 
INNER JOIN public.taxi_zones z ON z."LocationID" = d."PULocationID"
WHERE DATE(d.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_amount_sum DESC
LIMIT 1
```

## Question 6

```
SELECT zdo."Zone"
FROM public.green_taxi_data d 
INNER JOIN public.taxi_zones zpu ON zpu."LocationID" = d."PULocationID"
INNER JOIN public.taxi_zones zdo ON zdo."LocationID" = d."DOLocationID"
WHERE d.lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01' 
AND zpu."Zone" = 'East Harlem North'
ORDER BY d.tip_amount DESC
LIMIT 1
```