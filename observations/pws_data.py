import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

date = "20210715"
data = pd.read_csv(
    f"C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_full.txt", delimiter="\t")

precipitation = data["precipitation"]
print("Mean precipitation")
print(np.mean(precipitation))
print("Standard deviation precipitation")
print(np.std(precipitation))

plt.title(f"Precipitation n={len(data)}")
plt.hist(precipitation, density=True, bins=15)
plt.xlabel("precipitation (mm)")
plt.savefig(f"data_{date}")
