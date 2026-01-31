#!/usr/bin/env bash

## bash script to run postgres and pgadmin containers
echo "Running postgres and pgadmin containers..."

docker-compose up -d

## bash script to build the image
echo "Building image taxi_ingest:v001..."

docker build -t taxi_ingest:v001 .

## bash script to run the ingestion container
echo "Running data ingestion..."

docker run -it --rm \
  --network=pipeline_default \
  taxi_ingest:v001