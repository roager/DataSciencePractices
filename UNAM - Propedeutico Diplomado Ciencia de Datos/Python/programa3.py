# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 10:39:21 2023

@author: arangela

https://docs.python.org/es/3/tutorial/introduction.html#lists

(Mostrar lista de paquetes) pip list
(Ejemplo de instalar paquete) pip install mysql-connector
(Ejemplo de versión reciente de paquete) pip install mysql-connector-python
(Ejemplo de desinstalar paquete) pip uninstall mysql-connector

"""

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b
   
i = 256*256
print('The value of i is', i)
    
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

x = int(input("Please enter an integer: "))
#Please enter an integer: 16

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    
# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        
for i in range(5):
    print(i)

list(range(5, 10))
#Out[11]: [5, 6, 7, 8, 9]

lista=list(range(5, 10))

list(range(0, 10, 3))
#Out[13]: [0, 3, 6, 9]

list(range(-10, -100, -30))

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
    
range(10)

sum(range(4))  # 0 + 1 + 2 + 3

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
            print('Hola')
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)
    
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
    
class MyEmptyClass:
    pass

def initlog(*args):
    pass   # Remember to implement this!

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 402:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(400))

# point is an (x, y) tuple
point=(1,2,3)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("No es un punto")

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")













