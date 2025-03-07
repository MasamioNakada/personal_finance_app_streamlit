import streamlit as st
from views import landing
from utils.data_loaders import get_consumer_data

#temp libraries
import time

# Configuración de la página
st.set_page_config(
    page_title="Finanzas Personales",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

#Configuracion de navegacion
landing = st.Page("views/landing.py",title="Inicio",icon="🏠")
user_dashboard = st.Page("views/dashboard/user_dashboard.py",title="Dashboard",icon="📊")

pg = st.navigation([landing,user_dashboard],position="hidden")
pg.run()