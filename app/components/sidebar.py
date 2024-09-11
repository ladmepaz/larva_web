# app/components/sidebar.py

import streamlit as st
from streamlit_option_menu import option_menu
from app.pages import home, Microscopio

def load_sidebar():
    with st.sidebar:
        app = option_menu(
            menu_title=None,
            options=['Home', 'Microscopio'],
            icons=['house-fill','person-circle'],
            default_index=0,
            orientation='horizontal',
            styles={"container": {"padding": "5!important"},
                    "icon": {"color": "white", "font-size": "15x"}, 
                    "nav-link": {"color":"white","font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "gray"},
                    "nav-link-selected": {"background-color": "#02ab21"},}
            )
    if app == "Home":
        home.app()
    if app == "Microscopio":
        Microscopio.app()
