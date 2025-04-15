# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 19:05:20 2023

@author: arangela
"""

def tablamultiplicar (n):
    print("Tabla de multiplicar del número "+str(n))
    for x in range (1,11):
        print(f'{n} x {x} = {n * x}')
    
tablamultiplicar(int(input("Número de la tabla de multiplicar a mostrar: ")))

# #Tabla Multiplicar
# for i in range(1,11):
#     print(f'Tabla de multiplicar del {i}:')
#     for j in range (1,11):
#         print(f'{i} x {j} = {i * j} \n')