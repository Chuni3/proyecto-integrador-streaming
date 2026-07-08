import streamlit as st

# 1. Configuración principal de la página (debe ser el primer comando de Streamlit)
st.set_page_config(
    page_title="PI Minería de Datos - Streaming",
    page_icon="🍿",
    layout="centered"
)

# 2. Título y subtítulo
st.title("🎬 Análisis de Usuarios de Streaming")
st.subheader("Proyecto Integrador - Minería de Datos 1")
st.markdown("---")

# 3. Mensaje de bienvenida
st.markdown("""
¡Bienvenidos a la presentación interactiva de nuestro análisis!

Esta aplicación web fue diseñada para comunicar de forma dinámica los hallazgos obtenidos durante la exploración del dataset de usuarios de nuestra plataforma de streaming. 

A través del menú lateral, podrá navegar por las distintas etapas de nuestro trabajo:
* *Dataset:* Vista interactiva de los datos crudos y limpios.
* *EDA:* Gráficos de nuestro Análisis Exploratorio de Datos.
* *PCA:* Resultados de la Reducción de Dimensionalidad.
* *Conclusiones:* Resumen de los hallazgos clave.
""")

# 4. Tarjeta de información (Reemplaza con tus datos)
st.info("*Integrante:* Baudano Walter Gabriel")