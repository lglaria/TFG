# TFG
##

#Proceso cliente local --> main.py & p2p.py


##Orden de ejecucion servidor blockchain al iniciar (dentro de p2p.py)

###0. Si es la primera ejecucion (esto se comprueba si no hay generados ciertos archivos en sys__por implementar) se conecta a los nodos predeterminados para pedir direcciones ip de otros nodos

###1. Le pide a los otros nodos su copia de la cadena, aplica los protocolos para elegir la mas extensa, si tiene alguna cadena previa calculada la usa

###2. Comienza a ejecutar

#Para añadir otros clientes basta con copiar el codigo de main.py y modificar el puerto.

#Principales archivos:
 
##ecdsa_p256.py implementacion de la firma y validacion para el algoritmo ecdsa (curva p_256) se utiliza la libreria fastecdsa de python.

##blockchain.py implementacion del protocolo blockchain, 

###metodos incluidos: generacion del bloque inicial, algoritmo de prueba de trabajo, validar nuevos bloques, validar cadena, calcular nuevos bloques e incluir un bloque en la cadena.

#Archivo calculos_pow.py no forma parte de la estructura principal, se utiliza en el trabajo para hacer pruebas sobre el metodo de prueba de trabajo implementado
