import streamlit as st
import pandas as pd


st.set_page_config(page_title="Exploración del Dataset", page_icon="📊")

st.title("📊 Exploración del Dataset")
st.markdown("""
En esta sección puedes explorar los datos interactivos. 
Hemos habilitado dos pestañas para que puedas comparar el archivo original (con todos sus errores iniciales) y el dataset final procesado tras nuestro pipeline de limpieza.
""")

st.divider()


try:
    df_raw = pd.read_json('data/raw/dataset_PI.json')
    df_limpio = pd.read_csv('data/processed/dataset_limpio.csv')
    
    
    tab1, tab2 = st.tabs(["✨ Dataset Limpio (Procesado)", "⚠️ Dataset Original (Crudo)"])
    
    with tab1:
        st.subheader("Datos Listos para Análisis")
        st.dataframe(df_limpio, use_container_width=True)
        st.caption(f"Filas: {df_limpio.shape[0]} | Columnas: {df_limpio.shape[1]}")
        
    with tab2:
        st.subheader("Datos Originales con Errores")
        st.dataframe(df_raw, use_container_width=True)
        st.caption(f"Filas: {df_raw.shape[0]} | Columnas: {df_raw.shape[1]}")

except FileNotFoundError:
    st.error("❌ Error: No se encontraron los archivos de datos. Asegúrate de que las rutas 'data/raw/dataset_PI.json' y 'data/processed/dataset_limpio.csv' sean correctas.")