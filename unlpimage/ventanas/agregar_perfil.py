import PySimpleGUI as sg
import os
import funciones_agregar_perfil as funciones






ventana_actual = funciones.crear_ventana_agregar_perfil()

ruta_completa = os.path.join ( os.getcwd(), "datos_usuarios.json" )

existe = funciones.existe_archivo

if ( not existe ):

    usuarios = open ( 'datos_usuarios.json' , 'x' )  # en caso de que ya exista, lo abro en el Agregar_Perfil


def procesar_eventos ( ventana_actual , eventos, valores  ):

    correctos = funciones.controlador_datos ( valores['-AGREGAR-NOMBRE-'] ,  ventana_actual['-AGREGAR-TEXTO_NOMBRE-'] ,  valores['-AGREGAR-EDAD-'] ,  ventana_actual['-AGREGAR-TEXTO_EDAD-']  )
    
    if ( eventos == '-AGREGAR-AVATAR-' ):

        archivo = funciones.crear_ventana_archivos()

        if ( archivo != None ):

            ventana_actual['-AGREGAR-IMAGEN-'].update(archivo)

    elif  (eventos == "-AGREGAR-GUARDAR-")  and ( correctos ):

        funciones.cargo_un_usuario ( valores , ventana_actual['-AGREGAR-IMAGEN-'])

        ventana_actual.close()        

    elif (eventos == "-AGREGAR-GUARDAR-") and ( not correctos ):

        sg.popup ( 'Hay campos que contienen datos no validos.')

    elif ( eventos == "-AGREGAR-VOLVER-"):

        ventana_actual.close()


while True:

    eventos, valores = ventana_actual.read()

    if (eventos == sg.WIN_CLOSED):
                        
        break

    procesar_eventos ( ventana_actual, eventos, valores )




