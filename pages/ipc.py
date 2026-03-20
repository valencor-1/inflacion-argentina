import requests
import streamlit as st
import pandas as pd
from datetime import date
from api_cliente import get_data
from calculos import calcular_ipc
from charts import grafico_ipc


def mostrar_ipc():
  
  st.header("IPC")

  max_fecha = date.today()

  desde = st.date_input("Desde", value=date(2024, 1,1))
  hasta = st.date_input("Hasta", value = max_fecha, max_value= max_fecha)

  if desde >= hasta:
    st.warning("La fecha 'desde' debe ser menor a 'hasta'")
    return
    

  if desde.year == hasta.year and desde.month == hasta.month:
    st.warning("Elegí al menos un mes de diferencia")
    return
    

  df = get_data("148.3_INIVELNAL_DICI_M_26")

  df = calcular_ipc(df)

  df_filtrado = df[
        (df["fecha"] >= pd.to_datetime(desde)) &
        (df["fecha"] <= pd.to_datetime(hasta))
    ]
  
  if df_filtrado.empty:
    st.warning("no hay datos en ese rango")
  else:
    st.write("Datos totales:", len(df))
    st.write("Datos filtrados:", len(df_filtrado))
    st.write(df_filtrado.head())

    ultimo = df_filtrado["inflacion_mensual"].iloc[-1]
    
    st.metric("Inflación mensual", f"{ultimo:.2f}%")
    fig = grafico_ipc(df_filtrado)
    st.plotly_chart(fig)

