# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:43:50 2023

@author: arangela
"""
import cmath

class Chicha:
    a = 0
    b = 0
    c = 0
  
    def __init__(self,a,b,c):
          self.a = a
          self.b = b
          self.c = c
    
    def imprimir(self):
        print("valor a: " + str(self.a) + " valor b: " + str(self.b) + " valor c: " + str(self.c))
        return 
    
    def resultadoSuma(self):
          return (-(self.b) + (cmath.sqrt(self.b**2 - (4*self.a*self.c))))/(2*self.a)
    
    def resultadoResta(self):
          return (-self.b - (cmath.sqrt(self.b**2 - (4*self.a*self.c))))/(2*self.a)
      
obj=Chicha(1,2,3)
obj.imprimir()
print(obj.resultadoSuma())
print(obj.resultadoResta())

obj2=Chicha(1,2,1)
obj2.imprimir()
print(obj2.resultadoSuma())
print(obj2.resultadoResta())