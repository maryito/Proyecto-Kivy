from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager,Screen


class ScreenManager(ScreenManager):
	inventario={}
	#nos permite accerder al objeto identificado con el id yque  declaramos en .kv
	pro= ObjectProperty()
	codigo= ObjectProperty()
	costo= ObjectProperty()
	busquedad = ObjectProperty()
	# funcion para gusradar los dtos del inventario del supermercado
	def save(self):
		#agregagos a el diccionariorios los datos sin no son null
		if self.codigo.text !="" and self.costo.text !="" and self.pro.text != "":
			self.inventario[self.codigo.text] =[self.pro.text,self.costo.text]
		else:
			print ("Supermercado no puede almacenar datos null")
		# limpiamos los campos de las ventana
		self.codigo.text= ""
		self.pro.text= ""
		self.costo.text = ""
		self.producto = ""
		self.precio =""
	def buscando(self):	
		#asginamos el parametro que ingreso el usuario para buscarlo 	
		busquedad =self.busquedad.text

		if busquedad in self.inventario:	
			#traemos los datos del diccionario
			resultado = self.inventario[busquedad]	
			#asginamos los datos a la ventana a mostrar
			self.producto = resultado[0]
			self.precio = resultado[1]
			print ("Busquedad Exitoxa !")

		else:
			print ("Error de Busquedad  o No disponible")
			self.producto = "No Disponible"
			self.precio = "No Disponible"
		# limpiamos la ventana en el campo de busquedad
		self.busquedad.text=""
		

	
class SuperMercadoApp(App):
	def build(self):
		return ScreenManager()

if __name__ == '__main__':
	SuperMercadoApp().run()
