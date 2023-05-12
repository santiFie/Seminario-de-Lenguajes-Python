import PySimpleGUI as sg
import ventanas
import os
import funciones_menu_principal as f
from datetime import datetime


def procesar_eventos(ventana_actual,evento,valores,tags,descripcion,usuario):
    if evento == "-ETIQUETAR-SELECCION-IMAGEN-":
        tags.clear()
        descripcion = ""
        carpeta = f.informacion_archivo()[0]
        valor_actual= valores["-ETIQUETAR-SELECCION-IMAGEN-"][0]
        ruta_completa = os.path.normpath(os.path.join(carpeta, valor_actual))
        
        datos , esta = f.verificar_ruta_en_csv(valor_actual)
        
        if esta:
            resolucion= list(datos[2].split(','))
            datos[2]= resolucion
            cadena= datos[5]
            tags = set(cadena.split(','))
            descripcion = datos[1]
            f.actualizar_ventana_etiquetar(ruta_completa,ventana_actual,datos, tags, descripcion)
        else:
            formato_resolucion_peso = f.calculo_formato_resolucion_peso(ruta_completa)
            datos= [ valor_actual, "", formato_resolucion_peso[1], formato_resolucion_peso[2] , formato_resolucion_peso[0], "", "", ""]

            f.cargar_linea_csv(datos,'informacion_imagenes.csv')
            operacion = "nueva imagen clasificada"
            f.registro_carga_logs(usuario["Alias"],operacion)
            f.actualizar_ventana_etiquetar(ruta_completa,ventana_actual, datos, tags, descripcion)
        
        
    elif evento == "-ETIQUETAR-AGREGAR-TAG-":
        i= len(tags)
        if len(tags)<6:
            if valores["-ETIQUETAR-TAG-"] in tags:
                sg.popup("Debes ingresar una etiqueta la cual no se repita.")
            tags.add(valores["-ETIQUETAR-TAG-"])
            cadena_tags = 'Tags: '+ ' | '.join(map(str, tags))
            ventana_actual["-ETIQUETAR-MOSTRAR-TAG-"].update(cadena_tags)
            
        else:
            sg.popup("Alcanzaste el maximo de etiquetas. Borra una de ellas para poder agregar otra.")

    elif evento == "-ETIQUETAR-ELIMINAR-TAG-":
        if valores["-ETIQUETAR-TAG-"] in tags:
            tags.remove(valores["-ETIQUETAR-TAG-"])
            cadena_tags = 'Tags: '+ ' | '.join(map(str, tags))
            ventana_actual["-ETIQUETAR-MOSTRAR-TAG-"].update(cadena_tags)
        else:
            sg.popup("No se puede borrar. No existe etiqueta con ese nombre.")

    elif evento == "-ETIQUETAR-AGREGAR-DESCRIPCION-":
        if len(valores["-ETIQUETAR-DESCRIPCION-"]) >= 1 :
            descripcion = valores["-ETIQUETAR-DESCRIPCION-"]
            ventana_actual["-ETIQUETAR-MOSTRAR-DESCRIPCION-"].update("Descripcion: "+descripcion)

    elif evento == "-ETIQUETAR-ELIMINAR-DESCRIPCION-":
        descripcion= ""
        ventana_actual["-ETIQUETAR-MOSTRAR-DESCRIPCION-"].update("Descripcion: "+descripcion)

    elif evento == "-ETIQUETAR-GUARDAR-":
        fecha= datetime.timestamp(datetime.now())
        
        imagen_seleccionada= valores["-ETIQUETAR-SELECCION-IMAGEN-"][0] 
        f.buscar_reescribir_en_csv(imagen_seleccionada,tags,descripcion,fecha,usuario)
        linea_logs = [usuario["Alias"], "modificación de imagen previamente clasificada", fecha]
        f.cargar_linea_csv(linea_logs,"logs_sistema.csv")
        sg.popup("Los cambios se guardaron con exito.")
    elif evento == "-ETIQUETAR-VOLVER-":
        ventanas.crear_ventana_principal(usuario["Imagen"])
        ventana_actual.close()
    return tags, descripcion


    