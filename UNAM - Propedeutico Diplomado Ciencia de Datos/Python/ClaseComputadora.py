# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:15:27 2023

@author: arangela
"""

class Computadora:
    #Atributos o Variables de Clase (3)
    ram=0
    hd=0
    procesador=''
    #Constructor (1)
    def __init__(self,r,h,p):
        self.ram=r
        self.hd=h
        self.procesador=p
    #Métodos (2)
    def procesarInformacion(self,software,datos):
        informe=False
        if software!='' and datos!='':
            informe=True
        else:
            informe=False
        return informe
    def escribirDocumentos(self,software,documento,usuario):
        archivo=''
        if software!='' and documento!='' and usuario!='':
            archivo='documento.docx'
        else:
            archivo=''
        return archivo

laptop=Computadora(16,500,'Intel Core i5')

print(laptop.ram)
print(laptop.hd)
print(laptop.procesador)

print(laptop.procesarInformacion('SPSS','BD Ventas'))
print(laptop.escribirDocumentos('Word','Modelo en papel','Arturo Rangel'))

pc=Computadora(32,1000,'Intel Core i7')

print(pc.ram)
print(pc.hd)
print(pc.procesador)

print(pc.procesarInformacion('SPSS',''))
print(laptop.escribirDocumentos('Word','Modelo en papel',''))
