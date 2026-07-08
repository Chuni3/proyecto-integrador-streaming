import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA", layout="wide")
st.title("📈 Análisis Exploratorio de Datos (EDA)")

# 1. Cargar datos
df = pd.read_csv('data/processed/dataset_limpio.csv')

# --- GRÁFICO 1: Distribución por Plan ---
st.subheader("Distribución de Planes de Suscripción")
fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.countplot(data=df, x='subscription_plan', ax=ax1, palette='viridis')
st.pyplot(fig1)

# --- GRÁFICO 2: Histograma de Edades ---
st.subheader("Distribución de Edades")
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.histplot(data=df, x='age', kde=True, ax=ax2, color='skyblue')
st.pyplot(fig2)

# --- GRÁFICO 3: Minutos de visualización ---
st.subheader("Promedio de Minutos por Plan")
fig3, ax3 = plt.subplots(figsize=(8, 4))
# Asumiendo que esta es la lógica que usaste en el notebook
sns.barplot(data=df, x='subscription_plan', y='monthly_watch_time_mins', ax=ax3)
st.pyplot(fig3)

# --- GRÁFICO 4: Correlaciones ---
st.subheader("Matriz de Correlación")
fig4, ax4 = plt.subplots(figsize=(10, 6))
numeric_df = df.select_dtypes(include=['number'])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax4)
st.pyplot(fig4)