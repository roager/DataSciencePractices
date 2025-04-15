# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 10:31:43 2023

@author: arangela

https://docs.python.org/es/3/tutorial/errors.html

"""

# =============================================================================
# Error
# while True print('Hello world'):
#     
# Adecuación
# while True: 
#     print('Hello world')
# =============================================================================
    

#Error
#10 * (1/0)
#Adecuación
a=0
if a==0:
    print('No hacer la operación')
else:
    10 * (1/a)

#Error    
#4 + spam*3

#Adecuación
spam=1
4 + spam*3

#Error
#'2' + 2
#Adecuación
'2'+str(2)

#Gestión de excepciones
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")    
        
#Gestión de múltiples excepciones para un mismo flujo de instrucciones
try:
    pass
except (RuntimeError, TypeError, NameError):
     pass

#Personalización de Excepciones en un modelo de herencia
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

#Lanzar de forma explícita excepciones y administrar los parámetros de entrada
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
    
