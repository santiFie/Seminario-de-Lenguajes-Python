import os
import io
import json
import csv
import PySimpleGUI as sg
from datetime import datetime
from PIL import Image

def crear_archivo_guardar_configuracion():
    rutas_por_defecto = { "ruta_imagenes": "", "ruta_collage": "", "ruta_memes": "" }
    with open('ruta_configuracion.json', 'w') as archivo:
        json.dump(rutas_por_defecto, archivo)

def existe_archivo( ruta ):
    if ( os.path.isfile(ruta) ):
        return True
    else:
        return False

def informacion_archivo():
    with open('ruta_configuracion.json', 'r') as archivo:
        rutas = json.load(archivo)
        imagenes = rutas ["ruta_imagenes"]
        collage = rutas ["ruta_collage"]
        memes = rutas ["ruta_memes"]
    return imagenes,collage,memes

def actualizar_informacion_archivo(imagenes,collage,memes):
    with open('ruta_configuracion.json', 'w') as archivo:
        rutas_actualizadas = {"ruta_imagenes": imagenes, "ruta_collage": collage, "ruta_memes":memes}
        json.dump(rutas_actualizadas, archivo)


def calculo_formato_resolucion_peso(ruta_completa):
    imagen = Image.open(ruta_completa)
    resolucion = imagen.size
    formato = imagen.format
    imagen.close()
    peso = os.path.getsize(ruta_completa)
    peso_final = peso/(1024 * 1024)
    if peso_final>=1:
        return formato, resolucion, f" {peso_final:.2f} MB "
    else:
        peso_final = peso/1024
        return formato, resolucion, f" {peso_final:.2f} KB "

def actualizar_ventana_etiquetar(ruta_completa,ventana_actual,datos,tags,descripcion):
    imagen = Image.open(ruta_completa)
    imagen.thumbnail((200,150))
    bio = io.BytesIO()
    imagen.save(bio, format="PNG")
    ventana_actual["-IMAGEN-SELECCIONADA-"].update(data=bio.getvalue())
    ventana_actual["-IMAGEN-SELECCIONADA-"].update(visible=True)
    ventana_actual["-ETIQUETAR-DATOS-IMAGENES-"].update(f" | {datos[4]} |  {datos[3]} | {datos[2][0]}x{datos[2][1]} | ")
    ventana_actual["-ETIQUETAR-DATOS-IMAGENES-"].update(visible=True)
    ventana_actual["-ETIQUETAR-TAG-"].update(disabled=False)
    ventana_actual["-ETIQUETAR-AGREGAR-TAG-"].update(disabled=False)
    ventana_actual["-ETIQUETAR-ELIMINAR-TAG-"].update(disabled=False)
    ventana_actual["-ETIQUETAR-DESCRIPCION-"].update(disabled=False)
    ventana_actual["-ETIQUETAR-AGREGAR-DESCRIPCION-"].update(disabled=False)
    ventana_actual["-ETIQUETAR-ELIMINAR-DESCRIPCION-"].update(disabled=False)
    ventana_actual["-ETIQUETAR-GUARDAR-"].update(disabled=False)
    cadena_tags = 'Tags: '+ ' | '.join(map(str, tags))
    ventana_actual["-ETIQUETAR-MOSTRAR-TAG-"].update(cadena_tags)
    ventana_actual["-ETIQUETAR-MOSTRAR-DESCRIPCION-"].update("Descripcion: " + descripcion)

def crear_archivo_csv(encabezado,ruta_relativa):
    with open(ruta_relativa, 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)

def cargar_linea_csv(linea,ruta_relativa):
    with open(ruta_relativa, 'a', newline='') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(linea)

def verificar_ruta_en_csv(ruta_relativa):
    esta = False
    lista_encontrada= []
    with open('informacion_imagenes.csv', 'r') as archivo:
        lector = csv.reader(archivo)

        # línea del encabezado
        next(lector)

        for linea in lector:
            ruta_actual = linea[0]

            if ruta_actual == ruta_relativa:
                lista_encontrada= linea.copy()
                esta = True
    return lista_encontrada, esta

def buscar_reescribir_en_csv(imagen, tags, descripcion,fecha,usuario):
    archivo_original = 'informacion_imagenes.csv'
    archivo_temporal = 'informacion_imagenes_temporal.csv'

    with open(archivo_original, 'r', newline='') as archivo_orig, open(archivo_temporal, 'w', newline='') as archivo_temp:
        lector = csv.reader(archivo_orig)
        escritor = csv.writer(archivo_temp)

        # Copiar la línea de encabezado al archivo temporal
        encabezado = next(lector)
        escritor.writerow(encabezado)

        # Copiar las líneas del archivo original al archivo temporal, realizando modificaciones en la línea deseada
        for linea in lector:
            if linea[0] == imagen:
                linea[5] = ','.join(map(str, tags))
                linea[1] = descripcion
                linea[6] = usuario["Alias"]
                linea[7] = fecha
            escritor.writerow(linea)

    os.replace(archivo_temporal, archivo_original)

def registro_carga_logs(alias,operacion):
    fecha= datetime.timestamp(datetime.now())
    linea = [alias,operacion,fecha]
    cargar_linea_csv(linea, "logs_sistema.csv")


def actualizar_usuario ( usuario_modificado, valores, imagen ):

    ruta = os.path.join ( os.getcwd(), "datos_usuarios.json" )

    usuario_modificado['Nombre'] = valores['-EDITAR-NOMBRE-'] 
    usuario_modificado['Edad'] = valores['-EDITAR-EDAD-'] 
    usuario_modificado['Genero'] = valores['-EDITAR-COMBO-'] 
    usuario_modificado['Imagen'] = imagen


    with open('datos_usuarios.json', 'r') as f:
            usuarios = json.load(f)

    print ( usuario_modificado )
    
    for usuario in usuarios:
        if usuario_modificado['Alias'] == usuario['Alias']:
            usuario.update(usuario_modificado)

    with open('datos_usuarios.json', 'w') as f:
            print ( usuarios )
            json.dump(usuarios, f)


