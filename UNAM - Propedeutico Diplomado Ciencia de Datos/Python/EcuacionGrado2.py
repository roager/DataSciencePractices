# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 19:36:57 2023

@author: arangela
"""

class EcuacionGrado2:
    a=0.0
    b=0.0
    c=0.0
    x1=''
    x2=''
    def __init__ (self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def discriminante(self):
        return (self.b**2)-(4*self.a*self.c)
    def resolverX1X2 (self):
        d=self.discriminante()
        if self.a==0:
            self.x1='La ecuación no es de segundo grado'
            self.x2='La ecuación no es de segundo grado'
        else:
            if d>=0:
                self.x1=(-self.b-((d)**0.5))/(2*self.a)
                self.x2=(-self.b+((d)**0.5))/(2*self.a)
            else:
                self.x1=str(-self.b/(2*self.a))+' - '+str(((-d)**0.5)/(2*self.a))+' i '
                self.x2=str(-self.b/(2*self.a))+' + '+str(((-d)**0.5)/(2*self.a))+' i '

ec1=EcuacionGrado2(1,2,1)
ec1.resolverX1X2()
print(ec1.x1)
print(ec1.x2)

ec2=EcuacionGrado2(1,2,3)
ec2.resolverX1X2()
print(ec2.x1)
print(ec2.x2)

ec3=EcuacionGrado2(0,2,3)
ec3.resolverX1X2()
print(ec3.x1)
print(ec3.x2)
