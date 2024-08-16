import streamlit as st
from supabase import create_client, Client
import pandas as pd
import datetime

# Configuración de Supabase
URL = "https://cdubgkqitwvtbwtojjrw.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"
supabase: Client = create_client(URL, KEY)

st.set_page_config(page_title="Sistema de Gestión de Hotel", page_icon="🏨", layout="wide")

# Fondo personalizado usando CSS con color de fondo y recuadros
st.markdown("""
    <style>
        .main {
            background-color: #F7F7F7; /* Color de fondo claro */
            padding: 2rem;
        }
        .header {
            background-color: #004d40; /* Verde oscuro para el encabezado */
            color: white;
            padding: 1rem;
            text-align: center;
            font-size: 2rem;
            border-radius: 5px;
        }
        .recuadro {
            background-color: #F5F5DC; /* Beige para los recuadros de contenido y formularios */
            border: 1px solid #E0E0E0; /* Gris claro para los bordes */
            padding: 2rem;
            border-radius: 5px;
            margin-top: 1rem;
        }
        .stButton>button {
            background-color: #004d40; /* Verde oscuro para los botones */
            color: white;
            border: None;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #004d40; /* Verde oscuro al pasar el ratón */
        }
        .stTextInput>input,
        .stSelectbox>div>div>div,
        .stDateInput>div>div>div,
        .stMarkdown {
            color: #333333; /* Color de texto */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">Sistema de Gestión de Hotel</div>', unsafe_allow_html=True)

# Menú de navegación
tabs = st.tabs(['Consultar Datos', 'Agregar Datos', 'Generar Reportes'])

# Consultar Datos
with tabs[0]:
    st.header("Consultar Datos")
    with st.container():
        st.markdown('<div class="recuadro">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)

# Agregar Datos
with tabs[1]:
    st.header("Agregar Datos")
    with st.container():
        st.markdown('<div class="recuadro">', unsafe_allow_html=True)
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
                        value = st.number_input(field.capitalize(), min_value=0.0, value=fields.get('default_value', 0.0))
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
            fields['precio_por_noche'] = {'field_type': 'number', 'default_value': 50.0}  # Default value of 50.0
            add_record('habitaciones', fields)

        elif add_option == 'Promociones':
            fields = {
                'descripcion': 'text',
                'descuento': 'number',
                'fecha_inicio': 'date',
                'fecha_fin': 'date'
            }
            fields['descuento'] = {'field_type': 'number', 'default_value': 10.0}  # Default value of 10.0
            add_record('promociones', fields)
        st.markdown('</div>', unsafe_allow_html=True)

# Generar Reportes
with tabs[2]:
    st.header("Generar Reportes")
    with st.container():
        st.markdown('<div class="recuadro">', unsafe_allow_html=True)
        report_option = st.selectbox(
            'Seleccione el tipo de reporte',
            ('Reporte de Clientes', 'Reporte de Reservas', 'Reporte de Ventas', 'Reporte de Promociones')
        )

        def generate_report(report_type: str):
            try:
                if report_type == 'Reporte de Clientes':
                    st.subheader("Clientes Registrados")
                    start_date = st.date_input("Fecha de Inicio", datetime.date(2023, 1, 1))
                    end_date = st.date_input("Fecha de Fin", datetime.date.today())
                    query = supabase.table('clientes').select('*').gte('fecha_registro', start_date).lte('fecha_registro', end_date).execute()
                    df = pd.DataFrame(query.data)
                    st.write(df)

                elif report_type == 'Reporte de Reservas':
                    st.subheader("Reservas en el Rango de Fechas")
                    start_date = st.date_input("Fecha de Inicio", datetime.date(2023, 1, 1))
                    end_date = st.date_input("Fecha de Fin", datetime.date.today())
                    query = supabase.table('reservas').select('*').gte('fecha_inicio', start_date).lte('fecha_fin', end_date).execute()
                    df = pd.DataFrame(query.data)
                    st.write(df)

                elif report_type == 'Reporte de Ventas':
                    st.subheader("Ventas Totales")
                    start_date = st.date_input("Fecha de Inicio", datetime.date(2023, 1, 1))
                    end_date = st.date_input("Fecha de Fin", datetime.date.today())
                    query = supabase.table('ventas').select('*').gte('fecha', start_date).lte('fecha', end_date).execute()
                    df = pd.DataFrame(query.data)
                    st.write(df)

                elif report_type == 'Reporte de Promociones':
                    st.subheader("Promociones Activas")
                    query = supabase.table('promociones').select('*').lte('fecha_fin', datetime.date.today()).execute()
                    df = pd.DataFrame(query.data)
                    st.write(df)
                    
            except Exception as e:
                st.error(f"Ocurrió un error al generar el reporte: {e}")

        generate_report(report_option)
        st.markdown('</div>', unsafe_allow_html=True)
