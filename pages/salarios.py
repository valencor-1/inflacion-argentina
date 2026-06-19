import requests
import streamlit as st
import pandas as pd
from datetime import date
from api_cliente import get_data

def mostrar_salarios():

    df = get_data("149.1_TL_INDIIOS_OCTU_0_21")
    #arranca en octubre del 2016

    df = df.sort_values("fecha")

    #st.write(df.head(10))

    print("datos filtrados", df.tail(5))

    indicador = st.selectbox("elegi el indicador", ["mensual", "anual"])

    if indicador == "mensual":
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
                range(2016, date.today().year + 1),
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
            st.warning("No hay datos suficientes para calcular")
            return
        
        valor_actual = df_actual["valor"].iloc[0]
        valor_anterior = df_anterior["valor"].iloc[0]

        variacion_mensual = ((valor_actual / valor_anterior) - 1) * 100

        st.metric("Variación mensual del salario", f"{variacion_mensual:.2f}%", delta=" respecto al mes anterior")