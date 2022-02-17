import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from matplotlib import cm

date = "20210715"
data = pd.read_csv(
    f"C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_{date}_v.txt", delimiter="\t")

y = np.array(data["latitude"])
x = np.array(data["longitude"])
z = np.array(data["precipitation"])

# target grid to interpolate to
xi = np.arange(4.7, 6.6, 0.05)
yi = np.arange(49.4, 51, 0.05)
xi, yi = np.meshgrid(xi, yi)

# interpolate
zi = griddata((x, y), z, (xi, yi), method='linear')

# plot
gdf = gpd.read_file(
    "C:/Users/Maarten/Documents/Onderzoek/observations/shapefile/provinces_L08.shp")
rivers = gpd.read_file(
    "C:/Users/Maarten/Documents/Onderzoek/observations/shapefile/Hydro_08.shp")

ax = gdf.to_crs(epsg=4326).plot(color='lightgrey', edgecolor="black")
#rivers.to_crs(epsg=4326).plot(ax=ax, edgecolor="gray", alpha=0.3)

plt.contourf(xi, yi, zi, np.arange(0, 280, 20),
             alpha=0.7, cmap=cm.jet, extend='max')
#plt.title(f"Precipitation {date}")
plt.title("precipitation 20210712-15")
plt.colorbar(label="precipitation (mm)")
plt.xlabel("lat (°)")
plt.ylabel("lon (°)")
plt.savefig(f"plot_{date}")
