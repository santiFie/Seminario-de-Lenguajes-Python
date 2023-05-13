import PySimpleGUI as sg
import os
import json

imagen_actual = None
veces = 0

def crear_ventana_agregar_perfil():

    """Esta funcion retorna la ventana del Agregar Perfil"""

    correctos = False

    #columna de datos del usuario

    sg.set_options ( element_size= (30,1), font = ( 'Helvetica', 16))

    culumna1 = sg.Column ( layout= [  

                [sg.Text('Ingrese Alias',background_color='#000000')]   ,  
                
                [sg.Input(key = '-AGREGAR-ALIAS-')] , 
                
                [sg.Text('Ingrese nombre:', key= '-AGREGAR-TEXTO_NOMBRE-',background_color='#000000')] , 
                
                [sg.Input( key = '-AGREGAR-NOMBRE-')] , 

                [sg.Text('Ingrese edad:', key= '-AGREGAR-TEXTO_EDAD-', background_color='#000000')] ,
                 
                [sg.Input ( key= '-AGREGAR-EDAD-')] ,

                [sg.Text('Genero autopercibido', background_color='#000000')] ,
                 
                [sg.Combo( ['Masculino','Femenino' ] , key= '-AGREGAR-COMBO-', readonly = True, size= (29,6), default_value=['---Elija una opción---'] )] ,

                [sg.Checkbox ( 'Otro', key = '-AGREGAR-OTRO-' ) ]  ,

                [sg.Input( key= '-AGREGAR-TEXTO-OTRO-', default_text= 'Especifique el genero'  )] ,

                [sg.Button( 'Guardar' , key= '-AGREGAR-GUARDAR-' )] 
                
                ] , background_color='#000000' )
    

    #columna del avatar

    directorio_imagen = os.path.join ( os.getcwd(), 'unlpimage','imagenes_perfiles' )

    imagen = os.path.join ( directorio_imagen, '0.png' )

    columna2 = sg.Column (  

                layout= [                
                
                [sg.Image(filename=imagen, key='-AGREGAR-IMAGEN-' , subsample=1  , size= ( 150,150) )  ] ,
 
                [sg.Button ( 'Seleccionar avatar', key= '-AGREGAR-AVATAR-' , ) ] 
                             
                ], background_color='#000000'
                 
                )       
    



    #columna del volver
    
    columna3 = sg.Column ( layout= [ [ sg.Button( 'Volver', key= '-AGREGAR-VOLVER-') ] ] , expand_x=True, element_justification='right' , background_color='#000000') 
    
    layout = [ [columna3] , [ culumna1, columna2 ]  ]

    ventana= sg.Window('Nuevo Perfil',layout,finalize=True, resizable=True, background_color='#000000', size= ( 800,600 ))

    return ventana


def crear_ventana_archivos (agregar_imagen, nueva_imagen ):

    """Esta funcion crea una ventana para elegir una imagen mediante el browse"""

    layout = [[sg.Text('Seleccione un archivo:')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Button('OK')]]
        
    nueva_ventana = sg.Window( 'Seleccionar archivo', layout= layout , finalize=True )
    
    while True:

        evento, valores = nueva_ventana.read()

        if evento == sg.WIN_CLOSED:
            break

        elif evento == 'OK':

            directorio_imagen = os.path.join ( os.getcwd(), 'imagenes_perfiles' )

            nueva_imagen = os.path.join ( directorio_imagen, valores['Browse'] )

            agregar_imagen.update(source= nueva_imagen )

            break

    nueva_ventana.close()

    return nueva_imagen




def controlador_datos ( nombre, texto_nombre, edad, texto_edad ):

    """Esta funcion analiza si los datos ingresados son correctos"""
    
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




def cargo_un_usuario (valores, imagen , usuarios):
    """Esta funcion agrega un usuario al archivo json"""

    ruta = os.path.join ( os.getcwd(), "datos_usuarios.json" )

    imagen = imagen.split('/')[-1]

    datos = { 
              'Alias'  : valores['-AGREGAR-ALIAS-' ] ,
              'Nombre' : valores['-AGREGAR-NOMBRE-'] ,
              'Edad'   : valores['-AGREGAR-EDAD-'  ] , 
              'Genero' : valores['-AGREGAR-COMBO-' ] ,
              'Imagen' : imagen
            }

    
    usuarios.append(datos)

    
    
    with open('datos_usuarios.json', 'w') as f:
            #print ( usuarios )
            json.dump(usuarios, f)