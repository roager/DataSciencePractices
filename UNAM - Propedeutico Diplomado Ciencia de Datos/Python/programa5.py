# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:27:15 2023

@author: arangela
"""
base=''
min=0
max=0

print("Tabla de equivalencias de Temperaturas")
base=input("Elegir la base de conversión (C/K/F):")

min=int(input("Introducir el valor mínimo:"))
max=int(input("Introducir el valor máximo:"))

if base=='C' or base=='c':
    print("C\t\t\tK\t\t\tF")
    for c in range(min,max+1):
        print(str(c)+"\t\t\t"+str(c+273.15)+"\t\t\t"+str((9*c/5)+32))
elif base=='K' or base=='k':
    pass
elif base=='F' or base=='f':
    pass
else:
    print("La opción de base indicada no es correcta")

    
