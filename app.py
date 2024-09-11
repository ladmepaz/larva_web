import streamlit as st

# Importa las funciones de las páginas
from app.pages import home, Microscopio
from app.components import sidebar

st.set_page_config(
    page_title="Microscopio Robótico",
    page_icon="🔬",
    layout="wide"
)

sidebar.load_sidebar()


