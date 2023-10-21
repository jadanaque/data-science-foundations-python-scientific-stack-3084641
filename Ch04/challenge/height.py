# Draw the running track from track.csv
#
# - Sample data to a minute interval
# - Markers should be blue if the height is below 100 meter, otherwise red
# %%
import pandas as pd
import folium
# %%
track_df = pd.read_csv('./Ch04/challenge/track.csv',
                       parse_dates=['time'],
                       index_col='time')
# %%
center = [track_df['lat'].mean(), track_df['lng'].mean()]

m = folium.Map(
    location=center,
    zoom_start=15
)
m
# %%
track_minute = track_df.resample('min').mean()
print(track_minute)
# %%


def add_marker(row):
    location = tuple(row[['lat', 'lng']])
    marker = folium.CircleMarker(
        location,
        color='red' if row['height'] >= 100 else 'blue',
        radius=2,
        popup=f"{row.name.strftime('%H:%M')} \n {row.height}"
    )
    marker.add_to(m)


# %%
track_minute.apply(add_marker, axis=1)
m
# %%
folium.PolyLine(track_minute[['lat', 'lng']].apply(
    tuple, axis=1), color='gray').add_to(m)
m

# %%
