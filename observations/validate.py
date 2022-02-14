import pandas as pd

date = "20210713"
data = pd.read_csv(
    f"C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_{date}.txt", delimiter="\t")

data = data[data["precipitation"] > 2.0]
data = data[data["precipitation"] < 80.0]

data.to_csv(f"precipitation_{date}_v.txt", "\t", index=False)
