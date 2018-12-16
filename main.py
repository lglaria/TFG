#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing.connection import Listener
from multiprocessing import Process, Manager, Queue
from multiprocessing.connection import Client
from ecdsa_p256 import *
from blockchain import *

def client_listener(): #procesa los mensajes recibidos
	listener = Listener(address=('127.0.0.1', puerto), authkey=key)
	print('listener starting')

	while True:
		print('accepting conexions')
		conn = listener.accept()
		print('connection accepted from', listener.last_accepted)

		m = conn.recv()

		if m[0] == 'get_chain':
			send_queue.put([(listener.last_accepted[0], m[1]),key, Blockchain.cadena])
		elif m[0] == 'send_chain':
			if len(m[2]) > len(Blockchain.cadena) and Blockchain.validar_cadena(m[2]): #verifico que la nueva cadena es valida y la comparo con la que ya tengo
				Blockchain.cadena = m[2] 
		elif m[0] == 'data' and mining == 'on' and crypto.validacion(m[2]):
			bloque = Blockchain.calcular_bloque(m[2]) 
			
			send_queue.put(['all',key,['new_block',bloque]])
		elif m[0] == 'new_block':
			if Blockchain.validar_bloque(m[2], Blockchain.cadena[-1]):
				Blockchain.incluir_bloque(m[2])
		print(len(Blockchain.cadena))
		print(Blockchain.mostrar_datos(Blockchain.cadena))


def send_msg(address0,key, msg):
	if address0 == 'all': #en este caso le enviamos un mensaje a todos los nodos conocidos
		for data in addressbook:
			conn1 = Client(address=data, authkey=key)
			if msg[0] == 'data': #solo firmamos los datos que subimos
				conn1.send([msg[0],puerto,crypto.firma(msg[1])])
			else:
				conn1.send([msg[0],puerto,msg[1]])
			conn1.close()
	else: #este es el caso en que un nodo nos ha pedido nuestra copia de la cadena de bloques	
		conn1 = Client(address=address0, authkey=key)		
		conn1.send(['send_chain',puerto,msg])
		conn1.close()


if __name__ == '__main__':

	addressbook = [('127.0.0.1', 5001)]
	key = 'server'
	crypto = Ecdsa_p256()
	puerto = 6000
	

	mining = 'on' #si on este nodo participa en la prueba de trabajo, modificable.
	send_queue = Queue()

	Blockchain = Blockchain()
	Blockchain.primer_bloque()

	Blockchain.calcular_bloque(crypto.firma('hola_mundo'))
	Blockchain.calcular_bloque(crypto.firma('otro mensaje'))

	p = Process(target=client_listener, args=())
	p.start()

	try:
		while True:

			if not send_queue.empty():
				
				s = send_queue.get()

				send_msg(s[0],s[1],s[2])	
	except:
		pass			


print('end server')

