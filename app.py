import streamlit as st

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

with st.spinner("Cargando datos...",show_time=True):
    time.sleep(2)
    consumer_data = get_consumer_data()

st.title("Finanzas Personales")

with st.sidebar:
    st.header(f"Hola 👋 {consumer_data['name']}")
    st.divider()

    st.button("Añadir",icon="➕",use_container_width=True)
    st.button("Personalizar",icon="✏️",use_container_width=True)
    st.divider()

    st.button("Preferencias", icon="⚙️",use_container_width=True)

