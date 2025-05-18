import requests
import pandas as pd

urls = "http://api.open-notify.org/iss-now.json"

response = requests.get(url = urls)

response.raise_for_status()

df = response.json()
date = pd.to_datetime(df['timestamp'], errors="coerce",unit='s').strftime('%d-%b-%Y')
time = pd.to_datetime(df['timestamp'], errors="coerce",unit='s').strftime('%I:%M:%S %p')
l = pd.to_datetime(df['timestamp'], errors="coerce",unit='s').strftime('%d-%b-%Y : %I:%M:%S %p')
latitude = df["iss_position"]["latitude"]
longitude = df["iss_position"]["longitude"]

print(l)
