import streamlit as st
import pandas as pd
import plotly.express as px


def grafico_ipc(df):
    return px.line(df, x="fecha", y="valor")