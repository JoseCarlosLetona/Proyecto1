import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Configuración de la página de Streamlit
st.set_page_config(page_title="Super Market Data", layout="wide")


# Obtener la URI de MongoDB desde secrets.toml
mongo_uri = st.secrets["mongo"]["uri"]
db_name = st.secrets["mongo"]["db"]

# Conectar a la base de datos
client = MongoClient(mongo_uri)
db = client[db_name]


# titulo
st.title("Super Market Data")
# Subtitulo
st.subheader("Análisis de datos de un supermercado")

annex1_df = pd.DataFrame(list(db['Wholesale Price'].find()))
annex2_df = pd.DataFrame(list(db['Category'].find()))
annex3_df = pd.DataFrame(list(db['Sales'].find()))
annex4_df = pd.DataFrame(list(db['Loss Rate (%)'].find()))


annex3_df = annex3_df.drop(columns=['_id'])
annex2_df = annex2_df.drop(columns=['_id'])
# merge annex1 and annex2 for Item Name
merged_df = pd.merge(annex3_df, annex2_df, on='Item Code', how='left')

# mostrar los datos de merged_df
st.subheader("Datos de ventas")
st.dataframe(merged_df)