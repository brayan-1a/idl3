import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configuración de Supabase
URL = "https://cdubgkqitwvtbwtojjrw.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"

# Crear cliente de Supabase
supabase: Client = create_client(URL, KEY)

# Configuración de la página
st.set_page_config(page_title="Sistema de Gestión de Hotel", page_icon="🏨", layout="wide")

# Fondo personalizado usando CSS con imagen
st.markdown("""
    <style>
        .main {
            background-image: url('assets/fondo.jpg');
            background-size: cover;
            background-position: center;
            padding: 2rem;
        }
        .header {
            background-color: rgba(76, 175, 80, 0.8); /* Verde con transparencia */
            color: white;
            padding: 1rem;
            text-align: center;
            font-size: 2rem;
            border-radius: 5px;
        }
        .stButton>button {
            background-color: #4CAF50; /* Botones en verde */
            color: white;
            border: None;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #45a049; /* Color más oscuro al pasar el cursor */
        }
        .form-container {
            background-color: rgba(255, 255, 255, 0.8); /* Fondo blanco con transparencia */
            padding: 1rem;
            border-radius: 5px;
            margin: 1rem 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">Sistema de Gestión de Hotel</div>', unsafe_allow_html=True)

# Selección de operación
option = st.sidebar.selectbox(
    '¿Qué operación desea realizar?',
    ('Consultar Clientes', 'Consultar Habitaciones', 'Consultar Reservas', 'Consultar Ventas', 'Consultar Promociones', 
     'Generar Reserva', 'Agregar Cliente', 'Agregar Habitación', 'Agregar Promoción')
)

# Consultar datos
if option == 'Consultar Clientes':
    clientes = supabase.table('clientes').select('*').execute()
    df_clientes = pd.DataFrame(clientes.data)
    st.write(df_clientes)

    if st.button('Exportar Clientes a CSV'):
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

elif option == 'Consultar Habitaciones':
    habitaciones = supabase.table('habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    st.write(df_habitaciones)

elif option == 'Consultar Reservas':
    reservas = supabase.table('reservas').select('*').execute()
    df_reservas = pd.DataFrame(reservas.data)
    st.write(df_reservas)

elif option == 'Consultar Ventas':
    ventas = supabase.table('ventas').select('*').execute()
    df_ventas = pd.DataFrame(ventas.data)
    st.write(df_ventas)

elif option == 'Consultar Promociones':
    promociones = supabase.table('promociones').select('*').execute()
    df_promociones = pd.DataFrame(promociones.data)
    st.write(df_promociones)

# Generar Reserva
elif option == 'Generar Reserva':
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    cliente_id = st.number_input("ID del Cliente", min_value=1)
    habitaciones = supabase.table('habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    selected_habitacion = st.selectbox("Seleccione una habitación", df_habitaciones['id_habitacion'])
    fecha_inicio = st.date_input("Fecha de Inicio")
    fecha_fin = st.date_input("Fecha de Fin")
    
    if st.button('Generar Reserva'):
        reserva = supabase.table('reservas').insert({
            'id_cliente': cliente_id,
            'id_habitacion': selected_habitacion,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'estado': 'Confirmada'
        }).execute()
        st.success(f"Reserva generada con ID: {reserva.data[0]['id_reserva']}")
    st.markdown('</div>', unsafe_allow_html=True)

# Agregar Cliente
elif option == 'Agregar Cliente':
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    with st.form(key='form_cliente'):
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        email = st.text_input("Email")
        telefono = st.text_input("Teléfono")
        submit_button = st.form_submit_button(label='Guardar Cliente')

    if submit_button:
        supabase.table('clientes').insert({
            'nombre': nombre,
            'apellido': apellido,
            'email': email,
            'telefono': telefono
        }).execute()
        st.success("Cliente agregado exitosamente")
    st.markdown('</div>', unsafe_allow_html=True)

# Agregar Habitación
elif option == 'Agregar Habitación':
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    with st.form(key='form_habitacion'):
        tipo = st.selectbox("Tipo de Habitación", ["Simple", "Doble", "Suite"])
        precio_por_noche = st.number_input("Precio por Noche", min_value=0.0, format="%.2f")
        estado = st.selectbox("Estado", ["Disponible", "Ocupada", "En mantenimiento"])
        submit_button = st.form_submit_button(label='Guardar Habitación')

    if submit_button:
        supabase.table('habitaciones').insert({
            'tipo': tipo,
            'precio_por_noche': precio_por_noche,
            'estado': estado
        }).execute()
        st.success("Habitación agregada exitosamente")
    st.markdown('</div>', unsafe_allow_html=True)

# Agregar Promoción
elif option == 'Agregar Promoción':
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    with st.form(key='form_promocion'):
        descripcion = st.text_input("Descripción de la Promoción")
        descuento = st.number_input("Descuento (%)", min_value=0, max_value=100)
        fecha_inicio = st.date_input("Fecha de Inicio")
        fecha_fin = st.date_input("Fecha de Fin")
        submit_button = st.form_submit_button(label='Guardar Promoción')

    if submit_button:
        supabase.table('promociones').insert({
            'descripcion': descripcion,
            'descuento': descuento,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin
        }).execute()
        st.success("Promoción agregada exitosamente")
    st.markdown('</div>', unsafe_allow_html=True)





