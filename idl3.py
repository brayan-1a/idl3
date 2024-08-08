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
clientes = get_clientes()
df_clientes = pd.DataFrame(clientes.data)

# Lista desplegable para seleccionar la tabla
tabla_seleccionada = st.selectbox("Seleccione una tabla", ["Clientes", "Habitaciones", "Reservas", "Ventas", "Promociones", "Promociones-reservas"])

# Estado de la aplicación
if 'datos' not in st.session_state:
    st.session_state.datos = {}

# Botón para agregar datos
if st.button("Agregar"):
    if tabla_seleccionada == "Clientes":
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        email = st.text_input("Email")
        telefono = st.text_input("Teléfono")
        if st.button("Guardar"):
            try:
                supabase.from_("clientes").insert({"nombre": nombre, "apellido": apellido, "email": email, "telefono": telefono}).execute()
                st.session_state.datos[tabla_seleccionada] = pd.DataFrame({'Nombre': [nombre], 'Apellido': [apellido], 'Email': [email], 'Teléfono': [telefono]})
                st.success("Datos agregados con éxito")
            except Exception as e:
                st.error("Error al agregar datos: " + str(e))
    elif tabla_seleccionada == "Habitaciones":
        tipo = st.selectbox("Tipo", ["Simple", "Doble", "Suite"])
        precio_por_noche = st.number_input("Precio por noche")
        estado = st.selectbox("Estado", ["Disponible", "Ocupada", "En mantenimiento"])
        if st.button("Guardar"):
            try:
                supabase.from_("habitaciones").insert({"tipo": tipo, "precio_por_noche": precio_por_noche, "estado": estado}).execute()
                st.session_state.datos[tabla_seleccionada] = pd.DataFrame({'Tipo': [tipo], 'Precio por noche': [precio_por_noche], 'Estado': [estado]})
                st.success("Datos agregados con éxito")
            except Exception as e:
                st.error("Error al agregar datos: " + str(e))
    # Agregar más casos para cada tabla

# Botón para ver la tabla actualizada
if st.button("Ver tabla"):
    if tabla_seleccionada in st.session_state.datos:
        st.write(st.session_state.datos[tabla_seleccionada])
    else:
        st.write("No hay datos para mostrar")

# Botón para borrar datos
if st.button("Borrar"):
    if tabla_seleccionada in st.session_state.datos:
        st.session_state.datos.pop(tabla_seleccionada)
        st.success("Datos borrados con éxito")
    else:
        st.write("No hay datos para borrar")

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