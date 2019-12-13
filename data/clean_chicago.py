import json
import geopandas as gp
import pandas as pd

filt = ["date", "block", "primary_type", "description", "location_description", "arrest", "year", "latitude", "longitude"]
df = get_dataframe("chicago_crime", "crime")[filt]
df2018 = df[df.year == 2018].dropna()
gdf2018 = gp.GeoDataFrame(df2018, geometry=gp.points_from_xy(df2018.longitude, df2018.latitude)).drop(["latitude", "longitude"], axis=1)

