# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:09:09 2026

@author: Invitade
"""

def registrar_habitos():
    """
    registra los habitos diarios de una persona
    Parameters
    ---------
    
    return
    --------
    lista
    Una lista con las actividades diarias de el usuario
    """
    lista_habitos=[]
    actividad=input("ingrese la activdad que usted realizo hoy en el dia, para temrinar ingrese stop: ")
    while actividad!="stop":
        actividad=input("ingrese la activdad que usted realizo hoy en el dia, para temrinar ingrese stop: ")
        lista_habitos.append(actividad)
    return(lista_habitos)

    ## **Aplicación de PANDAS**

Basándonos en la función `registrar_habitos()`, que es la encargada de registrar los hábitos diarios de una persona, se podría implementar la librería Pandas para organizar los hábitos ingresados por el usuario en una estructura de tipo DataFrame.

La función almacena cada hábito dentro de una lista llamada `lista_habitos`. Mediante el uso de `pd.DataFrame()`, esos datos podrían transformarse en una tabla, donde cada fila representaría un hábito registrado por el usuario.

Dentro de la función se podría aplicar Pandas de la siguiente manera:

import pandas as pd

def registrar_habitos():

    lista_habitos = []

    actividad = input("Ingrese la actividad realizada hoy (para terminar escriba 'stop'): ")

    while actividad != "stop":
        lista_habitos.append(actividad)
        actividad = input("Ingrese otra actividad (o 'stop' para terminar): ")

    df_habitos = pd.DataFrame(lista_habitos, columns=["Habitos"])

    return df_habitos
```

El resultado se almacenaría como un DataFrame y se podría acceder fácilmente a los hábitos registrados mediante filas y columnas.

Es importante entender que la columna `"Habitos"` contendría todas las actividades ingresadas por el usuario. De esta manera, Pandas permitiría analizar mejor los datos, buscar hábitos específicos o incluso contar las actividades repetidas.

    
    
    
#-----------------------MATILDE--------------------------------------------

def analizar_habitos(lista):
    """
    La funcion recibe una lista de actividades y devuelve un diccionario con la cantidad de veces que aparece cada una. 
    
    Parameters
    ----------
    lista : lista de actividades
    
    Returns 
    -------
    diccionario : diccionario en donde las claves son las actividades y el valor es la cantidad de veces que aparecen. 

    """
    diccionario={}
    
    for i in lista:
        if i not in diccionario:
            diccionario[i]=1
            
        else:
            diccionario[i]+=1
    return diccionario
    
