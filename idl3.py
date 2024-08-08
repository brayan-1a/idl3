import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configuración de Supabase
URL = "https://cdubgkqitwvtbwtojjrw.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"

# Crear cliente de Supabase
supabase: Client = create_client(URL, KEY)

st.title("Sistema de Gestión de Hotel")

# Selección de operación
option = st.selectbox(
    '¿Qué operación desea realizar?',
    ('Consultar Clientes', 'Consultar Habitaciones', 'Consultar Reservas', 'Consultar Ventas', 'Consultar Promociones', 'Generar Reserva')
)

if option == 'Consultar Clientes':
    clientes = supabase.table('Clientes').select('*').execute()
    df_clientes = pd.DataFrame(clientes.data)
    st.write(df_clientes)

elif option == 'Consultar Habitaciones':
    habitaciones = supabase.table('Habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    st.write(df_habitaciones)

elif option == 'Consultar Reservas':
    reservas = supabase.table('Reservas').select('*').execute()
    df_reservas = pd.DataFrame(reservas.data)
    st.write(df_reservas)

elif option == 'Consultar Ventas':
    ventas = supabase.table('Ventas').select('*').execute()
    df_ventas = pd.DataFrame(ventas.data)
    st.write(df_ventas)

elif option == 'Consultar Promociones':
    promociones = supabase.table('Promociones').select('*').execute()
    df_promociones = pd.DataFrame(promociones.data)
    st.write(df_promociones)

elif option == 'Generar Reserva':
    # Datos del cliente
    cliente_id = st.number_input("ID del Cliente", min_value=1)
    
    # Datos de la habitación
    habitaciones = supabase.table('Habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    selected_habitacion = st.selectbox("Seleccione una habitación", df_habitaciones['id_habitacion'])
    
    # Fechas de la reserva
    fecha_inicio = st.date_input("Fecha de Inicio")
    fecha_fin = st.date_input("Fecha de Fin")
    
    # Generar reserva
    if st.button('Generar Reserva'):
        reserva = supabase.table('Reservas').insert({
            'id_cliente': cliente_id,
            'id_habitacion': selected_habitacion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'estado': 'Confirmada'
        }).execute()
        
        st.success(f"Reserva generada con ID: {reserva.data[0]['id_reserva']}")
