# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#saludo="Hola Mundo"
#print("¡Hola, mundo!")
#print(saludo)

palabras = ["Geniales", "Verde", "Python", "Códigos"]

with open("frases_famosas.txt", "a") as archivo:
    for palabra in palabras:
        archivo.write(palabra + "\n") 
        