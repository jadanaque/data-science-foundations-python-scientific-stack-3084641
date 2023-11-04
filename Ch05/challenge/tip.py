"""
- Load the taxi data.
- Remove all rows with either total_amount <= 0 or
  passenger_count == 0
- Create a bar chart of average tip % per passenger_count
- Create a bar chart of average tip % per day of week
"""
# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# %%
os.chdir("./Ch05/challenge")

# %%
# Reading taxi data
time_cols = [
    'tpep_pickup_datetime',
    'tpep_dropoff_datetime',
]

df = pd.read_csv('taxi.csv',
                 parse_dates = time_cols)

df.head()

# %%
df = df[(df['total_amount'] > 0) & (df['passenger_count'] != 0)]

# %%
df['tip_pct'] = df['tip_amount'] / df['total_amount'] * 100
df[['tip_amount', 'total_amount', 'tip_pct']]

# %%
df.groupby('passenger_count')['tip_pct'].mean().plot.bar(
  title = 'Tip % by Passenger Count',
  rot = 0
)
# %%
df.groupby(df['tpep_pickup_datetime'].dt.day_name())['tip_pct'].mean().plot.bar()

# %%
from calendar import day_abbr

# %%
day_week = df['tpep_pickup_datetime'].dt.day_of_week
# %%
by_day = df.groupby(day_week)['tip_pct'].mean()

by_day.plot.bar(title = 'Tip % by Day', rot = 45)
plt.ylabel('Tip %')
plt.xlabel('Day of Week')
#plt.xticks(ticks=plt.xticks()[0], labels = [day_abbr[v] for v in plt.xticks()[0]])
plt.xticks(ticks=plt.xticks()[0], labels = day_abbr)

print(plt.xticks())