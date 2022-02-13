import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/precipitation_20210713.txt", delimiter="\t")

precipitation = data["precipitation"]
print("Mean precipitation")
print(np.mean(precipitation))
print("Standard deviation precipitation")
print(np.std(precipitation))

plt.hist(precipitation, density=True, bins=30)
plt.ylabel("precipitation")
plt.show()
