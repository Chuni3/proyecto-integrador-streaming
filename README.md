# Proyecto Integrador: Minería de Datos 1

## Información general
* integrante: Baudano Walter Gabriel



## Objetivo del proyecto
Aplicar los contenidos de Minería de Datos 1 para construir un análisis reproducible y comunicable. El objetivo particular es comprender los patrones de consumo de los usuarios de una plataforma de streaming y evaluar, mediante análisis exploratorio y reducción de dimensionalidad, si el comportamiento numérico de uso (minutos y soporte) es un factor determinante en la elección de su plan de suscripción.

## Dataset
El proyecto utiliza un conjunto de datos provisto en formato JSON que contiene información demográfica y de comportamiento de usuarios de streaming. El archivo original cuenta con variables numéricas (edad, tiempo de visualización, tickets de soporte) y categóricas (género favorito, país, plan de suscripción, fecha de último ingreso). El dataset original se encuentra preservado sin alteraciones en la carpeta `data/raw/`, mientras que la versión curada utilizada para el análisis se ubica en `data/processed/`.

## Estructura del repositorio
PI_Mineria_Datos_1/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
├── app/
│   ├── Home.py
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
├── reports/
│   └── informe_final.pdf
└── logs/
    └── pipeline_log.csv

## Preparación y calidad de datos
Las decisiones de limpieza surgieron de la inspección documentada y se aplicaron estrictamente con evidencia empírica. Se estableció un rango lógico para la variable edad (18 a 100 años) y se descartaron registros con cantidades de tickets de soporte negativos o absurdos. Los valores nulos en el tiempo de visualización se imputaron con la mediana del dataset para conservar el volumen de la muestra. Adicionalmente, se estandarizaron los formatos textuales de los planes de suscripción, géneros favoritos y países para evitar duplicidades por diferencias de idioma o mayúsculas. Las fechas de ingreso irrecuperables fueron descartadas. El proceso paso a paso puede revisarse en el notebook `notebooks/02_calidad_y_limpieza.ipynb` y la trazabilidad completa se encuentra registrada en `logs/pipeline_log.csv`.

## Resumen del análisis exploratorio
Se realizó un análisis univariado, bivariado y multivariado sobre el dataset limpio para responder a nuestras preguntas de negocio. Se evaluó la distribución demográfica de los clientes y la popularidad de los distintos planes de suscripción. Al cruzar las variables, se analizó el impacto del tipo de plan sobre los minutos de visualización mensuales promedio y se determinaron las preferencias de consumo según el género de contenido favorito. El detalle de las interpretaciones, así como la matriz de correlación entre variables numéricas, se encuentra disponible en `notebooks/03_eda.ipynb`.

## Reducción de dimensionalidad
Se aplicó un Análisis de Componentes Principales (PCA) empleando las variables `age`, `monthly_watch_time_mins` y `customer_support_tickets`. Previo al algoritmo, los datos fueron escalados utilizando `StandardScaler`. Los resultados demostraron que los dos primeros componentes principales logran capturar la mayor parte de la varianza del sistema. Sin embargo, la proyección bidimensional no reveló agrupaciones (clústers) diferenciadas por plan de suscripción. El análisis técnico y los gráficos de varianza están documentados en `notebooks/04_pca.ipynb`.

## Visualización interactiva
Los resultados principales de este proyecto han sido volcados en una aplicación web desarrollada con Streamlit. La aplicación está diseñada para comunicar los hallazgos a un público general.
* *Enlace a la aplicación pública:* [Pega aquí tu link a Streamlit Cloud cuando lo tengas]
* *Código fuente de la app:* Carpeta `app/`

## Cómo ejecutar localmente
Para reproducir este proyecto o ejecutar la aplicación web en un entorno local, siga estos pasos:
1. Clone este repositorio.
2. Instale las dependencias ejecutando: `pip install -r requirements.txt`
3. Para ver los análisis, abra y ejecute los archivos de la carpeta `notebooks/`.
4. Para levantar la aplicación interactiva, ejecute en la terminal: `streamlit run app/Home.py`

## Conclusiones
El análisis evidencia patrones claros en las preferencias de género de contenido y distribuciones demográficas de los usuarios. No obstante, el estudio de componentes principales demostró que las métricas de interacción analizadas no bastan por sí solas para predecir el tipo de suscripción de un cliente, sugiriendo la necesidad de incorporar variables financieras o de uso de dispositivos en futuras iteraciones. El resumen formal del proyecto se encuentra en `reports/informe_final.pdf` y las conclusiones extendidas en `notebooks/05_conclusiones.ipynb`.