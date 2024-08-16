import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configuración de Supabase
URL = "https://cdubgkqitwvtbwtojjrw.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"

# Crear cliente de Supabase
supabase: Client = create_client(URL, KEY)

st.set_page_config(page_title="Sistema de Gestión de Hotel", page_icon="🏨", layout="wide")

st.title("Sistema de Gestión de Hotel")
st.sidebar.title("Navegación")
option = st.sidebar.selectbox(
    '¿Qué operación desea realizar?',
    ('Consultar Clientes', 'Consultar Habitaciones', 'Consultar Reservas', 'Consultar Ventas', 'Consultar Promociones', 
     'Generar Reserva', 'Agregar Cliente', 'Agregar Habitación', 'Agregar Promoción')
)

def display_table(table_name: str):
    try:
        data = supabase.table(table_name).select('*').execute()
        df = pd.DataFrame(data.data)
        st.write(df)
        if st.button(f'Exportar {table_name} a CSV'):
            df.to_csv(f'{table_name}.csv', index=False)
            st.success(f"Archivo CSV exportado exitosamente para {table_name}")
    except Exception as e:
        st.error(f"Ocurrió un error al consultar {table_name}: {e}")

def add_record(table_name: str, fields: dict):
    with st.form(key=f'form_{table_name}'):
        for field, field_type in fields.items():
            if field_type == 'text':
                value = st.text_input(field.capitalize())
            elif field_type == 'number':
                value = st.number_input(field.capitalize(), min_value=0)
            elif field_type == 'select':
                options = fields[field]
                value = st.selectbox(field.capitalize(), options)
            elif field_type == 'date':
                value = st.date_input(field.capitalize())
            if field_type != 'select':
                fields[field] = value
        submit_button = st.form_submit_button(label=f'Guardar {table_name}')
    
    if submit_button:
        try:
            supabase.table(table_name).insert(fields).execute()
            st.success(f"{table_name.capitalize()} agregado exitosamente")
        except Exception as e:
            st.error(f"Ocurrió un error al agregar {table_name}: {e}")

# Consultar datos
if option == 'Consultar Clientes':
    display_table('clientes')

elif option == 'Consultar Habitaciones':
    display_table('habitaciones')

elif option == 'Consultar Reservas':
    display_table('reservas')

elif option == 'Consultar Ventas':
    display_table('ventas')

elif option == 'Consultar Promociones':
    display_table('promociones')

# Generar Reserva
elif option == 'Generar Reserva':
    st.subheader("Generar Reserva")
    cliente_id = st.number_input("ID del Cliente", min_value=1)
    habitaciones = supabase.table('habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    selected_habitacion = st.selectbox("Seleccione una habitación", df_habitaciones['id_habitacion'])
    fecha_inicio = st.date_input("Fecha de Inicio")
    fecha_fin = st.date_input("Fecha de Fin")
    
    if st.button('Generar Reserva'):
        try:
            reserva = supabase.table('reservas').insert({
                'id_cliente': cliente_id,
                'id_habitacion': selected_habitacion,
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'estado': 'Confirmada'
            }).execute()
            st.success(f"Reserva generada con ID: {reserva.data[0]['id_reserva']}")
        except Exception as e:
            st.error(f"Ocurrió un error al generar la reserva: {e}")

# Agregar Cliente
elif option == 'Agregar Cliente':
    fields = {
        'nombre': 'text',
        'apellido': 'text',
        'email': 'text',
        'telefono': 'text'
    }
    add_record('clientes', fields)

# Agregar Habitación
elif option == 'Agregar Habitación':
    fields = {
        'tipo': 'select',  # Options will be filled below
        'precio_por_noche': 'number',
        'estado': 'select'  # Options will be filled below
    }
    add_record('habitaciones', fields)

# Agregar Promoción
elif option == 'Agregar Promoción':
    fields = {
        'descripcion': 'text',
        'descuento': 'number',
        'fecha_inicio': 'date',
        'fecha_fin': 'date'
    }
    add_record('promociones', fields)


