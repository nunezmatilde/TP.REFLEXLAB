


def parsear_linea(linea):
    """
    
    Descripcion: convierte una linea de un archivo en un diccionario con los datos ordenados 
    Parametros: linea(str), una linea de un archivo que tiene sus valores separados por una coma.
    Retorno: diccionario con los datos del registro

    """
    try:
        separo= linea.strip.split(",")
    
        registro = { 
                   "id_participante": int(separo[0]), 
                   "trial": int(separo[1]), 
                   "estimulo": str(separo[2]), 
                   "t_inicio": float(separo[3]), 
                   "respuesta": bool(separo[4]), 
                   "tiempo_reaccion": float(separo[5]), 
                   "resultado_respuesta": str(separo[6]), 
                   "condicion": str(separo[7]) 
                     } 
    
        return registro
    except IndexError:
        print("Error en parsear_linea: la linea tiene menos columnas de las esperadas.")
        return None
    except ValueError:
        print("Error en parsear_linea: un campo no pudo convertirse al tipo de dato esperado.")
        return None
 