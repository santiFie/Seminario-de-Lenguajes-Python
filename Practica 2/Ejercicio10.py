def calcularPromedio ( tupla ):
    """ sumo las notas y las divido por la cantidad de notas"""
    return round ( ( ( tupla[1] + tupla[2]) / len(tupla)-1 ), 2)


nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7,
74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

nombres = nombres.replace(",", " ").replace("\n", " ").replace("'", " ")

lista_nombres = nombres.split()



notas_1 = notas_1[:len(lista_nombres)]

notas_2 = notas_2[:len(lista_nombres)]


tupla =  tuple ( zip ( lista_nombres, notas_1, notas_2 ) )




lista_promedios = list( map( lambda x: calcularPromedio(x), tupla))

promedios_alumnos = list ( zip ( lista_nombres, lista_promedios ))



promedio_general =  round ( ( sum ( lista_promedios ) / len (promedios_alumnos)) , 2 )



nota_promedio_maxima = max( lista_promedios )


alumno_maximo = list ( filter(lambda x: x[1] == nota_promedio_maxima, promedios_alumnos)) 



todas_notas = notas_1 + notas_2

nota_minima = min( todas_notas )

alumno_minimo = list ( filter(lambda x: x[1] == nota_minima, tupla )) [0][0]

print ( tupla )

print ( f"El alumno con la nota mas baja es {alumno_minimo}" )



print ( f"El alumno con nota promedio mas alta es: {alumno_maximo[0][0]}" )


