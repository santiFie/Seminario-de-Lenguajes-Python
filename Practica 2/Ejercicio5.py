string = input ("Ingrese una frase: ")
palabra = input ( 'Ingrese una palabra a contar: ')



string = string.lower()

lista_palabras = string.split()



if ( palabra.lower() in lista_palabras):
    print ( f"La palabra {palabra} aparecio {lista_palabras.count(palabra.lower())} veces en la frase.")

