import streamlit as st
import requests
from pages.ipc import mostrar_ipc
from pages.salarios import mostrar_salarios
from pages.pobreza import mostrar_pobreza



st.title("Dashboard economico de Argentina")

indicador = st.selectbox("elegi el indicador", ["IPC", "Salarios", "Actividad económica", "Pobreza", "Desempleo"])

if indicador == "IPC":
    mostrar_ipc()

elif indicador == "Salarios":
    mostrar_salarios()

elif indicador == "Pobreza":
    mostrar_pobreza()