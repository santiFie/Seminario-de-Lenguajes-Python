import os
import csv

#Generar una función que retorna la actividad de un usuario dado como parámetro. 
# Esta función recibe un parámetro opcional que indica: "TODO" para retornar la información completa, "FACULTAD", solo los accesos realizados desde la facultad 
# (dirección IP comienza con "163.10") o 
# "EXTERIOR, solo los accesos realizados con una IP que no comienza con "163.10". Por defecto la función retorna solo los accesos desde la facultad.


def retronar_actividad ( datos, nombre_usuario, informacion_retorno = "Facultad"):

    info_lower = informacion_retorno.lower()

    actividad = []

    for elem in datos:

        if ( nombre_usuario in elem[1]):

            if ( info_lower == 'todo' ):

                actividad.append(elem)
            
            elif ( info_lower == 'facultad' ):

                if ( elem[6].startswith("163.10")):

                    actividad.append(elem)

            else:
                
                if not( elem[6].startswith("163.10")):

                    actividad.append(elem)
    
    return actividad







def imprimir_datos ( datos, encabezado ):

  

    fecha_usuario = datos[0].split(",")

    print(f"{fecha_usuario[0]:<30}  {datos[3]:<70} {datos[6]:<30}  {fecha_usuario[1]}")






#Escribir un programa que, utilizando la función anterior, muestre un listado similar al siguiente, 
# donde sólo se muestra la información sobre fecha y hora de acceso, recurso accedido y dirección IP. 
# Notar que la columna "Recurso accedido" no muestra todo el texto sino los primeros caracteres de modo que quede prolijo el listado.




ruta_archivo = os.path.join("Documentos", "Python 2023", "Practica", "PythonPlus", "log_catedras.csv")

archivo = open( ruta_archivo, "r")

csvreader = csv.reader(archivo, delimiter=",")

encabezado = next(csvreader)




usuario_ejemplo = 'Geodude'

datos_usuario = retronar_actividad ( csvreader, usuario_ejemplo, "TODO" )





print ( 'Usuario :   ' + usuario_ejemplo )

print()

print ( f'Dia  --                      {encabezado[3]}                                              --     {encabezado[6]}                  --        hora')
         
print ()


print ()





for datos in datos_usuario:

    imprimir_datos ( datos, encabezado)


archivo.close()