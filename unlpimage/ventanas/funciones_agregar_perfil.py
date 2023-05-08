import PySimpleGUI as sg
import os
import json
import PIL as Image





def crear_ventana_agregar_perfil():

    correctos = False

    #columna de datos del usuario

    sg.set_options ( element_size= (30,1), font = ( 'Helvetica', 16))

    culumna1 = sg.Column ( layout= [  

                [sg.Text('Ingrese Alias')]   ,  
                
                [sg.Input(key = '-AGREGAR-ALIAS-')] , 
                
                [sg.Text('Ingrese nombre:', key= '-AGREGAR-TEXTO_NOMBRE-')] , 
                
                [sg.Input( key = '-AGREGAR-NOMBRE-')] , 

                [sg.Text('Ingrese edad:', key= '-AGREGAR-TEXTO_EDAD-')] ,
                 
                [sg.Input ( key= '-AGREGAR-EDAD-')] ,

                [sg.Text('Genero autopercibido')] ,
                 
                [sg.Combo( ['Masculino','Femenino' ] , key= '-AGREGAR-COMBO-', readonly = True, size= (44,6), default_value=['---Elija una opción---'] )] ,

                [sg.Checkbox ( 'Otro', key = '-AGREGAR-OTRO-' ) ]  ,

                [sg.Input( key= '-AGREGAR-TEXTO-OTRO-', default_text= 'Especifique el genero'  )] ,

                [sg.Button( 'Guardar' , key= '-AGREGAR-GUARDAR-' )] 
                
                ]  )
    

    #columna del avatar

    directorio_imagen = 'imagenes'

    imagen = os.path.join ( directorio_imagen, 'AvatarEnBlanco.png' )

    columna2 = sg.Column(  layout=[                
                
                [sg.Image(filename=imagen, key='-AGREGAR-IMAGEN-' )  ] ,
 
                [sg.Button ( 'Seleccionar avatar', key= '-AGREGAR-AVATAR-') ] 
                             
                ]  , element_justification= 'center' )
    



    #columna del volver
    
    columna3 = sg.Column ( layout= [ [ sg.Button( 'Volver', key= '-AGREGAR-VOLVER-') ] ] ) 
    
    layout = [ [ culumna1, columna2 ] , [columna3]  ]

    ventana= sg.Window('Nuevo Perfil',layout,finalize=True, resizable=True)



    return ventana



def crear_ventana_archivos ():

    archivo = None

    layout = [[sg.Text('Seleccione un archivo:')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Button('OK')]]
        
    nueva_ventana = sg.Window( 'Seleccionar archivo', layout= layout , finalize=True )
    
    while True:

        event, values = nueva_ventana.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == 'OK':
            print ( values )
            archivo = values['Browse']
            break

    nueva_ventana.close()

    return archivo





def controlador_datos ( nombre, texto_nombre, edad, texto_edad ):
    
    correctos = True

    if  ( not ( nombre.isalpha() ) )  :

        texto_nombre.update( '*Ingrese su nombre' )
    
        correctos = False
        
    if ( not  ( edad.isdigit() ) ):

        texto_edad.update ( '*Ingrese su edad' ) 
        
        correctos = False
    
    return correctos





def existe_archivo ( ruta ):

    """Si el archivo existe retorno True, en caso contrario retorno False"""

    if ( os.path.isfile(ruta) ):

        return True
    
    else:

        return False




def cargo_un_usuario (valores, imagen ):

    ruta = os.path.join ( os.getcwd(), "datos_usuarios.json" )

    datos = { 
              'Alias'  : valores['-AGREGAR-ALIAS-' ] ,
              'Nombre' : valores['-AGREGAR-NOMBRE-'] ,
              'Edad'   : valores['-AGREGAR-EDAD-'  ] , 
              'Genero' : valores['-AGREGAR-COMBO-' ] ,
              'Imagen' : imagen
            }

    if ( existe_archivo (ruta)):

        with open('datos_usuarios.json', 'r') as f:
            usuarios = json.load(f)

        if ( not datos in usuarios ):
            usuarios.append(datos)

    else:

        usuarios = [datos]
    
    with open('datos_usuarios.json', 'w') as f:
            print ( usuarios )
            json.dump(usuarios, f)