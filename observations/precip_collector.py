import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")

validated_station_id, precipitation, lats, lons = [], [], [], []
date = "20210715"

data = pd.read_csv(
    "C:/Users/Maarten/Documents/Onderzoek/observations/data/pws.txt", delimiter="\t")

station_ids = data["stationId"].tolist()

for station_id in station_ids:
    response = requests.get(
        f"https://api.weather.com/v2/pws/history/daily?stationId={station_id}&format=json&units=m&date={date}&apiKey={API_KEY}&numericPrecision=decimal")
    response = response.json()
    response = response["observations"]
    if len(response) > 0:
        response = response[0]
        lats.append(response["lat"])
        lons.append(response["lon"])

        response = response["metric"]
        precipitation.append(response["precipTotal"])
        validated_station_id.append(station_id)
        print(station_id)

df = pd.DataFrame(
    {"stationId": validated_station_id, "latitude": lats, "longitude": lons, "precipitation": precipitation})
df.to_csv(f"precipitation_{date}.txt", "\t", index=False)
