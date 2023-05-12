import PySimpleGUI as sg
from . import ventanas
from . import principal
from . import configuracion
from . import editar_perfil as editar
import etiquetar_imagenes as etiquetar
import generar_collage as collage
import generar_meme as meme
import funciones_menu_principal as f
import os

def menu_principal(usuario):
    ventanas.crear_ventana_principal(usuario["Imagen"])
    tags= set()
    descripcion = ""
    ruta_logs= os.path.join (os.getcwd(), "logs_sistema.csv")
    if not f.existe_archivo(ruta_logs):
        encabezado = ['Alias','operacion','Fecha y hora']
        f.crear_archivo_csv(encabezado,ruta_logs)

    while True:
        ventana_actual, evento, valores = sg.read_all_windows()
        print(f"Ventana actual: {ventana_actual}, Evento: {evento}, valores: {valores}")
        
        if evento == sg.WIN_CLOSED:
            break

        evento_palabra = evento.split("-")[1]
    
        match evento_palabra:
            case "PRINCIPAL":
                principal.procesar_eventos(ventana_actual, evento,usuario)
            case "CONFIGURACION":
                configuracion.procesar_eventos(ventana_actual, evento,valores,usuario)
            case "AYUDA":
                ventanas.crear_ventana_principal(usuario["Imagen"])
                ventana_actual.close()
            case "EDITAR":
                editar.procesar_eventos(ventana_actual,evento,valores, usuario)
            case "COLLAGE":
                collage.procesar_eventos(ventana_actual,evento, usuario["Imagen"])
            case "MEME":
                meme.procesar_eventos(ventana_actual,evento, usuario["Imagen"])
            case "ETIQUETAR":
                tags, descripcion= etiquetar.procesar_eventos(ventana_actual,evento,valores,tags,descripcion,usuario)

    
usuario = {'Alias': 'manu', 'Nombre' : "Manuel", 'Genero' : "Masculino", 'Edad' : '23', "Imagen":"0.png"}

menu_principal(usuario)

