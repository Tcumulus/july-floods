import pandas as pd
import requests

validated_station_id, precipitation, lats, lons = [], [], [], []
date = "20210713"
min_threshold, max_treshold = 0, 80

data = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/pws.txt", delimiter="\t")

station_ids = data["stationId"].tolist()

for station_id in station_ids:
    response = requests.get(
        f"https://api.weather.com/v2/pws/history/daily?stationId={station_id}&format=json&units=m&date={date}&apiKey=2b269bf9fe864282a69bf9fe86e28259&numericPrecision=decimal")
    response = response.json()
    response = response["observations"]
    if len(response) > 0:
        if response["metric"][precipitation] > min_threshold or response["metric"][precipitation] < max_treshold:
            response = response[0]
            lats.append(response["lat"])
            lons.append(response["lon"])

            response = response["metric"]
            precipitation.append(response["precipTotal"])
            validated_station_id.append(station_id)

df = pd.DataFrame(
    {"stationId": validated_station_id, "latitude": lats, "longitude": lons, "precipitation": precipitation})
df.to_csv(f"precipitation_{date}.txt", "\t", index=False)
