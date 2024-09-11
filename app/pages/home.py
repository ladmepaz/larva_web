# app/pages/home.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def app():
    st.title("Página de Inicio del Microscopio Robótico")
    st.write("Bienvenido a la interfaz del microscopio robótico. Aquí puedes ver datos y gráficos.")

    # Generar datos de ejemplo
    data = pd.DataFrame({
        'x': np.arange(10),
        'y': np.random.rand(10)
    })

    # Mostrar datos en una tabla
    st.write("Datos de ejemplo:")
    st.dataframe(data)

    # Crear un gráfico
    st.write("Gráfico de ejemplo:")
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'], marker='o')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Gráfico de Datos Ejemplo')
    st.pyplot(fig)

    # Agregar una entrada de texto
    user_input = st.text_input("Introduce un valor:")
    st.write(f"Valor introducido: {user_input}")

    # Agregar un botón
    if st.button("Haz clic aquí"):
        st.write("¡Botón clickeado!")
