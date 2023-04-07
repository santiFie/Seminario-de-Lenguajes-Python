import string

jupyter_info = """ JupyterLab is a web-based interactive development environment for Jupyter notebooks, 
code, and data. JupyterLab is flexible: configure and arrange the user interface to support a wide range 
of workflows in data science, scientific computing, and machine learning. JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing ones.
"""

palabras = jupyter_info.split(" ")

letra = input ( "Ingrese una letra ")

if not( letra in string.ascii_letters ):
    print ( 'El caracter ingresado no es una letra.')

comienzan_letra = []

for palabra in palabras:
    if ( palabra.startswith(letra) ):
        comienzan_letra.append(palabra)

comienzan_letra = set ( comienzan_letra )

for elem in comienzan_letra:
    print ( elem  )