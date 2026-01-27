#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

def main():
    engine = create_engine('postgresql://postgres:postgres@postgres:5432/ny_taxi')

    df = pd.read_parquet(
        'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet',
        engine='pyarrow'
    )

    df.to_sql(
        name='green_taxi_data',
        con=engine,
        if_exists='replace'
    )

    df_iter = pd.read_csv(
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv',
        iterator=True,
        chunksize=100000,
    )

    first = True

    for df_chunk in tqdm(df_iter):
        if first:
            df_chunk.head(0).to_sql(
                name='taxi_zones',
                con=engine,
                if_exists='replace'
            )
            first = False

        df_chunk.to_sql(
            name='taxi_zones',
            con=engine,
            if_exists='append'
        )

if __name__ == "__main__":
    main()
