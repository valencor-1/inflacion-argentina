import pandas as pd


def calcular_ipc(df):
    df["inflacion_mensual"] = df["valor"].pct_change() * 100
    return df

def ipc_interanual(df):
    df["inflacion_interanual"] = df["ipc"].pct_change(12) * 100
    return df

def acumulada_en_el_anio(df):
    df["año"] = df["fecha"].dt.year
    df["inflacion_acumulada"] = df.groupby("año")["ipc"].pct_change().cumsum() * 100