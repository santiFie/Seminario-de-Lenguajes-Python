import PySimpleGUI as sg
import os
import funciones_agregar_perfil as funciones
from funciones_agregar_perfil import imagen_actual




def procesar_eventos ( ventana_actual , eventos, valores, imagen_actual   ):

    """Esta funcion los eventos de la ventana Agregar Perfil"""

    #verifico que los datos sean correctos
    correctos = funciones.controlador_datos ( valores['-AGREGAR-NOMBRE-'] ,  ventana_actual['-AGREGAR-TEXTO_NOMBRE-'] ,  valores['-AGREGAR-EDAD-'] ,  ventana_actual['-AGREGAR-TEXTO_EDAD-']  )

    #si se selecciona un avatar, actualizo el que aparece en pantalla
    if ( valores['-AGREGAR-OTRO-'] == True ):
        
        valores['-AGREGAR-COMBO-'] = valores['-AGREGAR-TEXTO-OTRO-']

    if ( eventos == '-AGREGAR-AVATAR-' ):

        nueva_imagen = funciones.crear_ventana_archivos(ventana_actual['-AGREGAR-IMAGEN-'], None)

        if ( nueva_imagen != None ):

            imagen_actual = nueva_imagen

    # guardo los datos si son correctos
    elif  (eventos == "-AGREGAR-GUARDAR-")  and ( correctos ):

        #agrego un usuario al archivo de usuarios

        funciones.cargo_un_usuario ( valores , imagen_actual)

        ventana_actual.close()        

    # si los datos no son correctos, realizo un popup notificandolo
    elif (eventos == "-AGREGAR-GUARDAR-") and ( not correctos ):

        sg.popup ( 'Hay campos que contienen datos no validos.')

    elif ( eventos == "-AGREGAR-VOLVER-"):

        ventana_actual.close()
        


    return imagen_actual

def hacer_todo ():

    imagen_actual = None

    ventana_actual = funciones.crear_ventana_agregar_perfil()


    ruta_completa = os.path.join ( os.getcwd(), "datos_usuarios.json" )

    existe = funciones.existe_archivo

    if ( not existe ):

        usuarios = open ( 'datos_usuarios.json' , 'x' )  # en caso de que ya exista, lo abro en el Agregar_Perfil

    while True:

        eventos, valores = ventana_actual.read()

        if (eventos == sg.WIN_CLOSED):
                            
            break
            generar_pantalla_inicio

        imagen_actual = procesar_eventos ( ventana_actual, eventos,  valores, imagen_actual )
    

