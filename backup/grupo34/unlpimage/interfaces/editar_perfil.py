import PySimpleGUI as sg
import sys
import os
import json
import unlpimage.archivos_auxiliares.funciones_menu_principal as f
import sys
import unlpimage.archivos_auxiliares.ventanas as  ventanas
from unlpimage.archivos_auxiliares.ventanas import crear_ventana_editar_perfil

from unlpimage.archivos_auxiliares.funciones_agregar_perfil import crear_ventana_archivos
from unlpimage.archivos_auxiliares.funciones_agregar_perfil import existe_archivo
from unlpimage.archivos_auxiliares.funciones_agregar_perfil import controlador_datos




def procesar_eventos(ventana_actual, evento,valores, usuario, imagen_actual ):

    if valores["-EDITAR-OTRO-"] == True:
        valores['-EDITAR-COMBO-'] = valores['-EDITAR-TEXTO-OTRO-']

    if evento == "-EDITAR-VOLVER-":
        ventanas.crear_ventana_principal(usuario["Imagen"])
        ventana_actual.close()

    elif evento == '-EDITAR-AVATAR-':
        #abro la carpeta de archivos para que el usuario elija una nueva imagen
        nueva_imagen = crear_ventana_archivos(ventana_actual['-EDITAR-IMAGEN-'], nueva_imagen= None)
        #si eligio una nueva imahen
        if ( nueva_imagen != None ):
            #actualizo la imagen actual
            imagen_actual = nueva_imagen

    elif evento == "-EDITAR-GUARDAR-" :
        #verifico que los datos sean correctos
        correctos = controlador_datos( valores['-EDITAR-NOMBRE-'], ventana_actual['-EDITAR-TEXTO-NOMBRE-'] ,  valores['-EDITAR-EDAD-'] ,  ventana_actual['-EDITAR-TEXTO-EDAD-'] )
        if correctos :
            #los guardo y cierro la ventana
            f.actualizar_usuario ( usuario, valores , imagen_actual )
            ventana_actual.close() 
        else:
            #le informo al usuario
            sg.popup ( 'Hay campos que se actualizaron con datos no validos.')


    return imagen_actual


def hacer_todo ():

    with open('datos_usuarios.json', 'r') as f:
        usuarios = json.load(f)

    usuario = usuarios[0]

    ventana_actual = crear_ventana_editar_perfil(usuario)


    ruta_completa = os.path.join ( os.getcwd(), "datos_usuarios.json" )

    existe = existe_archivo(ruta_completa)

    if ( not existe ):

        usuarios = open ( 'datos_usuarios.json' , 'x' )  # en caso de que ya exista, lo abro en el Agregar_Perfil

    while True:

        eventos, valores = ventana_actual.read()

        if (eventos == sg.WIN_CLOSED):
                            
            break

        
        
        imagen_actual = procesar_eventos ( ventana_actual, eventos,  valores, usuario, usuario['Imagen'] )
    
