#!/usr/bin/env bash

## bash script to generate base64 encoded .env variable values
while IFS='=' read -r key value; do
    echo "SECRET_$key=$(echo -n "$value" | base64)";
done < .env > .env_encoded

## bash script to generate base64 encoded json to .env variable value
# SECRET_GCP_SA=$(cat .keys/kestra-sa.json | base64 -w 0)" >> .env_encoded