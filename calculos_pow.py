#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from gestor import *
import string

Blockchain = blockchain()


def random_array(length): #metodo para generar un array aleatorio de longitud fija
	array=[]
	for i in range(length):
		array.append(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(1,10*length))))
	return array

resultados = []
for i in range(1,6):
	print(i)
	Blockchain.longitud_nonce = i
	for j in range(20):
		array = random_array(j+1)
		init_time = time.time()
		Blockchain.pow(array)
		end_time = time.time()
		resultados.append((i,j,end_time-init_time))
resultados=np.array(resultados)

unq_n, idx_n, counts_n = np.unique(resultados.T[0], return_inverse = True, return_counts = True)
media_nonce = np.bincount(idx_n, weights = resultados.T[2]) / counts_n

#unq_l, idx_l, counts_l = np.unique(resultados.T[1], return_inverse = True, return_counts = True)
#media_long = np.bincount(idx_l, weights = resultados.T[2]) / counts_l

#print(resultados)
print(media_nonce)
#print(media_long)
