import requests
import streamlit as st
import pandas as pd
from datetime import date
from api_cliente import get_data
from calculos import calcular_ipc
from charts import grafico_ipc


def mostrar_ipc():
  
  max_fecha = date.today()

  df = get_data("148.3_INIVELNAL_DICI_M_26")
  df = df.sort_values("fecha")
  df = calcular_ipc(df)

  indicador = st.selectbox("elegi el indicador", ["acumulada durante el anio", "Interanual", "Mensual", "Entre dos fechas en especifico"])

  if indicador == "acumulada durante el anio" or indicador == "Entre dos fechas en especifico":

    col1, col2 = st.columns(2)

    with col1:

      if indicador == "acumulada durante el anio":
        desde = st.date_input("Desde", value=date(2026, 1,1), min_value=date(2026, 1,1), max_value=date(2026, 1,1))
      else:
       desde = st.date_input("Desde", value=date(2026, 1,1))
    
    with col2:
      if indicador == "acumulada durante el anio":
       hasta = st.date_input("Hasta", value = max_fecha, max_value= max_fecha, min_value= max_fecha)
      else:
        hasta = st.date_input("Hasta", value = max_fecha, min_value= desde)

    

    if indicador == "acumulada durante el anio":

      df_filtrado = df[
            (df["fecha"] >= pd.to_datetime(desde)) &
            (df["fecha"] <= pd.to_datetime(hasta))
        ]
    
      if df_filtrado.empty:
        st.warning("no hay datos en ese rango")
      else:

        if indicador == "acumulada durante el anio":

          st.write("Datos filtrados:", len(df_filtrado))

          inflacion_total = (
          (df_filtrado["valor"].iloc[-1] / df_filtrado["valor"].iloc[0]) - 1) * 100
          
          st.metric("Inflación acumulada", f"{inflacion_total:.2f}%")
          fig = grafico_ipc(df_filtrado)
          st.plotly_chart(fig)

    

    if indicador == "Entre dos fechas en especifico":

      if desde >= hasta:
        st.warning("La fecha 'desde' debe ser menor a 'hasta'")
        return
        

      if desde.year == hasta.year and desde.month == hasta.month:
        st.warning("Elegí al menos un mes de diferencia")
        return
        

      df_filtrado = df[
            (df["fecha"] >= pd.to_datetime(desde)) &
            (df["fecha"] <= pd.to_datetime(hasta))
        ]
      

      
      if df_filtrado.empty:
        st.warning("no hay datos en ese rango") 
        
      else:
        st.write("Datos filtrados:", len(df_filtrado))
        
        inflacion_total = (
        (df_filtrado["valor"].iloc[-1] / df_filtrado["valor"].iloc[0]) - 1) * 100
        
        st.metric("Inflación acumulada", f"{inflacion_total:.2f}%")
        fig = grafico_ipc(df_filtrado)
        st.plotly_chart(fig)

        st.write("Datos filtrados:", df_filtrado)

  if indicador == "Interanual":
    col1, col2 = st.columns(2)

    with col1:
        mes = st.selectbox("Mes", range(1, 13))

    with col2:
        anio = st.selectbox("Año", range(2020, date.today().year + 1))

    fecha_actual = date(anio, mes, 1)
    fecha_anterior = date(anio - 1, mes, 1)

    df_actual = df[df["fecha"] == pd.to_datetime(fecha_actual)]
    df_anterior = df[df["fecha"] == pd.to_datetime(fecha_anterior)]

    if df_actual.empty or df_anterior.empty:
        st.warning("No hay datos suficientes")
        return

    valor_actual = df_actual["valor"].iloc[0]
    valor_anterior = df_anterior["valor"].iloc[0]

    inflacion_interanual = ((valor_actual / valor_anterior) - 1) * 100

    st.metric("Inflación interanual", f"{inflacion_interanual:.2f}%", help="Mide la inflación de un mes con el mismo mes del año anterior", delta=" " if inflacion_interanual > 0 else "- ", # Un espacio con signo engaña al motor visual
    delta_color="normal")
    
  if indicador == "Mensual":
    col1, col2 = st.columns(2)

    with col1:

      meses = [
      "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
      "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"  ]
      mes = st.selectbox(
          "Mes",
          range(1, 13),
          format_func=lambda x: meses[x-1]
      )

    with col2:
        anio = st.selectbox(
            "Año",
            range(2020, date.today().year + 1),
            index=6
        )

    desde_final = date(anio, mes, 1)


    if mes == 1:
        mes_anterior = date(anio - 1, 12, 1)
    else:
        mes_anterior = date(anio, mes - 1, 1)

    st.info(f"Fecha seleccionada: {desde_final}")

    df_actual = df[df["fecha"] == pd.to_datetime(desde_final)]
    df_anterior = df[df["fecha"] == pd.to_datetime(mes_anterior)]

    if df_actual.empty or df_anterior.empty:
        st.warning("No hay datos suficientes para calcular la inflación")
        return

    valor_actual = df_actual["valor"].iloc[0]
    valor_anterior = df_anterior["valor"].iloc[0]

    inflacion_mensual = ((valor_actual / valor_anterior) - 1) * 100

    st.metric("Inflación mensual", f"{inflacion_mensual:.2f}%")

    

  

  
  

