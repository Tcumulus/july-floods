import pandas as pd

data12 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210712.txt", delimiter="\t")
data13 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210713_v.txt", delimiter="\t")
data14 = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/precipitation_20210714_v.txt", delimiter="\t")

data = pd.merge(data12, data13, on=[
                "stationId", "longitude", "latitude"], how='inner')
data = pd.merge(data, data14, on=[
                "stationId", "longitude", "latitude"], how='inner')

data["c_precipitation"] = data["precipitation"] + \
    data["precipitation_x"] + data["precipitation_y"]

data = data.drop(["precipitation", "precipitation_x",
                 "precipitation_y"], axis=1)

data = data.rename(columns={"c_precipitation": "precipitation"})

data.to_csv(f"precipitation_cumulative.txt", "\t", index=False)
