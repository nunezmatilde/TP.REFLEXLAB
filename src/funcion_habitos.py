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
    actividad=input("ingrese la actividad que usted realizo hoy en el dia, para temrinar ingrese stop: ")
    while actividad!="stop":
        lista_habitos.append(actividad)
        actividad=input("ingrese la actividad que usted realizo hoy en el dia, para temrinar ingrese stop: ")
        
    return(lista_habitos)

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
    