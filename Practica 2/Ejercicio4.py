



evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources provides the promise of capturing unprecedented details of large-scale complex systems. However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures."""

lineas = evaluar.split( '\n' )

dicc_oraciones = {"faciles" : 0,
                  "aceptables" : 0,
                  "diciles" : 0,
                  "muy dificiles" : 0}


#quito los elementos de la lista que no son palabras o no forman parte del cuerpo del titulo

titulo = lineas[0].split(" ")
titulo.remove("título:")
titulo.remove("")



oraciones = lineas[1].split("resumen: ")[1]

oraciones = oraciones.split(". ")



for oracion in oraciones:

    tamanio = len(oracion.split(" "))

    if ( tamanio <= 12 ):
        dicc_oraciones["faciles"] += 1
    elif ( tamanio <= 17 ):
        dicc_oraciones["aceptables"] += 1
    elif ( tamanio <= 25 ):
        dicc_oraciones["diciles"] += 1
    else:
        dicc_oraciones["muy dificiles"] += 1



if ( len(titulo) <= 10 ):
    print("El titulo cumple con las condiciones.")
else:
    print ( "El titulo NO cumple con las condiciones.")


print ( f"Cantidad de oraciones faciles de leer: {dicc_oraciones['faciles']}, aceptables para leer: {dicc_oraciones['aceptables']}, dificiles de leer: {dicc_oraciones['diciles']}, muy dificil de leer: {dicc_oraciones['muy dificiles']}" )
