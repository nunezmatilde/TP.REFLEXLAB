
#datos seria una lista de diccionarios 

def filtrar_por_participante(datos, id_participante):
    """
    
    Descripcion: analiza los datos y devuelve los datos del participante solicitado
    Parametro: datos(lista), es una lista de diccionarios con los registros
                id_participante(id), es para identificar al participante a analizar
    Retorno: devuelve una lista con la informacion del participante solicidato

    """
    resultado=[] #creo la lista vacia
    
    for dato in datos: #recorro la info
        ID= dato["id_participante"]
        if ID == id_participante: #si coincide el id se agrega a la lista creada anteriormente
            resultado.append(dato)
            
    return resultado #una vez finalizado se retorna la lista
