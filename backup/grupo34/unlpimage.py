import unlpimage.archivos_auxiliares.funciones_agregar_perfil as funciones_agregar_perfil
import os
import sys

import unlpimage.interfaces.inicio as inicio




ruta_completa = os.path.join ( os.getcwd(), "datos_usuarios.json" )

existe = funciones_agregar_perfil.existe_archivo

if ( not existe ):

    usuarios = open ( 'datos_usuarios.json' , 'x' )  # en caso de que ya exista, lo abro en el Agregar_Perfil
        


inicio.generar_pantalla_inicio()

