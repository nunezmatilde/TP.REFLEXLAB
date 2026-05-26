import pandas as pd


#datos seria una lista de diccionarios 

def filtrar_por_participante(datos, id_participante= None):
    """
    
    Descripcion: filtra los datos y devuelve los datos del participante solicitado o devuelve los IDs disponibles utilizando pandas 
    Parametro: datos(lista), es una lista de diccionarios con los registros
                id_participante(id), es para identificar al participante a analizar
    Retorno: list- devuelve una lista de registros con la informacion del participante solicidato o lista de IDs si no se especifica el participante. 

    """
    #convertir lista de diccionarios a DataFrame
    df= pd.DataFrame(datos)
    
    if id_participante is None:
        return df["id_participante"].unique().tolist()
    
    #filtrar por participantes usando pandas
    resultado= df[df["id_participante"] == id_participante]
   
    #convierto devuelta a la lista de diccionarios 
            
    return resultado.to_dict(orient="records")#una vez finalizado se retorna la lista
