# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:09:09 2026

@author: Invitade
"""

def registrar_habitos(ruta_archivo):
    """
  Lee un archivo con habitos diarios y devuelve una lista de habitos validos
  Parameters
    ---------
    
    return
    --------
    lista
    una lista con las habitos validos diarios em el usuario
    """
    lista_habitos=[]
   try:
        with open(ruta_archivo, "r")as archivo:
            for linea in archivo:
                registro=parsear_linea(linea)
                if not registro_valido(registro):
                    raise ValueError("El registro es invalido")
                lista_habitos.append(registro)
    actividad=input("ingrese la actividad que usted realizo hoy en el dia, para temrinar ingrese stop: ")
   except FileNotFoundError:
        print("Error:el archivo no fue encontrado")   
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
    
