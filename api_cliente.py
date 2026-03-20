import requests 
import pandas as pd

URL = "https://apis.datos.gob.ar/series/api/series/"

def get_data(id_serie):

    params = {
        "ids": id_serie,
        "limit": 5000
    }

    response = requests.get(URL, params=params)

    data = response.json()

    df = pd.DataFrame(data["data"], columns=["fecha", "valor"])

    df["fecha"] = pd.to_datetime(df["fecha"])

    return df