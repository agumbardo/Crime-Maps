import json
import geopandas as gp
import pandas as pd
import numpy as np
from fetch_data import get_dataframe
from bokeh.io import output_notebook, show, output_file, export_png, push_notebook
from bokeh.plotting import figure, gmap
from bokeh.models import GeoJSONDataSource, GMapOptions, ColumnDataSource, WheelZoomTool, LinearColorMapper, ColorBar, CustomJS
from bokeh.palettes import mpl, viridis
from bokeh.tile_providers import get_provider, Vendors
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Slider, Toggle
from bokeh.layouts import column
from bokeh.models.tools import HoverTool

# Filter and drop null rows
filt = ["date", "block", "primary_type", "description", "location_description", "arrest", "year", "latitude", "longitude"]
df = get_dataframe("chicago_crime", "crime")[filt].dropna()

# Extract time info into seperate columns for easy querying
df["year"] = df["year"].astype("int16")
df["month"] = df.date.apply(lambda x: x.month).astype("int8")
df["day"] = df.date.apply(lambda x: x.day).astype("int8")
df["hour"] = df.date.apply(lambda x: x.hour).astype("int8")

# Create geometry from lat and long, project to the web mercator, and drop unnecessary rows
gdf = gp.GeoDataFrame(df, geometry=gp.points_from_xy(df.longitude, df.latitude), crs={'init': 'epsg:4326'})
gdf = gdf.to_crs({'init': 'epsg:3857'})
gdf = gdf.drop(["latitude", "longitude", "date"], axis=1)

crime_nums = {}
for y in range(2016,2019):
    crime_nums[y] = {}
    for m in range(1,13):
        print(y, m, end=' ')
        crime_nums[y][m] = {}
        filt = (gdf["year"] == y) & (gdf["month"] == m)
        geom = gdf[filt].geometry
        for _, row in bound.iterrows():
            cn = row["com_num"]
            com = row["geometry"]
            crime_nums[y][m][cn] = 0
            for point in geom:
                if com.contains(point):
                    crime_nums[y][m][cn] += 1
        print("DONE")

with open('crime_nums.json', 'w') as fp:
    json.dump(crime_nums, fp)

print("saved to crime_nums.json")