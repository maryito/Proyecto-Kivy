import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Registro(BoxLayout):
	precio_comida= ObjectProperty()
	lista_pedido= ObjectProperty()
	total_consumido= ObjectProperty() 

	#declaracion de variables que su funcion es acumular datos
	lista_consumido=[]
	consumido = 0  
	#declaracionde metodo que nos traera el plato seleccionado por el usuario
	def menu(self,plato):
		# dicionario que contiene el plato y el precio
		precio_platos = {'Spaguetti con salsa roja':50, 
						 "Pizza de pepperoni":150, 
						 "Camarones":250}
		#asginamos el precio del plato con la opcion selecionada por el usuario				 
		precio =precio_platos[plato]	

		#le asigamos el total apagar  accediedno al objeto y a su propieda .text
		self.precio_comida.text = "    $ "+str(precio) 
		
		#agremagos el plato seleccionado a la lista 
		self.lista_consumido.append(plato) 
		#le enviamos la lista de todo lo consumido  y lo visualizamos atraves del listview .kv
		self.lista_pedido.item_strings = self.lista_consumido

		# vamos acumulando todos los costo consumido por el cliente
		self.consumido = self.consumido+ precio	

		#le asigamos el total apagar  accediedno al objeto y a su propieda .text
		self.total_consumido.text = "$ "+str(self.consumido)
class RestauranteApp(App):
	
	def build(self):
		registro = Registro()
		return registro

if __name__ == "__main__":
    RestauranteApp().run()
