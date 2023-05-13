import os
from . import funciones_menu_principal as f
from . import ventanas as v


def procesar_eventos(ventana_actual, evento,usuario):
    if evento == "-PRINCIPAL-CONFIG-":
        ruta_completa= os.path.join (os.getcwd(), "ruta_configuracion.json")
        if not f.existe_archivo(ruta_completa) :
            f.crear_archivo_guardar_configuracion()
        texto= f.informacion_archivo()
        v.crear_ventana_configuracion(texto[0], texto[1], texto[2])
        ventana_actual.close()
        
    elif evento == "-PRINCIPAL-AYUDA-":
        v.crear_ventana_ayuda()
        ventana_actual.close()
    
    elif evento == "-PRINCIPAL-NICK-":
        v.crear_ventana_editar_perfil(usuario)
        ventana_actual.close()
    
    elif evento == "-PRINCIPAL-ETIQUETAR-":
        ruta_completa= os.path.join (os.getcwd(), "informacion_imagenes.csv")
        if not f.existe_archivo(ruta_completa) :
            encabezado = ['Ruta', 'texto descriptivo', 'resolución', 'tamaño', 'tipo', 'lista de tags', 'perfil actualizo', 'última actualización']
            f.crear_archivo_csv(encabezado,ruta_completa)
        v.crear_ventana_etiquetar_imagenes()
        ventana_actual.close()

    elif evento == "-PRINCIPAL-MEME-":
        v.crear_ventana_generar_meme()
        ventana_actual.close()
    
    elif evento == "-PRINCIPAL-COLLAGE-":
        v.crear_ventana_generar_collage()
        ventana_actual.close()

    elif evento == "-PRINCIPAL-SALIR-":
        return ventana_actual.close()
    
    

