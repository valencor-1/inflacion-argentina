import requests
import pandas as pd

URL = "https://apis.datos.gob.ar/series/api/series/"

params = {
    "ids": "148.3_INIVELNAL_DICI_M_26",
    "limit": 5000
}

response = requests.get(URL, params=params)
data = response.json()

df = pd.DataFrame(data["data"], columns=["fecha", "ipc"])

df["fecha"] = pd.to_datetime(df["fecha"])

print(df.tail())