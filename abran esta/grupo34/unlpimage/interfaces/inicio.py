import PySimpleGUI as sg
import json
import os
import sys
from agregar_perfil import hacer_todo
sys.path.append(os.getcwd())
import unlpimage.archivos_auxiliares.funciones_agregar_perfil as funciones_agregar_perfil
from unlpimage.interfaces.menu_principal import menu_principal as mp

# Rutas relativas que van a ser utilizadas


ruta_json = os.path.join(os.getcwd(), 'datos_usuarios.json')


ruta_imagenes = os.path.join(os.getcwd(), 'unlpimage', 'imagenes_perfiles')

# Cargar los datos de los usuarios desde el archivo JSON
with open(ruta_json, 'r') as f:
    usuarios = json.load(f)

boton_adicional_tamanio = (10,2)
boton_usuarios_tamanio = (12,5)

def mostrar_todos_los_usuarios(usuarios):
    """"
    funcion que genera una pantalla para seleccionar entre todos los usuarios
    que se encuentran en el archivo json
    """
    # Definimos los tamaños de los botones
    max_botones_por_fila = 4

    # Creamos la lista de botones
    botones = []
    fila_botones = []
    contador_botones_en_fila = 0

    # Mostramos los botones de usuario
    for usuario in usuarios:
        if contador_botones_en_fila == max_botones_por_fila:
            botones.append(fila_botones)
            fila_botones = []
            contador_botones_en_fila = 0

        nombre_imagen = usuario["Imagen"]
        ruta_imagen = os.path.join(ruta_imagenes, nombre_imagen)
        #print(ruta_imagen)
        fila_botones.append(sg.Button(image_source= ruta_imagen, image_size=(128,128), size=boton_usuarios_tamanio, key=usuario["Alias"], tooltip=usuario["Alias"]))

        contador_botones_en_fila += 1

    # Si no se terminó de completar la última fila de botones, la agregamos a la lista de botones
    if fila_botones:
        botones.append(fila_botones)

    # Agregamos un botón de "Volver"
    botones.append([sg.Button('Volver', size=boton_adicional_tamanio, key='-VOLVER-')])

    # Creamos el layout con los botones
    layout = [
        [sg.Text('UNLPImage', font=('Helvetica', 20), pad=((20, 0), (20, 10)), background_color="#000000")],
        [sg.Column(botones, scrollable=True, vertical_scroll_only=True, background_color="#000000", justification='center', size=(None, None), expand_x=True, expand_y=True, pad=(100, 0))],
    ]




    # Creamos la ventana
    ventana = sg.Window('Todos los usuarios', layout, size=(800, 600), resizable=True, background_color="#000000")

    # Mostramos la ventana y leemos eventos
    while True:
        event, values = ventana.read()
        if event == sg.WIN_CLOSED:
            break
        # Manejamos los eventos según su key
        if event == '-VOLVER-':
            ventana.close()
            generar_pantalla_inicio()
        elif event in [usuario["Alias"] for usuario in usuarios]:
            ventana.close()
            usuario_seleccionado = next(usuario for usuario in usuarios if usuario["Alias"] == event)
            #mp.menu_principal(usuario_seleccionado)
            print(usuario_seleccionado)
            break

    # Cerramos la ventana y terminamos el programa
    ventana.close()


def generar_pantalla_inicio():
    """"
    Esta función genera una pantalla con las opciones de agregar perfil y de presionar sobre 
    una imagen de perfil para acceder a su menu principal

    """
    # Definimos los tamaños de los botones

    max_botones_por_fila = 4

    # Creamos la lista de botones de usuario y botones adicionales
    botones_usuarios = []
    botones_adicionales = []
    alias = []

    # Si no hay usuarios, solo mostramos el botón de agregar perfil
    if not usuarios:
        layout = [[sg.Text('UNLPImage', font=('Helvetica', 20), pad=((0, 0), (20, 40)),background_color="#000000")],
                  [sg.Text('Bienvenido, presione el siguiente botón para crear su usuario:', font=('Helvetica', 15), pad=((120, 0), (20, 50)),background_color="#000000")],
                  [sg.Column([[sg.Button('Agregar perfil', size=boton_usuarios_tamanio, key='-AGREGAR-PERFIL-')]], 
                  pad=(20, 0), justification='center',background_color="#000000")]]
    else:
        # Mostramos los botones de usuario
        for i, usuario in enumerate(usuarios):
            if i < max_botones_por_fila:
                nombre_imagen = usuario["Imagen"]
                ruta_imagen = os.path.join(ruta_imagenes, nombre_imagen)
                #print(ruta_imagen)
                botones_usuarios.append(sg.Button(image_source= ruta_imagen, image_size=(128,128), size=boton_usuarios_tamanio, key=usuario["Alias"],tooltip=usuario["Alias"] ))
                alias.append(usuario["Alias"])

            else:
                break
    

        # Si hay menos de 4 usuarios, mostramos también el botón de agregar perfil
        if len(usuarios) <= max_botones_por_fila:
            botones_adicionales.append(sg.Button('Agregar perfil', size=boton_adicional_tamanio, key='-AGREGAR-PERFIL-'))
        else:
            # Si hay más de 4 usuarios, agregamos un botón para mostrar todos los usuarios
            botones_adicionales.append(sg.Button('Ver todos los usuarios', size=boton_adicional_tamanio, key='-MOSTRAR-PERFILES-'))
            botones_adicionales.append(sg.Button('Agregar perfil', size=boton_adicional_tamanio, key='-AGREGAR-PERFIL-'))
        # Agregamos los botones de usuario y los botones adicionales a la lista de botones

    # Creamos el layout con los botones
        layout = [
            [sg.Text('UNLPImage', font=('Helvetica', 20), pad=((20, 0), (20, 50)),background_color="#000000")],
            [sg.Text('Seleccione su usuario:', font=('Helvetica', 15), pad=(285,25),background_color="#000000")],
            [sg.Column([botones_usuarios], expand_y=True, vertical_scroll_only=True, justification='center', background_color="#000000")],
            [sg.Column([botones_adicionales], background_color="#000000",justification='center', pad=((0, 0), (0, 220)))]
    ]

    # Creamos la ventana
    ventana = sg.Window('UNLPImage', layout, size=(800, 600), resizable=True, background_color="#000000")
    

    # Mostramos la ventana y leemos eventos
    while True:
        event, values = ventana.read()
        if event == sg.WIN_CLOSED:
            break
        # Manejamos los eventos según su key
        if event == '-AGREGAR-PERFIL-':
            ventana.close()
            hacer_todo(generar_pantalla_inicio())
            funciones_agregar_perfil.crear_ventana_agregar_perfil()
        elif event == '-MOSTRAR-PERFILES-':
            ventana.close()
            mostrar_todos_los_usuarios(usuarios)
        elif event in [usuario["Alias"] for usuario in usuarios]:
            #ventana.close()
            usuario_seleccionado = next(usuario for usuario in usuarios if usuario["Alias"] == event)
            mp(usuario_seleccionado)
            break

    # Cerramos la ventana y terminamos el programa
    ventana.close()


generar_pantalla_inicio()