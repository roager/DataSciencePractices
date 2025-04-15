# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 20:07:46 2023

@author: arangela
"""

class Suma0:
    n1=0
    n2=0
    r=0
    
objs0=Suma0()
objs0.n1=5
objs0.n2=6
objs0.r=objs0.n1+objs0.n2
print(objs0.r)

class Suma1:
    n1=0
    n2=0
    r=0
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.r=n1+n2
        
objs1=Suma1(5,6)
print(objs1.r)

class Suma2:
    n1=0
    n2=0
    r=0
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        self.r=n1+n2
    def resultado(self):
        print(self.r)
        
objs2=Suma2(5,6)
objs2.resultado()

class Suma3:
    n1=0
    n2=0
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def resultado(self):
        return self.n1+self.n2

objs3=Suma3(5,6)
print(objs3.resultado())

class Suma4:
    def resultado(self,n1,n2):
        return n1+n2

objs4=Suma4()
print(objs4.resultado(5,6))

class Suma5:
    def __init__(self,n1,n2):
        print(n1+n2)
        
objs5=Suma5(5,6)

class Suma6:
    n1=0
    n2=0
    def setn1(self,n1):
        self.n1=n1
    def setn2(self,n2):
        self.n2=n2
    def getr(self):
        return self.n1+self.n2
    def getn1(self):
        return self.n1
    def getn2(self):
        return self.n2

objs6=Suma6()
objs6.setn1(5)
objs6.setn2(6)
print(objs6.getr())




















