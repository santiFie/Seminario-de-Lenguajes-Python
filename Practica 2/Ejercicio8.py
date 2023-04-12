
palabra = input ( 'Ingrese una palabra: ' )

#hago un conjunto con las letras pasadas a minuscula de la palabra y le quito ( en caso de tener ) los espacios sobrantes de adelante y atras de la palabra

letras_distintas = set ( palabra.lower().strip() ) 



if ( len ( letras_distintas ) == len ( palabra ) ):

    print ( "La palabra ingresada es heterograma.")

else:

    print ( "La palabra ingresada NO es heterograma.")