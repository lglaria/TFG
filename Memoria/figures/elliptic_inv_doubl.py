import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore",category=RuntimeWarning) #tendremos algunas raices negativas

X = np.linspace(-2.5, 5, 5000)
Y_0 = np.linspace(-10, 10, 5000)

Z = (X**3 - 3*X + 5)**(0.5)
Y = 2*X
plt.plot(X, Z, color = 'black')
plt.plot(X,-Z, color = 'black')

plt.plot(X,[0]*5000, color = 'red')



#curva en implicita: Y**2 -X**3 +3*X -5 = 0
#pendiente de la recta tangente = -parcial_x/parcial y
#-(-3X**2 + 3)/2Y
# (-1, 7**0.5) --> m = 0
#intercept = 5**0.5

pendiente = 0
intercept = float(7**0.5)

Y_line = intercept + pendiente*X

dif = Z-Y_line

flag = False
k = 0
#La funcion de flag y k es no marcar mas de un punto en el mismo entorno, el redondeo hace que dif valga cero en entornos de los puntos de interseccion
for i in range(len(dif-1)):
	
	if round(dif[i],2) == 0 and not flag and k == 0:

		plt.plot(X[i], intercept, 'ro')
		plt.annotate('P',(X[i], intercept),xytext=(-10,10), textcoords = 'offset points')
		plt.plot([X[i]]*5000, Y_0,'--')
		plt.plot(X[i], -intercept, 'ro')
		plt.annotate('-P',(X[i], -intercept),xytext=(-15,-10), textcoords = 'offset points')
		flag = True

	elif round(dif[i],2) == 0 and flag and k >= 150:
		plt.plot(X[i], intercept, 'ro')
		plt.annotate('S',(X[i], intercept),xytext=(-10,10), textcoords = 'offset points')
		plt.plot([X[i]]*5000, Y_0,'--')
		plt.plot(X[i], -intercept, 'ro')
		plt.annotate('2P',(X[i], -intercept),xytext=(-15,-10), textcoords = 'offset points')
		flag = False
	elif flag== True:
		k += 1

plt.plot(X,Y_line)


plt.axis('off')
plt.savefig('elliptic1.eps', format = 'eps')

plt.show()


