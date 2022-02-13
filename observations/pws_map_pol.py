import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

date = "20210712"
data = pd.read_csv(
    f"C:/Users/Maarten/Documents/Onderzoek/observations/precipitation_{date}.txt", delimiter="\t")

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
gdf.to_crs(epsg=4326).plot(color='lightgrey', edgecolor="black")

plt.contourf(xi, yi, zi, np.arange(0, max(z), round(max(z)/10, 1)), alpha=0.7)
plt.title(f"Precipitation {date}")
plt.colorbar(label="precipitation (mm)")
plt.xlabel("lat (°)")
plt.ylabel("lon (°)")
plt.show()