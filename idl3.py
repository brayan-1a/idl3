import streamlit as st
import pandas as pd
from supabase import create_client, Client

# Configuración de Supabase
url = "https://cdubgkqitwvtbwtojjrw.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"

# Crear cliente de Supabase
supabase: Client = create_client(url, key)

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

# Página principal
st.title("App de Hotel")

# Sección de clientes
st.header("Clientes")
clientes = get_clientes()
df_clientes = pd.DataFrame(clientes.data)
st.write(df_clientes)

# Botón para agregar cliente
if st.button("Agregar cliente"):
    st.write("Agregar cliente")

# Sección de habitaciones
st.header("Habitaciones")
habitaciones = get_habitaciones()
df_habitaciones = pd.DataFrame(habitaciones.data)
st.write(df_habitaciones)

# Botón para agregar habitación
if st.button("Agregar habitación"):
    st.write("Agregar habitación")

# Sección de reservas
st.header("Reservas")
reservas = get_reservas()
df_reservas = pd.DataFrame(reservas.data)
st.write(df_reservas)

# Botón para agregar reserva
if st.button("Agregar reserva"):
    st.write("Agregar reserva")

# Sección de ventas
st.header("Ventas")
ventas = get_ventas()
df_ventas = pd.DataFrame(ventas.data)
st.write(df_ventas)

# Botón para agregar venta
if st.button("Agregar venta"):
    st.write("Agregar venta")

# Sección de promociones
st.header("Promociones")
promociones = get_promociones()
df_promociones = pd.DataFrame(promociones.data)
st.write(df_promociones)

# Botón para agregar promoción
if st.button("Agregar promoción"):
    st.write("Agregar promoción")

# Sección de promociones-reservas
st.header("Promociones-reservas")
promociones_reservas = get_promociones_reservas()
df_promociones_reservas = pd.DataFrame(promociones_reservas.data)
st.write(df_promociones_reservas)

# Botón para agregar promoción-reserva
if st.button("Agregar promoción-reserva"):
    st.write("Agregar promoción-reserva")



