import streamlit as st

def app():
    st.title("Hola")
    st.write("esta es uan prueba")

    # Agregar un botón
    if st.button("Haz clic aquí"):
        st.write("¡Botón clickeado!")