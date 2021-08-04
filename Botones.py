import random
def Lista_Datos():
	primera_lista=[]
	segunda_lista=[]
	tercera_lista=[]

	while True:
		agregar_numero=random.randint(1,9)
		if agregar_numero not in primera_lista:
			primera_lista.append(agregar_numero)
		if len(primera_lista)==9:
			break
	while True:
		agregar_numero=random.randint(1,9)
		if agregar_numero not in segunda_lista:
			segunda_lista.append(agregar_numero)
		if len(segunda_lista)==9:
			break

	tercera_lista=primera_lista+segunda_lista
	primera_lista=[]
	while True:
		posicion_lista=random.randint(1,17)
		if posicion_lista not in primera_lista:
			primera_lista.append(tercera_lista[posicion_lista])
		if len(primera_lista)==18:
			break
	
	return tercera_lista
