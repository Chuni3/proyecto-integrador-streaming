import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns

st.set_page_config(page_title="PCA", page_icon="🧬")
st.title("🧬 Análisis de Componentes Principales")

df = pd.read_csv('data/processed/dataset_limpio.csv')
features = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
x = df[features].dropna()
x_scaled = StandardScaler().fit_transform(x)

pca = PCA(n_components=3)
pca.fit(x_scaled)

# Gráfico 1: Varianza
st.subheader("Gráfico de Varianza Explicada")
fig1, ax1 = plt.subplots()
ax1.bar(['PC1', 'PC2', 'PC3'], pca.explained_variance_ratio_)
st.pyplot(fig1)

st.markdown("""
**Interpretación:** Aplicamos StandardScaler para normalizar variables con escalas distintas. 
El gráfico muestra cómo se distribuye la información. Observamos que reteniendo los 
primeros dos componentes (PC1 y PC2) capturamos la gran mayoría de la varianza original.
""")

# Gráfico 2: Proyección 2D
st.subheader("Proyección 2D de usuarios")
pca_data = pca.transform(x_scaled)
pca_df = pd.DataFrame(data=pca_data, columns=['PC1', 'PC2', 'PC3'])
pca_df['plan'] = df.loc[x.index, 'subscription_plan'].values

fig2, ax2 = plt.subplots()
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='plan', ax=ax2)
st.pyplot(fig2)

st.markdown("""
**Interpretación:** En este mapa proyectamos a los usuarios en 2 dimensiones. 
Al estar los puntos de los distintos planes mezclados, concluimos que las variables 
numéricas (edad, tiempo y tickets) no bastan por sí solas para predecir el plan 
de suscripción.
""")