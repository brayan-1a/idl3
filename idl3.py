import streamlit as st
from supabase import create_client, Client
import pandas as pd

# Configuración de Supabase
URL = "https://cdubgkqitwvtbwtojjrw.supabase.co"
KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNkdWJna3FpdHd2dGJ3dG9qanJ3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNDU5MDMsImV4cCI6MjAzODcyMTkwM30.2tir9-ogeojL_ueU3ogD1MD9p76GJ5OoVyKVCXKpphM"

# Crear cliente de Supabase
supabase: Client = create_client(URL, KEY)

# Función para validar datos
def validar_datos(data):
    if not data['nombre']:
        return False
    if not data['apellido']:
        return False
    if not data['email']:
        return False
    if not data['telefono']:
        return False
    return True

# Función para agregar cliente
def agregar_cliente(data):
    if validar_datos(data):
        supabase.table('clientes').insert({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).execute()
        st.success("Cliente agregado exitosamente")
    else:
        st.error("Error al agregar cliente")

# Función para agregar habitación
def agregar_habitacion(data):
    if validar_datos(data):
        supabase.table('habitaciones').insert({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).execute()
        st.success("Habitación agregada exitosamente")
    else:
        st.error("Error al agregar habitación")

# Función para agregar promoción
def agregar_promocion(data):
    if validar_datos(data):
        supabase.table('promociones').insert({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).execute()
        st.success("Promoción agregada exitosamente")
    else:
        st.error("Error al agregar promoción")

# Función para consultar datos
def consultar_datos(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').delete().eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación eliminada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').delete().eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva eliminada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').delete().eq('id_venta', data['id_venta']).execute()
        st.success("Venta eliminada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').delete().eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción eliminada exitosamente")

# Función para actualizar datos
def actualizar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').update({
            'nombre': data['nombre'],
            'apellido': data['apellido'],
            'email': data['email'],
            'telefono': data['telefono']
        }).eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente actualizado exitosamente")
    elif tipo == 'habitaciones':
        supabase.table('habitaciones').update({
            'tipo': data['tipo'],
            'precio_por_noche': data['precio_por_noche'],
            'estado': data['estado']
        }).eq('id_habitacion', data['id_habitacion']).execute()
        st.success("Habitación actualizada exitosamente")
    elif tipo == 'reservas':
        supabase.table('reservas').update({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).eq('id_reserva', data['id_reserva']).execute()
        st.success("Reserva actualizada exitosamente")
    elif tipo == 'ventas':
        supabase.table('ventas').update({
            'id_venta': data['id_venta'],
            'monto': data['monto'],
            'fecha': data['fecha']
        }).eq('id_venta', data['id_venta']).execute()
        st.success("Venta actualizada exitosamente")
    elif tipo == 'promociones':
        supabase.table('promociones').update({
            'descripcion': data['descripcion'],
            'descuento': data['descuento'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin']
        }).eq('id_promocion', data['id_promocion']).execute()
        st.success("Promoción actualizada exitosamente")

# Función para generar reserva
def generar_reserva(data):
    if validar_datos(data):
        supabase.table('reservas').insert({
            'id_cliente': data['id_cliente'],
            'id_habitacion': data['id_habitacion'],
            'fecha_inicio': data['fecha_inicio'],
            'fecha_fin': data['fecha_fin'],
            'estado': 'Confirmada'
        }).execute()
        st.success("Reserva generada exitosamente")
    else:
        st.error("Error al generar reserva")

# Función para exportar datos a CSV
def exportar_datos_a_csv(tipo):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        df_clientes.to_csv('clientes.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        df_habitaciones.to_csv('habitaciones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        df_reservas.to_csv('reservas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        df_ventas.to_csv('ventas.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        df_promociones.to_csv('promociones.csv', index=False)
        st.success("Archivo CSV exportado exitosamente")

# Función para buscar datos
def buscar_datos(tipo, data):
    if tipo == 'clientes':
        clientes = supabase.table('clientes').select('*').execute()
        df_clientes = pd.DataFrame(clientes.data)
        st.write(df_clientes)
    elif tipo == 'habitaciones':
        habitaciones = supabase.table('habitaciones').select('*').execute()
        df_habitaciones = pd.DataFrame(habitaciones.data)
        st.write(df_habitaciones)
    elif tipo == 'reservas':
        reservas = supabase.table('reservas').select('*').execute()
        df_reservas = pd.DataFrame(reservas.data)
        st.write(df_reservas)
    elif tipo == 'ventas':
        ventas = supabase.table('ventas').select('*').execute()
        df_ventas = pd.DataFrame(ventas.data)
        st.write(df_ventas)
    elif tipo == 'promociones':
        promociones = supabase.table('promociones').select('*').execute()
        df_promociones = pd.DataFrame(promociones.data)
        st.write(df_promociones)

# Función para eliminar datos
def eliminar_datos(tipo, data):
    if tipo == 'clientes':
        supabase.table('clientes').delete().eq('id_cliente', data['id_cliente']).execute()
        st.success("Cliente eliminado exitosamente")
   
