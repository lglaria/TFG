# TFG
##

#Proceso cliente local --> main.py & p2p.py
##Orden de ejecucion servidor blockchain al iniciar (dentro de p2p.py)
###0. Si es la primera ejecucion (esto se comprueba si no hay generados ciertos archivos en sys) se conecta a los nodos predeterminados para pedir direcciones ip de otros nodos
###1. Le pide a los otros nodos su copia de la cadena, aplica los protocolos para elegir la mas extensa, si tiene alguna cadena previa calculada la usa
###2. Comienza a ejecutar

#Para añadir otros clientes basta con copiar el codigo de main.py y modificar el puerto.
