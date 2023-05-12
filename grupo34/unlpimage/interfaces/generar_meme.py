import PySimpleGUI as sg
import ventanas

def procesar_eventos(ventana_actual, evento,usuario_imagen):
    #Falta por implementar mas eventos.
    if evento == "-MEME-VOLVER-":
        ventanas.crear_ventana_principal(usuario_imagen)
        ventana_actual.close()