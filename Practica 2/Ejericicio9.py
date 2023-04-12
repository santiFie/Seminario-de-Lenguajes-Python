def buscar_letra ( letra, claves, tabla ):

    valor = 0

    for clave in claves:

        if ( letra in clave):

            valor = tabla[clave]
    
    return valor



tabla = { "AEIOULNRST" : 1,
         "DG" : 2,
         "BCMP" : 3,
         "FHVWY" : 4,
         "K" : 5,
         "JX" : 8,
         "QZ" : 10 }

palabra = input ( "Ingrese una palabra: " )


palabra_mayuscula = palabra.upper()

letras = list ( palabra_mayuscula )

suma = 0
claves = tuple ( tabla.keys() )



suma = sum ( list ( map ( lambda x : buscar_letra(x, claves, tabla) , letras)   )    )

print ( suma )

