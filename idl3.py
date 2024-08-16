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

# Función para mostrar datos en un DataFrame
def mostrar_datos(tabla: str):
    data = supabase.table(f'hotel.{tabla}').select('*').execute()
    df = pd.DataFrame(data.data)
    st.write(df)

if option == 'Consultar Clientes':
    mostrar_datos('Clientes')

elif option == 'Consultar Habitaciones':
    mostrar_datos('Habitaciones')

elif option == 'Consultar Reservas':
    mostrar_datos('Reservas')

elif option == 'Consultar Ventas':
    mostrar_datos('Ventas')

elif option == 'Consultar Promociones':
    mostrar_datos('Promociones')

elif option == 'Generar Reserva':
    st.subheader("Generar Reserva")
    
    # Datos del cliente
    cliente_id = st.number_input("ID del Cliente", min_value=1, step=1)
    
    # Selección de habitación
    habitaciones = supabase.table('hotel.Habitaciones').select('*').execute()
    df_habitaciones = pd.DataFrame(habitaciones.data)
    selected_habitacion = st.selectbox("Seleccione habitación", df_habitaciones['id_habitacion'])
    
    # Fechas de la reserva
    fecha_inicio = st.date_input("Fecha de inicio")
    fecha_fin = st.date_input("Fecha de fin")
    
    # Mostrar información de la habitación seleccionada
    if selected_habitacion:
        habitacion = df_habitaciones[df_habitaciones['id_habitacion'] == selected_habitacion]
        st.write("Detalles de la habitación seleccionada:")
        st.write(habitacion)
    
    # Seleccionar promoción
    promociones = supabase.table('hotel.Promociones').select('*').execute()
    df_promociones = pd.DataFrame(promociones.data)
    promocion_options = df_promociones['descripcion'].tolist() + ['Ninguna']
    selected_promocion = st.selectbox("Seleccione promoción (opcional)", promocion_options, index=0)
    
    # Número de personas
    numero_personas = st.number_input("Número de personas", min_value=1, step=1)
    
    # Pago anticipado
    pago_anticipado = st.checkbox("Pago anticipado")
    
    # Comentarios
    comentarios = st.text_area("Comentarios (opcional)")
    
    if st.button('Crear Reserva'):
        # Verificar si la fecha de fin es posterior a la fecha de inicio
        if fecha_inicio >= fecha_fin:
            st.error("La fecha de fin debe ser posterior a la fecha de inicio.")
        else:
            # Insertar la reserva
            reserva = supabase.table('hotel.Reservas').insert({
                'id_cliente': cliente_id,
                'id_habitacion': selected_habitacion,
                'fecha_inicio': fecha_inicio,
                'fecha_fin': fecha_fin,
                'estado': 'Confirmada',
                'numero_personas': numero_personas,
                'pago_anticipado': pago_anticipado,
                'comentarios': comentarios
            }).execute()

            # Obtener el ID de la nueva reserva
            if reserva.status_code == 201:
                reserva_id = reserva.data[0]['id_reserva']
                st.success("Reserva creada exitosamente")

                # Aplicar promoción si se seleccionó
                if selected_promocion != "Ninguna":
                    promocion = df_promociones[df_promociones['descripcion'] == selected_promocion]
                    promocion_id = promocion['id_promocion'].values[0]
                    supabase.table('hotel.Promociones_Reservas').insert({
                        'id_promocion': promocion_id,
                        'id_reserva': reserva_id
                    }).execute()
                    st.success("Promoción aplicada exitosamente")

                # Calificación
                calificacion = st.slider("Califica tu estancia (1-5 estrellas)", 1, 5)
                if st.button("Enviar Calificación"):
                    # Aquí podrías guardar la calificación en la base de datos
                    st.success(f"Calificación enviada: {calificacion} estrellas")
            else:
                st.error("Error al crear la reserva")
