import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configuración de Supabase
URL = "https://clmdobighgagqdqwfclt.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNsbWRvYmlnaGdhZ3FkcXdmY2x0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMzMDYsImV4cCI6MjAzODA0OTMwNn0.7pncUo2SvBwi1Jnxl863e9-omO8fGulmZC3_zhUVFTM"
supabase: Client = create_client(URL, KEY)

st.title("Sistema de Gestión de Hotel")

# Selección de operación
option = st.sidebar.selectbox(
    '¿Qué operación desea realizar?',
    ('Consultar Clientes', 'Consultar Habitaciones', 'Consultar Reservas', 'Consultar Ventas', 'Consultar Promociones', 'Generar Reserva')
)

if option == 'Consultar Clientes':
    clientes = supabase.table('hotel.Clientes').select('*').execute()
    df_clientes = pd.DataFrame(clientes.data)
    st.write(df_clientes)

elif option == 'Consultar Habitaciones':
    habitaciones = supabase.table('hotel.Habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    st.write(df_habitaciones)

elif option == 'Consultar Reservas':
    reservas = supabase.table('hotel.Reservas').select('*').execute()
    df_reservas = pd.DataFrame(reservas.data)
    st.write(df_reservas)

elif option == 'Consultar Ventas':
    ventas = supabase.table('hotel.Ventas').select('*').execute()
    df_ventas = pd.DataFrame(ventas.data)
    st.write(df_ventas)

elif option == 'Consultar Promociones':
    promociones = supabase.table('hotel.Promociones').select('*').execute()
    df_promociones = pd.DataFrame(promociones.data)
    st.write(df_promociones)

elif option == 'Generar Reserva':
    st.subheader("Generar Reserva")
    
    # Datos del cliente
    cliente_id = st.number_input("ID del Cliente", min_value=1)
    
    # Selección de habitación
    habitaciones = supabase.table('hotel.Habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    selected_habitacion = st.selectbox("Seleccione habitación", df_habitaciones['id_habitacion'])
    
    # Fechas de la reserva
    fecha_inicio = st.date_input("Fecha de inicio")
    fecha_fin = st.date_input("Fecha de fin")
    
    if st.button('Crear Reserva'):
        reserva = supabase.table('hotel.Reservas').insert({
            'id_cliente': cliente_id,
            'id_habitacion': selected_habitacion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'estado': 'Confirmada'
        }).execute()
        if reserva.status_code == 201:
            st.success("Reserva creada exitosamente")
        else:
            st.error("Error al crear la reserva")

