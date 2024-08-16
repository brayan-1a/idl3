import streamlit as st
from supabase import create_client, Client
import os
# Cargar variables de entorno
load_dotenv()

# Configurar conexión a Supabase
url: str = os.getenv("https://cdubgkqitwvtbwtojjrw.supabase.co")
key: str = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM")
supabase: Client = create_client(url, key)

# Función para obtener datos de una tabla
def get_data(table_name: str):
    response = supabase.table(table_name).select("*").execute()
    return response.data

# Interfaz de usuario
st.title("Gestión del Hotel")

# Mostrar datos de clientes
st.header("Clientes")
clientes = get_data("Clientes")
st.write(clientes)

# Agregar nuevo cliente
st.subheader("Agregar Nuevo Cliente")
with st.form("add_client"):
    nombre = st.text_input("Nombre")
    apellido = st.text_input("Apellido")
    email = st.text_input("Email")
    telefono = st.text_input("Teléfono")
    direccion = st.text_input("Dirección")
    if st.form_submit_button("Agregar Cliente"):
        supabase.table("Clientes").insert({
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "direccion": direccion
        }).execute()
        st.success("Cliente agregado exitosamente!")

# Calificación
st.header("Calificación de Habitaciones")
calificacion = st.slider("Califica tu estancia (1-5 estrellas)", 1, 5)
if st.button("Enviar Calificación"):
    # Aquí podrías guardar la calificación en la base de datos
    st.success(f"Calificación enviada: {calificacion} estrellas")
