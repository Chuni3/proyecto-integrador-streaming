import streamlit as st

st.set_page_config(page_title="Conclusiones", page_icon="📝", layout="wide")

st.title("📝 Conclusiones del Proyecto Integrador")

st.markdown("""
---
## 1. Conclusiones Principales

A lo largo de este análisis exploratorio y de dimensionalidad, hemos llegado a las siguientes conclusiones basadas en la evidencia recopilada:

* **Sobre el perfil de los usuarios:** Observamos que en la distribución de edades en nuestra plataforma predominan usuarios de entre 30 y 40 años.
* **Sobre el consumo y los planes:** Al analizar el promedio de minutos visualizados según el plan de suscripción, determinamos que predominan los planes premium y en menor cantidad los básicos, siendo que el gráfico de los planes contratados por los clientes muestra un comportamiento contrario.
* **Sobre las preferencias de contenido:** El género que genera mayor retención de tiempo general es el Thriller.
* **Sobre la predicción de comportamiento (PCA):** Tras aplicar un Análisis de Componentes Principales, confirmamos que las variables de edad, tiempo de visualización y tickets de soporte no forman grupos naturales que separen a los usuarios por plan. Concluimos que la elección del plan de suscripción no depende exclusivamente de estas métricas.

---
## 2. Limitaciones del Análisis

* El alcance de las conclusiones se encuentra condicionado por la información disponible y por las decisiones en el proceso de limpieza, como la eliminación de fechas erróneas, estandarización de palabras y minutos atípicos.
* Tenemos una cantidad limitada de variables descriptivas, lo que no nos permite basarnos en algo concreto a la hora de determinar, por ejemplo, por qué los usuarios acudieron a un plan específico.

""")
