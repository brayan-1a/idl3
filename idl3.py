import streamlit as st
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import pandas as pd

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

# Función para insertar datos en una tabla
def insert_data(table_name: str, data: dict):
    response = supabase.table(table_name).insert(data).execute()
    return response.data

# Función para actualizar datos en una tabla
def update_data(table_name: str, id: int, data: dict):
    response = supabase.table(table_name).update(data).eq('id', id).execute()
    return response.data

# Función para eliminar datos en una tabla
def delete_data(table_name: str, id: int):
    response = supabase.table(table_name).delete().eq('id', id).execute()
    return response.data

# Interfaz de usuario
st.title("Gestión del Hotel")

# Mostrar datos de clientes
st.header("Clientes")
clientes = pd.DataFrame(get_data("Clientes"))
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
        insert_data("Clientes", {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "direccion": direccion
        })
        st.success("Cliente agregado exitosamente!")

# Editar cliente existente
st.subheader("Editar Cliente")
cliente_id = st.number_input("ID del Cliente", min_value=1)
cliente_data = get_data("Clientes")
if cliente_id:
    cliente = next((item for item in cliente_data if item["id_cliente"] == cliente_id), None)
    if cliente:
        with st.form("edit_client"):
            nombre = st.text_input("Nombre", value=cliente['nombre'])
            apellido = st.text_input("Apellido", value=cliente['apellido'])
            email = st.text_input("Email", value=cliente['email'])
            telefono = st.text_input("Teléfono", value=cliente['telefono'])
            direccion = st.text_input("Dirección", value=cliente['direccion'])
            if st.form_submit_button("Actualizar Cliente"):
                update_data("Clientes", cliente_id, {
                    "nombre": nombre,
                    "apellido": apellido,
                    "email": email,
                    "telefono": telefono,
                    "direccion": direccion
                })
                st.success("Cliente actualizado exitosamente!")

# Eliminar cliente
st.subheader("Eliminar Cliente")
delete_id = st.number_input("ID del Cliente para Eliminar", min_value=1)
if st.button("Eliminar Cliente"):
    delete_data("Clientes", delete_id)
    st.success("Cliente eliminado exitosamente!")

# Funcionalidad de calificación
st.header("Calificación de Habitaciones")
calificacion = st.slider("Califica tu estancia (1-5 estrellas)", 1, 5)
if st.button("Enviar Calificación"):
    # Aquí podrías guardar la calificación en la base de datos
    st.success(f"Calificación enviada: {calificacion} estrellas")

# Mostrar y gestionar otras tablas (habitaciones, reservas, ventas, promociones)
# Aquí puedes repetir los bloques de código de clientes para las demás tablas.
# Agregar funcionalidades similares para Habitaciones, Reservas, Ventas, Promociones.

