import pandas as pd

data12 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210712.txt", delimiter="\t")
data13 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210713_v.txt", delimiter="\t")
data14 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210714_v.txt", delimiter="\t")
data15 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210715_v.txt", delimiter="\t")

data = pd.merge(data12, data13, on=[
                "stationId", "longitude", "latitude"], how='inner')
data = data.rename(columns={
                   "precipitation_x": "precipitation_12", "precipitation_y": "precipitation_13"})

data = pd.merge(data, data14, on=[
                "stationId", "longitude", "latitude"], how='inner')
data = data.rename(columns={"precipitation": "precipitation_14"})

data = pd.merge(data, data15, on=[
                "stationId", "longitude", "latitude"], how='inner')
data = data.rename(columns={"precipitation": "precipitation_15"})

data["precipitation"] = data["precipitation_12"] + \
    data["precipitation_13"] + \
    data["precipitation_14"] + data["precipitation_15"]

data.to_csv(f"precipitation_full.txt", "\t", index=False)
