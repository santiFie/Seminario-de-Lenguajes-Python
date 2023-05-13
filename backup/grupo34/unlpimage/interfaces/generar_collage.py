import PySimpleGUI as sg
import os
import sys
sys.path.append(os.getcwd())

import unlpimage.archivos_auxiliares.ventanas as ventanas

def procesar_eventos(ventana_actual, evento,usuario_imagen):
    #Falta por implementar mas eventos.
    if evento == "-COLLAGE-VOLVER-":
        ventanas.crear_ventana_principal(usuario_imagen)
        ventana_actual.close()