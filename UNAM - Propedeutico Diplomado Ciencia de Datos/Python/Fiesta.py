# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 19:49:12 2023

@author: arangela
"""

class Evento:
    nombre = ''
    tipo = ''
    fecha = ''
    hora_inicio = ''
    hora_fin = ''
    def __init__(self, n, t, f, hi, hf):
        self.nombre = n
        self.tipo = t
        self.fecha = f
        self.hora_inicio = hi
        self.hora_fin = hf
    def publicarDatos(self):
        print("Evento: "+self.nombre)  # Imprime: Fiesta de cumpleaños
        print("Tipo: "+self.tipo)  # Imprime: Social
        print("Fecha: "+self.fecha)  # Imprime: 2023-06-30
        print("Inicio: "+self.hora_inicio)  # Imprime: 20:00
        print("Fin: "+self.hora_fin)  # Imprime: 23:00

class Invitado:
    nombre = ''
    tipo = ''
    genero = ''
    def __init__ (self, n, t, g):
        self.nombre=n
        self.tipo=t
        self.genero=g
    def publicarDatos(self):
        print ("Invitado: " + self.nombre)
        print ("Tipo: "+ self.tipo)
        print ("Género: " + self.genero)

class GrupoMusica:
    nombre=''
    integrantes=0
    tipo=''
    def __init__(self,n,i,t):
        self.nombre=n
        self.integrantes=i
        self.tipo=t
    def publicarDatos(self):
        print("Grupo: "+self.nombre)
        print("Integrantes: "+str(self.integrantes))
        print("Tipo: "+self.tipo)
     
class Fiesta:
    comida=''
    evento=Evento('','','','','')
    invitados=[Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','',''),
               Invitado('','','')]
    gruposMusica=[GrupoMusica('',0,''),
                  GrupoMusica('',0,''),
                  GrupoMusica('',0,'')]
    def __init__(self,c,e,i,g):
        self.comida=c
        self.evento=e
        self.invitados=i
        self.gruposMusica=g
    def publicarBienvenida(self):
        #Describir el evento y mencionar a los invitados
        print("Bienvenidos a la fiesta")
        self.evento.publicarDatos()
        print("Lista de invitados")
        for inv in self.invitados:
            inv.publicarDatos()
    def publicarBaile1(self):
        #Describir el inicio de baile con primer grupo musical
        print("Se apertura el baile")
        self.gruposMusica[0].publicarDatos()
    def publicarComida(self):
        #Describir el tiempo de comida 
        print("Da inicio el tiempo de alimentos")
        print(self.comida)
    def publicarBaile2(self):
        #Describir la segunda fase de baile con el segundo grupo musical
        print("Comienza el segundo momento de baile")
        self.gruposMusica[1].publicarDatos()
    def publicarMariachi(self):
        #Describir la última etapa amenizada con el tercer grupo musical
        print("Comienza la última etapa de amenización")
        self.gruposMusica[2].publicarDatos()
    def publicarCierre(self):
        #Agradecimientos y conclusión de la fiesta
        print("Muchas gracias a todos por su asistencia")
        print("La fiesta ha concluido")
    def publicarDatos(self):
        #Ejecuta todos los métodos de la clase
        self.publicarBienvenida()
        self.publicarBaile1()
        self.publicarComida()
        self.publicarBaile2()
        self.publicarMariachi()
        self.publicarCierre()

class CapturaImplementaFiesta:        
    comida=''
    evento=Evento("", "", "", "", "")
    invitados=[Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','',''),
         Invitado('','','')]
    gruposMusica=[GrupoMusica('',0,''),
                  GrupoMusica('',0,''),
                  GrupoMusica('',0,'')]
    def __init__(self):
        self.comida=self.capturarAlimentos()
        self.evento=self.capturarEvento()
        self.invitados=self.capturarInvitados()
        self.gruposMusica=self.capturarGruposMusica()
    def capturarAlimentos(self):
        a=input('Captura los alimentos de la fiesta: ')
        return a
    def capturarEvento(self):
        evlocal=Evento("", "", "", "", "")
        s1=input('Captura el nombre del evento: ')
        s2=input('Captura el tipo de evento: ')
        s3=input('Captura fecha del evento: ')
        s4=input('Captura hora inicio del evento: ')
        s5=input('Captura hora fin del evento: ')
        evlocal=Evento(s1, s2, s3, s4, s5)
        return evlocal
    def capturarInvitados(self):
        invitados=self.invitados
        for i in range(0,len(self.invitados)):
            s1=input('Captura el nombre del invitado '+str(i)+': ')
            s2=input('Captura el tipo de invitado '+str(i)+': ')
            s3=input('Captura el género del invitado '+str(i)+' (M o H): ')
            invitados[i]=Invitado(s1,s2,s3)
        return invitados
    def capturarGruposMusica(self):
        gruposM=self.gruposMusica
        for i in range(0,len(self.gruposMusica)):
            s1=input('Captura el nombre del grupo musical '+str(i)+': ')
            s2=input('Captura el número de integrantes del grupo '+str(i)+': ')
            s3=input('Captura el tipo de grupo musical '+str(i)+': ')
            gruposM[i]=GrupoMusica(s1,int(s2),s3)
        return gruposM
    def publicarDatos(self):
        objFiesta=Fiesta(self.comida,self.evento,self.invitados,self.gruposMusica)
        objFiesta.publicarDatos()
             
objnvo=CapturaImplementaFiesta()
objnvo.publicarDatos()




