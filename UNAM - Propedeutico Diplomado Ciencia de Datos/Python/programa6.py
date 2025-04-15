# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:38:10 2023

@author: arangela
"""

#import numpy as np
#a =np.array([[1,4,7],[2,5,8],[3,6,9]])
#b =np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(a+b)


def sumar_matrices(matriz1, matriz2):
    resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    for i in range(3):
        for j in range(3):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    
    return resultado

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz 1
matriz1 = [
    [1, 4, 7],
    [2, 5, 6],
    [3, 6, 9]
]

# Matriz 2
matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Sumar las matrices
resultado = sumar_matrices(matriz1, matriz2)

# Mostrar el resultado
print("Matriz 1:")
imprimir_matriz(matriz1)

print("\nMatriz 2:")
imprimir_matriz(matriz2)

print("\nMatriz Resultado:")
imprimir_matriz(resultado)

########################################

#Génesis Osorio 18:01
A=[[1,4,7],[2,5,8],[3,6,9]]
B=[[1,2,3],[4,5,6],[7,8,9]]

C=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range (len(A[0])):
        C[i][j]=A[i][j]+B[i][j]
        
print(C)