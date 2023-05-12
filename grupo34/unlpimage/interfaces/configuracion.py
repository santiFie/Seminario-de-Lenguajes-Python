import PySimpleGUI as sg
import ventanas
import funciones_menu_principal as f

def procesar_eventos(ventana_actual, evento,valores,usuario):
    if evento == "-CONFIGURACION-VOLVER-":
        ventanas.crear_ventana_principal(usuario["Imagen"])
        ventana_actual.close()
    elif evento == "-CONFIGURACION-GUARDAR-":
        f.actualizar_informacion_archivo(valores[0], valores[1], valores[2])
        operacion = "cambio en la configuración del sistema"
        f.registro_carga_logs(usuario["Alias"],operacion)
        sg.popup("Los Datos se actualizaron con exito")
    