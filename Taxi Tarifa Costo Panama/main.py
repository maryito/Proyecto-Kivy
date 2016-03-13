#!/usr/bin/python
# -*- coding: utf-8 -*-

from kivy.app import App
from  kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from precios import Precio
class Ventana(Screen):
	precio = ObjectProperty
	origen=""
	destino=""
	def Origen(self, origen):
			self.origen = origen
			print (origen)
	def Destino(self, destino):
			self.destino = destino
			print (destino)	
	def CalcularPrecio(self):
			if self.origen != "" and self.destino != "":
                                costo = ""+Precio(self.origen,self.destino)
                                if costo == "null":
                                        self.precio.text ="Costo Aun no Disponible... porque vas de S a N o N a S. Proximamente."
                                else:
                                        self.precio.text = "El Costo del Viaje sera de $ "+costo	
			else:
				self.precio.text = "Aún no a Seleccionado las Ruta..."

class AplicacionApp(App): 
	def build(self):  
		return Ventana()
	def on_pause(self):
		return True



if __name__ == '__main__':
	AplicacionApp().run()
