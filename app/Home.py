import streamlit as st

# Configuración principal de la página (Siempre debe ser la primera línea de Streamlit)
st.set_page_config(
    page_title="Proyecto Minería de Datos",
    page_icon="🎬",
    layout="wide"
)

# ==========================================
# CARTEL DE BIENVENIDA PERSONALIZADO
# ==========================================
st.markdown("""
<div style="background-color: #0E1117; padding: 30px; border-radius: 15px; border: 2px solid #4B4B4B; text-align: center; box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);">
    <h1 style="color: #4CB4F3; margin-bottom: 10px;">🎬 Proyecto Integrador: proyecto integrador</h1>
    <h3 style="color: #E0E0E0; margin-top: 0px;">Minería de Datos</h3>
    <p style="color: #A0A0A0; font-size: 18px; margin-top: 20px;">Presentado por: <b>Baudano Walter Gabriel</b></p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ==========================================
# INSTRUCCIONES DE NAVEGACIÓN
# ==========================================
st.markdown("""
### 👋 ¡Bienvenido a la aplicación interactiva!

A través de esta plataforma, podrás explorar el trabajo realizado sobre un dataset de usuarios de una plataforma de streaming. Hemos aplicado técnicas de limpieza, análisis exploratorio y reducción de dimensionalidad para descubrir patrones de comportamiento.

👈 **Utiliza el menú lateral izquierdo para navegar por las distintas etapas del proyecto:**

* 🗃️ **Dataset:** Explora la diferencia entre los datos crudos y los datos procesados.
* 📈 **EDA:** Visualiza los gráficos de nuestro Análisis Exploratorio de Datos.
* 🧬 **PCA:** Descubre cómo se proyectan las variables numéricas en el espacio.
* 📝 **Conclusiones:** Revisa los hallazgos finales y las limitaciones de nuestra investigación.
""")

# Un toque extra visual al final
st.info("💡 **Tip:** Asegúrate de expandir el menú lateral si estás navegando desde un celular o pantalla pequeña.")