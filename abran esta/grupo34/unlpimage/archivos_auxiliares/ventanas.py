import PySimpleGUI as sg
import sys
print ( sys.path )
import funciones_menu_principal as f
import os
import io
from PIL import Image

def crear_ventana_principal(usuario):

    carpeta_menu = os.path.join(os.getcwd(), "unlpimage", "imagenes_menu")
    rueda_configuracion = "Ruedita_de_configuracion.png"
    simbolo_ayuda = "Simbolo_ayuda.png"
    carpeta_perfiles = os.path.join(os.getcwd(), "unlpimage", "imagenes_perfiles")
    ruta_perfil_imagen = os.path.normpath(os.path.join(carpeta_perfiles, usuario))
    imagen_perfil = Image.open(ruta_perfil_imagen)
    imagen_perfil.thumbnail((100,100))
    bio = io.BytesIO()
    imagen_perfil.save(bio, format="PNG")

    layout = [[sg.Button(image_source= bio.getvalue() , key="-PRINCIPAL-NICK-", tooltip= "Seleccione para editar datos del usuario actual.",size=(10, 2))],
              [sg.Column([[sg.Button(image_source= os.path.join(carpeta_menu,rueda_configuracion), image_size=(64,64),border_width=0 ,key="-PRINCIPAL-CONFIG-",
                                     tooltip= "Seleccione para entrar a la configuracion de la aplicacion.")],
                          [sg.Button(image_source= os.path.join(carpeta_menu,simbolo_ayuda), image_size=(64,64),border_width=0 ,key = "-PRINCIPAL-AYUDA-")]]
                          ,justification="right",background_color="#000000")],
              [sg.Column([
                  [sg.Button("Etiquetar imagenes",key="-PRINCIPAL-ETIQUETAR-", tooltip= "Seleccione para poder agregar tags y descripciones a las imagenes.",size=(16, 4))],
                  [sg.Button("Generar Meme", key="-PRINCIPAL-MEME-", tooltip= "Seleccione para poder generar Memes con imagenes escogidas y luego almacenarlas.",size=(16, 4))],
                  [sg.Button("Generar Collage",key="-PRINCIPAL-COLLAGE-", tooltip= "Seleccione para generar Collage con imagenes escogidas y luego almacenarlas.",size=(16, 4))],
              [sg.Button("Salir", key="-PRINCIPAL-SALIR-",size=(16, 4))]],justification="center",background_color="#000000")]]
    
    return sg.Window("Menu principal", layout, finalize=True, size=(800, 600), resizable=True, background_color="#000000")

def crear_ventana_configuracion(texto_1, texto_2, texto_3):
    layout = [[sg.Button("Volver", key="-CONFIGURACION-VOLVER-")],
              [sg.Button("Guardar",key="-CONFIGURACION-GUARDAR-")],
             [sg.Column([
                [sg.Text("Selecciona una carpeta para el repositorio de imagenes:",background_color="#000000")], [sg.Input(default_text=texto_1), sg.FolderBrowse()], 
                [sg.Text("Selecciona una carpeta para almacenar tus collage generados:",background_color="#000000")],[sg.Input(default_text=texto_2),sg.FolderBrowse()],
                [sg.Text("Selecciona una carpeta para almacenar tus memes generados:",background_color="#000000")],[sg.Input(default_text=texto_3),sg.FolderBrowse()]]
                ,justification="center",background_color="#000000")]]

    return sg.Window("Configuracion", layout, finalize=True, size=(800, 600), resizable=True, background_color="#000000")

def crear_ventana_ayuda():
    layout= [[sg.Column([[sg.Text("Para obtener información sobre la funcionalidad de cada botón, basta con colocar el cursor sobre el botón que se desea seleccionar. De esta manera, se mostrará una breve descripción o ayuda que proporciona detalles sobre el propósito o función del botón.",
                     size=(60, 5),justification="center")],
            [sg.Button("Ok", key="-AYUDA-OK-", size=(10, 2))]],justification="center")]]
    return sg.Window("Ayuda", layout, finalize=True, size=(800, 600), resizable=True,  background_color="#000000")

