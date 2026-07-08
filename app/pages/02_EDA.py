import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA", page_icon="📈", layout="wide")
st.title("📈 Análisis Exploratorio de Datos (EDA)")

# 1. Cargar el dataset procesado y limpio
# Nota: La ruta en Streamlit debe ser relativa a la raíz del repositorio
df = pd.read_csv('data/processed/dataset_limpio.csv')

# Configuración visual para que los gráficos se vean profesionales
sns.set_theme(style="whitegrid")

# ==========================================
# GRÁFICO 1: Distribución de Planes
# ==========================================
st.subheader("1. Distribución de Usuarios por Plan de Suscripción")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x='subscription_plan', palette='viridis', order=df['subscription_plan'].value_counts().index, ax=ax1)

ax1.set_title('Distribución de Usuarios por Plan de Suscripción', fontsize=14)
ax1.set_xlabel('Plan de Suscripción', fontsize=12)
ax1.set_ylabel('Cantidad de Usuarios', fontsize=12)

# Agregar las cantidades arriba de cada barra (tal como lo tenías)
for p in ax1.patches:
    ax1.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')

st.pyplot(fig1)

# ==========================================
# GRÁFICO 2: Histograma de Edades
# ==========================================
st.subheader("2. Distribución de la Edad de los Usuarios")
fig2, ax2 = plt.subplots(figsize=(9, 5))
sns.histplot(data=df, x='age', bins=20, kde=True, color='skyblue', ax=ax2)

ax2.set_title('Distribución de la Edad de los Usuarios', fontsize=14, fontweight='bold')
ax2.set_xlabel('Edad (Años)', fontsize=12)
ax2.set_ylabel('Cantidad de Usuarios (Frecuencia)', fontsize=12)

st.pyplot(fig2)

# ==========================================
# GRÁFICO 3: Promedio de Minutos por Plan
# ==========================================
st.subheader("3. Promedio de Minutos Visualizados al Mes por Plan")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.barplot(data=df, x='subscription_plan', y='monthly_watch_time_mins', palette='Set2', errorbar=None, ax=ax3)

ax3.set_title('Promedio de Minutos Visualizados al Mes por Plan', fontsize=14, fontweight='bold')
ax3.set_xlabel('Plan de Suscripción', fontsize=12)
ax3.set_ylabel('Promedio de Minutos / Mes', fontsize=12)

st.pyplot(fig3)

# ==========================================
# GRÁFICO 4: Minutos Promedio por Género Favorito
# ==========================================
st.subheader("4. Promedio de Minutos de Visualización Mensual por Género Favorito")
fig4, ax4 = plt.subplots(figsize=(10, 5))

# Calculamos el promedio de minutos para ordenar las barras de mayor a menor
orden_generos = df.groupby('favorite_genre')['monthly_watch_time_mins'].mean().sort_values(ascending=False).index

sns.barplot(data=df, x='favorite_genre', y='monthly_watch_time_mins', palette='viridis', order=orden_generos, errorbar=None, ax=ax4)

ax4.set_title('Promedio de Minutos de Visualización Mensual por Género Favorito', fontsize=14, fontweight='bold')
ax4.set_xlabel('Género Favorito', fontsize=12)
ax4.set_ylabel('Minutos Promedio / Mes', fontsize=12)
plt.setp(ax4.get_xticklabels(), rotation=15) # Rotamos los nombres para que se lean bien

st.pyplot(fig4)

# ==========================================
# GRÁFICO 5: Edad vs. Minutos por Plan de Suscripción
# ==========================================
st.subheader("5. Relación entre Edad y Minutos de Visualización según el Plan")
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='monthly_watch_time_mins', hue='subscription_plan', alpha=0.7, palette='deep', ax=ax5)

ax5.set_title('Relación entre Edad y Minutos de Visualización según el Plan', fontsize=14, fontweight='bold')
ax5.set_xlabel('Edad (Años)', fontsize=12)
ax5.set_ylabel('Minutos Visualizados al Mes', fontsize=12)
ax5.legend(title='Plan de Suscripción')

st.pyplot(fig5)