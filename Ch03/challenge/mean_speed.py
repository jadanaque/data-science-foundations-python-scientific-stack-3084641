# What is the mean speed (mile/hour) in taxi.parquet?

# - Run download_data.py to download the data

# %%
import pandas as pd
import numpy as np

# %%
# Read Data from parquet file
taxi_df = pd.read_parquet('../../taxi.parquet')
print(taxi_df)

# %%
# get traveled time
traveled_times = taxi_df['tpep_dropoff_datetime'] - \
    taxi_df['tpep_pickup_datetime']

# %%
# convert times to hours
traveled_times_hr = traveled_times / pd.Timedelta(1, 'hour')
print(traveled_times_hr)

# %%
speeds = taxi_df['trip_distance'] / traveled_times_hr

# %%
speeds_noinf = speeds[~np.isinf(speeds)]

# %%
print(speeds.shape[0])
print(speeds_noinf.shape)

# %%
speeds_noinf.mean()

# %%
print(taxi_df.iloc[speeds.argmax()])
print(speeds[speeds.argmax()])

# %%
sum(speeds == np.inf)
speeds.shape[0]-sum(speeds == np.inf)

# %%
tst = np.array([True, True, False])
print(tst)
print(~tst)

# %%
# Following the solution provided
taxi_df = taxi_df[taxi_df['tpep_dropoff_datetime']
                  > taxi_df['tpep_pickup_datetime']]

# %%
print(taxi_df.shape)

traveled_times = taxi_df['tpep_dropoff_datetime'] - \
    taxi_df['tpep_pickup_datetime']
print(traveled_times)

# %%
traveled_times_hr = traveled_times / pd.Timedelta(1, 'hour')

# %%
speeds = taxi_df['trip_distance'] / traveled_times_hr

# %%
print(speeds.mean())

# %%
tst_vc = np.array([1, 2, 3])
bool_vc = np.array([True, True, False])
print(tst_vc)
print(bool_vc)

# %%
tst_vc[~bool_vc]
