import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

date = "20210712"

# pws points
# data = pd.read_csv(
#    "C:/Users/Maarten/Documents/Onderzoek/observations/pws.txt", delimiter="\t")

data = pd.read_csv(
    f"C:/Users/Maarten/Documents/Onderzoek/observations/precipitation_{date}.txt", delimiter="\t")

crs = {'init': 'EPSG:4326'}
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
_data = gpd.GeoDataFrame(data, crs=crs, geometry=geometry)

gdf = gpd.read_file(
    "C:/Users/Maarten/Documents/Onderzoek/observations/shapefile/provinces_L08.shp")
fig, ax = plt.subplots(figsize=(10, 10))
gdf.to_crs(epsg=4326).plot(ax=ax, color='lightgrey', edgecolor="black")
_data.plot(ax=ax, column=data["precipitation"], legend=True, legend_kwds={
           "label": "precipitation (mm)"})
ax.set_title(f"Precipitation {date}")

plt.xlabel("lat(°)")
plt.ylabel("lon(°)")

plt.show()
