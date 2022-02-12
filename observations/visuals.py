import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

data = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/pws.txt", delimiter="\t")

crs = {'init': 'EPSG:4326'}
geometry = [Point(xy) for xy in zip(data['longitude'], data['latitude'])]
data = gpd.GeoDataFrame(data, crs=crs, geometry=geometry)

map = gpd.read_file(
    "C:/Users/Maarten/Documents/Onderzoek/observations/shapefile/provinces_L08.shp")
fig, ax = plt.subplots(figsize=(10, 10))
map.to_crs(epsg=4326).plot(ax=ax, color='lightgrey', edgecolor="black")
data.plot(ax=ax)
ax.set_title('Belgium')

plt.show()
