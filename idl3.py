import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Configuración de Supabase
url = "https://cdubgkqitwvtbwtojjrw.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"

# Crear cliente de Supabase
supabase: Client = create_client(url, key)

# Página principal
st.title("App de Hotel")

# Sección de clientes
st.header("Clientes")

# Funciones para interactuar con las tablas
def get_clientes():
    response = supabase.from_("clientes").select("*")
    return response.execute()

def get_habitaciones():
    response = supabase.from_("habitaciones").select("*")
    return response.execute()

def get_reservas():
    response = supabase.from_("reservas").select("*")
    return response.execute()

def get_ventas():
    response = supabase.from_("ventas").select("*")
    return response.execute()

def get_promociones():
    response = supabase.from_("promociones").select("*")
    return response.execute()

def get_promociones_reservas():
    response = supabase.from_("promociones_reservas").select("*")
    return response.execute()

# Estado de la aplicación
if 'datos' not in st.session_state:
    st.session_state.datos = {}

# Botón para agregar datos
if st.button("Agregar"):
    clientes = get_clientes()
    df_clientes = pd.DataFrame(clientes.data)
    if st.button("Guardar"):
        try:
            supabase.from_("clientes").insert({"nombre": "Nombre", "apellido": "Apellido", "email": "email@example.com", "telefono": "1234567890"}).execute()
            st.session_state.datos["Clientes"] = pd.DataFrame({'Nombre': ["Nombre"], 'Apellido': ["Apellido"], 'Email': ["email@example.com"], 'Teléfono': ["1234567890"]})
            st.success("Datos agregados con éxito")
        except Exception as e:
            st.error("Error al agregar datos: " + str(e))

# Botón para ver la tabla actualizada
if st.button("Ver tabla"):
    if "Clientes" in st.session_state.datos:
        st.write(st.session_state.datos["Clientes"])
    else:
        st.write("No hay datos para mostrar")

# Botón para borrar datos
if st.button("Borrar"):
    if "Clientes" in st.session_state.datos:
        st.session_state.datos.pop("Clientes")
        st.success("Datos borrados con éxito")
    else:
        st.write("No hay datos para borrar")