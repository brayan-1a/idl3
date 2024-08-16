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

# Menú de navegación
tabs = st.tabs(['Consultar Datos', 'Agregar Datos'])

# Consultar Datos
with tabs[0]:
    st.header("Consultar Datos")
    option = st.selectbox(
        'Seleccione la tabla para consultar',
        ('Clientes', 'Habitaciones', 'Reservas', 'Ventas', 'Promociones')
    )

    def display_table(table_name: str):
        try:
            data = supabase.table(table_name.lower()).select('*').execute()
            df = pd.DataFrame(data.data)
            st.write(df)
            if st.button(f'Exportar {table_name} a CSV'):
                df.to_csv(f'{table_name.lower()}.csv', index=False)
                st.success(f"Archivo CSV exportado exitosamente para {table_name}")
        except Exception as e:
            st.error(f"Ocurrió un error al consultar {table_name}: {e}")

    display_table(option)

# Agregar Datos
with tabs[1]:
    st.header("Agregar Datos")
    
    add_option = st.selectbox(
        'Seleccione la tabla para agregar datos',
        ('Clientes', 'Habitaciones', 'Promociones')
    )

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
                fields[field] = value
            submit_button = st.form_submit_button(label=f'Guardar {table_name}')
        
        if submit_button:
            try:
                supabase.table(table_name.lower()).insert(fields).execute()
                st.success(f"{table_name} agregado exitosamente")
            except Exception as e:
                st.error(f"Ocurrió un error al agregar {table_name}: {e}")

    if add_option == 'Clientes':
        fields = {
            'nombre': 'text',
            'apellido': 'text',
            'email': 'text',
            'telefono': 'text'
        }
        add_record('clientes', fields)

    elif add_option == 'Habitaciones':
        fields = {
            'tipo': 'select',  # Options will be filled below
            'precio_por_noche': 'number',
            'estado': 'select'  # Options will be filled below
        }
        add_record('habitaciones', fields)

    elif add_option == 'Promociones':
        fields = {
            'descripcion': 'text',
            'descuento': 'number',
            'fecha_inicio': 'date',
            'fecha_fin': 'date'
        }
        add_record('promociones', fields)



