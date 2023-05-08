import PySimpleGUI as sg
import funciones_agregar_perfil as funciones_agregar_perfil

def crear_ventana_rama():

    layout = [  [ sg.Button( "Agregar perfil", key = "perfil" ) ]   ]

    window = sg.Window ( "Inicio" , layout , margins= (300,300) )

    while True:

        eventos,valores = window.read()

        if eventos == sg.WIN_CLOSED :

            break

        if  eventos == "perfil" :

            window.close()

            funciones_agregar_perfil.crear_ventana_agregar_perfil()


crear_ventana_rama()