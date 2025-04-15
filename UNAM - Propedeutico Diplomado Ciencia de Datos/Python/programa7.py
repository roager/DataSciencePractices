# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 18:05:05 2023

@author: arangela
"""
print("PROGRAMA PARA MULTIPLICAR MATRICES")

ra=int(input("Número de renglones en A:"))
ca=int(input("Número de columnas en A:"))

rb=int(input("Número de renglones en B:"))
cb=int(input("Número de columnas en B:"))

if ca==rb:

    A=[[0] * ca for x in range(ra)]
    
    for i in range(ra):
        for j in range(ca):
            A[i][j]=int(input("Dato de A["+str(i)+"]["+str(j)+"]:"))
            
    print("Matriz A:")
    print(A)
    
    B=[[0] * cb for x in range(rb)]
    
    for i in range(rb):
        for j in range(cb):
            B[i][j]=int(input("Dato de B["+str(i)+"]["+str(j)+"]:"))
            
    print("Matriz B:")
    print(B)
    
    R=[[0] * cb for x in range(ra)]
    
    for i in range(ra):
        for j in range(cb):
            for k in range(ca): #rb
                R[i][j]+=A[i][k]*B[k][j]
                
    print("Matriz R:")
    print(R)
    
else:
    print("Las matrices no se pueden multiplicar")