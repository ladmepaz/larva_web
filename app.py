import streamlit as st
from app.components.sidebar import load_sidebar
from app.pages.home import show_home

# Configuración básica de la aplicación
st.set_page_config(page_title="Microscopio Robótico", layout="wide")

# Cargar la barra lateral
load_sidebar()

# Cargar la página principal
show_home()