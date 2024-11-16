import streamlit as st
import gspread
from google.oauth2 import service_account
import pandas as pd

def get_gsheet_data():
    try:
        # Cargar las credenciales desde los secretos de Streamlit
        creds_dict = st.secrets["gcp_service_account"]
        
        # Autenticar usando google.oauth2.service_account
        credentials = service_account.Credentials.from_service_account_info(creds_dict)
        
        # Conectar con gspread usando las credenciales
        client = gspread.authorize(credentials)
        
        # Abrir la hoja de cálculo y obtener los datos
        sheet = client.open("Facturas Clientes").worksheet("Hoja 1")
        data = sheet.get_all_records()
        
        # Retornar los datos como un DataFrame de pandas
        return pd.DataFrame(data)
    
    except Exception as e:
        # En caso de error, mostrar el mensaje y retornar None
        st.error(f"Error al conectar con Google Sheets: {e}")
        return None

# Título de la aplicación
st.title("Demo TrackerCyl")

# Intentar cargar los datos
df = get_gsheet_data()

# Verificar si la conexión fue exitosa
if df is not None:
    st.success("Conexión exitosa con Google Sheets")
else:
    st.error("No se pudo establecer conexión con Google Sheets")