def crear_ventana_editar_perfil(usuario):

    columna1 = sg.Column (layout= [ [sg.Text("Alias")] , 
                          
                [sg.Input(key = "-EDITAR-ALIAS-", readonly=True, default_text= usuario['Alias'])] , 

                [sg.Text("Nombre", key="-EDITAR-TEXTO-NOMBRE-")] , 

                [sg.Input( key = "-EDITAR-NOMBRE-", default_text= usuario['Nombre'])]  ,
                
                [sg.Text("Edad", key="-EDITAR-TEXTO-EDAD-")] , [sg.Input ( key= "-EDITAR-EDAD-", default_text= usuario['Edad'])],

                [sg.Text("Genero autopercibido")] , 
                
                [sg.Combo( ["Masculino","Femenino" ] , key= "-EDITAR-COMBO-", size= (44,6), default_value=usuario['Genero']) ] ,

                [sg.Checkbox ( "Otro", key = "-EDITAR-OTRO-" ) ]  ,

                [sg.Button( "Guardar", key = "-EDITAR-GUARDAR-" )],

                [sg.Button("Volver", key="-EDITAR-VOLVER-")]

                ], background_color='#000000'

              )
    
    directorio_imagen = os.path.join ( os.getcwd(), 'unlpimage','imagenes_perfiles' )

    imagen = os.path.join ( directorio_imagen,usuario['Imagen'] )


    columna2 = sg.Column (  

                layout= [                

                [sg.Image(filename=imagen, key='-EDITAR-IMAGEN-' , subsample=1  , size= ( 150,150) )  ] ,
 
                [sg.Button ( 'Seleccionar avatar', key= '-EDITAR-AVATAR-' , ) ] 
                             
                ], background_color='#000000'
                 
                )
    layout = [  [columna1, columna2]  ]
    
    return sg.Window("Editar Perfil", layout, finalize=True, size=(800, 600), resizable=True, background_color="#000000")
    
def crear_ventana_etiquetar_imagenes():

    try:
        carpeta_imagenes = f.informacion_archivo()[0]
        imagenes = [elemento for elemento in os.listdir(carpeta_imagenes) if elemento.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
        ok = True
    except FileNotFoundError:
        sg.popup("El sistema no pudo encontrar la ruta especificada, pruebe modificando la ruta del repositorio de imagenes en la configuracion de la aplicacion.")
        imagenes = []
        ok= False

    layout = [[sg.Text("Imágenes en la carpeta seleccionada:", background_color="#000000", expand_x=True),
               sg.Button("Volver", key= "-ETIQUETAR-VOLVER-")],
             [sg.Listbox(values= imagenes, size=(30, 10), key="-ETIQUETAR-SELECCION-IMAGEN-",enable_events=ok)],
             [sg.Column([
                        [sg.Text("Tag", background_color="#000000")],
                        [sg.Input(key="-ETIQUETAR-TAG-", disabled=True)],
                        [sg.Button("Agregar", key="-ETIQUETAR-AGREGAR-TAG-", disabled=True, tooltip="Presione para agregar una etiqueta."),
                        sg.Button("Eliminar", key="-ETIQUETAR-ELIMINAR-TAG-", disabled=True, tooltip="Presione para eliminar una etiqueta.")],
                        [sg.Text("Texto descriptivo", background_color="#000000")],
                        [sg.Input(key="-ETIQUETAR-DESCRIPCION-", disabled=True)],
                        [sg.Button("Agregar", key="-ETIQUETAR-AGREGAR-DESCRIPCION-", disabled=True, tooltip="Presione para agregar descripcion."),
                         sg.Button("Eliminar", key="-ETIQUETAR-ELIMINAR-DESCRIPCION-",disabled=True, tooltip="Presione para eliminar la descripcion.")]
                        ],size= (250,200), background_color="#000000")
             ,sg.Text(" ",expand_x=True, background_color="#000000"),
             sg.Column([[sg.Image(key="-IMAGEN-SELECCIONADA-", visible=False)],
                         [sg.Text("", key="-ETIQUETAR-DATOS-IMAGENES-", visible=False, background_color="#000000")]]
                         ,justification="right",size= (250,200), background_color="#000000")
             ], 
                        [sg.Text(" ",expand_x=True, background_color="#000000") ,sg.Text("", key="-ETIQUETAR-MOSTRAR-TAG-", background_color="#000000")],
                        [sg.Text(" ",expand_x=True, background_color="#000000"),sg.Text("", key="-ETIQUETAR-MOSTRAR-DESCRIPCION-",background_color="#000000")], 
                        [sg.Text(" ",expand_y=True, background_color="#000000")],
                        [sg.Text(" ",expand_x=True, background_color="#000000"), sg.Button("Guardar", key="-ETIQUETAR-GUARDAR-", disabled=True, tooltip="Presione para guardar cambios")]
             ]
    
    return sg.Window("Etiquetar imagenes", layout, finalize=True, size=(800, 600), resizable=True, background_color="#000000")

def crear_ventana_generar_meme():

    layout = [[sg.Button("Volver", key= "-MEME-VOLVER-")]]

    return sg.Window("Generar Meme", layout, finalize=True, size=(800,600), resizable=True, background_color="#000000")

def crear_ventana_generar_collage():

    layout = [[sg.Button("Volver", key= "-COLLAGE-VOLVER-")]]

    return sg.Window("Generar Collage", layout, finalize=True, size=(800,600), resizable=True, background_color="#000000")
