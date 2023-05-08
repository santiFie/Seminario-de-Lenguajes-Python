import csv
import os

def Nunca_Accedieron( orden = "None"):
    ruta = ruta = os.path.dirname(os.path.realpath("."))
    archi = os.path.join(ruta, "log_catedras.csv")
    f = open(archi,"r")
    csvreader = csv.reader(f, delimiter=',')
    
    lista_foro = list(filter(lambda linea: linea [3] == "Foro: Avisos", csvreader));
    lista_nombres = set(map(lambda n: n[1], lista_foro))


    if (orden == "None"):
        return lista_nombres
    else:
        if ( orden == "A"):
            return lista_nombres.sort()
        else:
            if ( orden == "B"):
                return lista_nombres.sort(reverse=True)
    f.close()

Nunca_Accedieron("A")