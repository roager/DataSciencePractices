# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:21:55 2023

@author: arangela
"""

def ejemplo():
	print ("Esto es una funcion sin argumentos")
 
ejemplo()

def suma(a,b):
	resultado = a+b
	return resultado
 
print(suma(5,6))

def restar (actual, nacimiento):
	resultado = actual - nacimiento
	return resultado

 
edad_erronea = restar(1990,2023)
edad = restar(nacimiento=1990, actual=2023)
print (edad_erronea)
print (edad)

def dividir (dividendo, divisor=2):
	resultado = dividendo/divisor
	return resultado
 
cuarto = dividir(40,4)
mitad = dividir(40)
print (cuarto,mitad)

def sumarx(*args):
	resultado = 0
	for valor in args:
		resultado = resultado + valor
	return resultado
 
total = sumarx(4,3,6,2,6)
print (total)
total = sumarx(4,3)
print (total)

def cuadradoycubo (n):
	cuadrado = n ** 2
	cubo = n ** 3
	return cuadrado, cubo
	#return [cuadrado,cubo]
 
 
print (cuadradoycubo(5))
c2, c3 = cuadradoycubo(5)
print (c2)
print (c3)
 
lista = cuadradoycubo(3)
print (lista)

