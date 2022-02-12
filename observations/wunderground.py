import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")

station_id, lats, lons, state = [], [], [], []

lat = 49.5
while lat < 50.8:
    lon = 4.8
    while lon < 6.4:
        response = requests.get(
            f"https://api.weather.com/v3/location/near?geocode={lat},{lon}&product=pws&format=json&apiKey={API_KEY}")

        data = response.json()
        data = data["location"]
        for index, station in enumerate(data["stationId"]):
            if data["qcStatus"][index] != 0:
                if station not in station_id:
                    station_id.append(station)
                    lats.append(data["latitude"][index])
                    lons.append(data["longitude"][index])
        lon = lon + 0.1

    lat = lat + 0.1
    print(lat)

df = pd.DataFrame(
    {"stationId": station_id, "latitude": lats, "longitude": lons})
df.to_csv("pws.txt", "\t", index=False)
