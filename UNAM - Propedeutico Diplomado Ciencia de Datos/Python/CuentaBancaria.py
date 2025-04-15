# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:22:32 2023

@author: arangela
"""

# =============================================================================
# CuentaBancaria
#  + numeroCuenta:int
#  + nombreCuentahabiente:String
#  + nombreBanco:String
#  + tipoCuenta:String
#  + saldo:float
#  + CuentaBancaria(nomch:String,tc:String)
#  + CuentaBancaria(numc:int)
#  + transferirCash(importe:float,numctr:int):confirmacion
#  + consultarSaldo( ):saldo
#  + darDeBajaCuenta( ):confirmacion
#  + depositarCash(importe:float):confirmacion
#  + retirarCash(importe:float):confirmacion
# =============================================================================

class CuentaBancaria:
    
    # numeroCuenta=0
    # nombreCuentahabiente=''
    # nombreBanco=''
    # tipoCuenta=''
    # saldo=0.0
    
    def CuentaBancaria1(self,nomch,tc):
        self.nombreCuentahabiente=nomch
        self.tipoCuenta=tc
        self.numeroCuenta=123456789
        self.nombreBanco='HSBC'
        if tc=='Nómina':
            self.saldo=0
        elif tc=='Ahorro':
            self.saldo=2000
        elif tc=='Cheques':
            self.saldo=5000
        else:
            self.saldo=0
            
    def CuentaBancaria2(self,numc):
        self.numeroCuenta=numc
        if numc==111111111:
            self.nombreCuentahabiente='Nelly Loranca Quintero'
            self.tipoCuenta='Ahorro'
            self.nombreBanco='HSBC'
            self.saldo=15000
        elif numc==222222222:
            self.nombreCuentahabiente='Oscar Flores Contreras'
            self.tipoCuenta='Cheques'
            self.nombreBanco='HSBC'
            self.saldo=133000
    
    def transferirCash(self,importe,numctr):
        confirmacion=False
        if importe!=0 and numctr!=0:
            self.saldo = self.saldo - importe
            confirmacion=True
        else:
            confirmacion=False
        return confirmacion
    
    def consultarSaldo(self):
        return self.saldo
    
    def darDeBajaCuenta(self):
        confirmacion=False
        if self.saldo==0:
            confirmacion=True
        else:
            confirmacion=False
        return confirmacion
    
    def depositarCash(self,importe):
        confirmacion=False
        if importe>=0:
            self.saldo = self.saldo + importe
            confirmacion=True
        else:
            confirmacion=False
        return confirmacion
    
    def retirarCash(self,importe):
        confirmacion=False
        if importe<=self.saldo:
            self.saldo = self.saldo - importe
            confirmacion=True
        else:
            confirmacion=False
        return confirmacion

# Objetos de Cuenta Nueva
ctaNva=CuentaBancaria()
ctaNva.CuentaBancaria1('Arturo Rangel Álvarez','Nómina')

print(ctaNva.nombreBanco)
print(ctaNva.numeroCuenta)
print(ctaNva.consultarSaldo())

print(ctaNva.depositarCash(5000))

print(ctaNva.nombreBanco)
print(ctaNva.numeroCuenta)
print(ctaNva.consultarSaldo())

print(ctaNva.retirarCash(2000))

print(ctaNva.nombreBanco)
print(ctaNva.numeroCuenta)
print(ctaNva.consultarSaldo())

print(ctaNva.darDeBajaCuenta())
print(ctaNva.nombreBanco)
print(ctaNva.numeroCuenta)
print(ctaNva.consultarSaldo())

# Objetos de Cuenta Existente
ctaExs=CuentaBancaria()
ctaExs.CuentaBancaria2(222222222)

print(ctaExs.nombreCuentahabiente)
print(ctaExs.nombreBanco)
print(ctaExs.tipoCuenta)
print(ctaExs.consultarSaldo())

print(ctaExs.depositarCash(5000))

print(ctaExs.nombreCuentahabiente)
print(ctaExs.nombreBanco)
print(ctaExs.tipoCuenta)
print(ctaExs.consultarSaldo())

print(ctaExs.retirarCash(2000))

print(ctaExs.nombreCuentahabiente)
print(ctaExs.nombreBanco)
print(ctaExs.tipoCuenta)
print(ctaExs.consultarSaldo())

print(ctaExs.darDeBajaCuenta())

print(ctaExs.nombreCuentahabiente)
print(ctaExs.nombreBanco)
print(ctaExs.tipoCuenta)
print(ctaExs.consultarSaldo())