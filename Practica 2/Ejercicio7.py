import string

def noEsCaracter ( char ):
    cumple = False
    if  not char.isalpha() and not char.isspace():
        cumple = True
    
    return cumple

texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
 """


mayus = sum (1 for char in texto if char.isupper() )
minusculas = sum ( 1 for char in texto if char.islower() )
no_letras = sum ( 1 for char in texto if noEsCaracter(char) )

print ( no_letras )

palabras_lower = texto.lower().split()

lista = [palabra for palabra in palabras_lower if palabra.isalpha()]
print ( lista )
