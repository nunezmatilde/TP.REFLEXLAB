
import pandas as pd

def leer_archivo(ruta_archivo):
    """
    descripcion: lee un archivo CSV usando pandas y devuelve los datos como lista de diccionarios.
    parametros: ruta_archivo (str)- ruta del archivo CSV.
    retorno: list - lista de registros (diccionarios)
    
    """
    try: 
        df= pd.read_csv(ruta_archivo)

        #convierte cada fila en un diccionario
        datos= df.to_dict(orient="records") #cada fila un diccionario 
        return datos 
    
    except Exception as e:
        print(f"Error al leer el archivo con pandas: {e}")
        return[]
    
    
def parsear_linea(linea):
    """
    
    Descripcion: convierte una linea de un archivo en un diccionario con los datos ordenados  
    Parametros: linea(str), una linea de un archivo que tiene sus valores separados por una coma.
    Retorno: diccionario con los datos del registro o None si salta un error

    """
    try:
        separo= linea.strip().split(",")
        
        
        if len(separo)!=8: #lo pongo para verificar si tiene 8 elementos
            raise ValueError("cantidad de campos incorrecta")
    
        registro= { 
            "id_participante": int(separo[0]), 
            "trial": int(separo[1]), 
            "estimulo": str(separo[2]), 
            "t_inicio": float(separo[3]), 
            "respuesta": bool(separo[4]=="True"), 
            "tiempo_reaccion": float(separo[5]), 
            "resultado_respuesta": str(separo[6]), 
            "condicion": str(separo[7]) 
            }
     
        return registro

    except Exception as e:
        print(f"Error: {e}")
       
        return None

    















    


  