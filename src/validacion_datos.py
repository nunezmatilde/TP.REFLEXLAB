
import pandas as pd
def validar_datos(ruta):
     """
     Procesa un archivo linea por linea
     
     Parámetros:
         ruta(str): nombre del archivo a procesar o ruta
         
     retorna:
             lista: retonra una lista de registros validos apartir del archivo
     """
   

     df = pd.read_csv(ruta)
     df = df.dropna()  # elimina filas con valores vacíos/inválidos
     return df