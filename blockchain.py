#to English
"""
Implementacion de un gestor de publicaciones basado en blockchain
Por convenio se incluye una unica transaccion en cada bloque
"""
#Implementacion de un gestor de publicaciones basado en blockchain
#Por convenio se incluye una unica transaccion en cada bloque
from hashlib import sha256
#from ecdsa import VerifyingKey, SigningKey
import time
import random

#docstrings python, check
class Blockchain(object): #pasar a mayuscula init
	#formato bloques [hash_bloque_anterior, (data,data), timestamp, indice, nonce]
	"""
	formato bloques [hash_bloque_anterior, (data,data), timestamp, indice, nonce]
	"""
	def __init__(self):
		self.cadena = []
		self.longitud_nonce = 4 #DIFICULTAD DE POW se puede modificar

	def primer_bloque(self): #metodo para generar el primer bloque (cuando creamos la cadena)
		primer_bloque = [0,0,int(round(time.time())),0]
		self.cadena.append(self.pow(primer_bloque))

	def pow(self,bloque): #dado un bloque calcula un nonce
		bloque_str = ''.join(str(e) for e in bloque)
		while True:
			var = format(random.getrandbits(32), '08b') #buscamos nonces de 32 bits
			if sha256((bloque_str+str(var)).encode('utf-8')).hexdigest()[:self.longitud_nonce] == '0'*self.longitud_nonce:
				break
		bloque.append(var)
		return bloque

	def calcular_bloque(self, dato1): #equivale al proceso de minado
		ultimo_bloque = self.cadena[-1]
		indice_anterior = ultimo_bloque[3]
		#se calcula el hash del bloque anterior
		hash_anterior = sha256((''.join(str(e) for e in ultimo_bloque)).encode('utf-8')).hexdigest()

		timestamp = int(round(time.time()))

		bloque = self.pow([hash_anterior, dato1,timestamp, indice_anterior+1])
		self.cadena.append(bloque)                         
		return bloque

	def validar_bloque(self, bloque, ultimo_bloque): #se comprueba si el bloque recibido es correcto respecto al ultimo bloque que tenemos
	#se podria incluir alguna comprobacion adicional sobre el timestamp
	# ultimo_bloque = self.cadena[-1] <- esta es la forma de obtener el ultimo bloque dada la cadena
		hash_anterior = sha256(''.join(str(e) for e in ultimo_bloque)).hexdigest()

		if hash_anterior != bloque[0] or ultimo_bloque[3]+1 != bloque[3]: #se comprueba que coincidan tanto el hash anterior como que el indice sea consecutivo
			return False
		if sha256(''.join(str(e) for e in bloque)).hexdigest()[:self.longitud_nonce] == '0'*self.longitud_nonce:
			return True
		else:
			return False

	def incluir_bloque(self,bloque):
		if self.validar_bloque(bloque, self.cadena[-1]):
			self.cadena.append(bloque)

	def mostrar_datos(self, cadena):
		datos = []
		for bloque in cadena:
			if bloque[3] > 0:
				datos.append((bloque[1][0], bloque[1][2].x)) #devuelve el dato almacenado y la coordenada x de la clave publica de quien lo ha agregado
		return datos

	def validar_cadena(self, cadena):
		for bloque in cadena:
			if bloque[3] == 0: #si estamos con la cadena inicial
				if sha256(''.join(str(e) for e in bloque)).hexdigest()[:self.longitud_nonce] != '0'*self.longitud_nonce:
					return False
				bloque_anterior = bloque
			else:
				if not self.validar_bloque(bloque, bloque_anterior):
					return False
				else:
					bloque_anterior = bloque
		return True

