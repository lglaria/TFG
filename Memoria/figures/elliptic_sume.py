import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore",category=RuntimeWarning) #tendremos algunas raices negativas

X = np.linspace(-2.5, 5, 5000)
Y_0 = np.linspace(-10, 10, 5000)


Z = (X**3 - 3*X + 5)**(0.5)
Y = 2*X
plt.plot(X, Z, color = 'black')
plt.plot(X,-Z, color = 'black')
plt.plot(X,2*X)
plt.plot(X,[0]*5000, color = 'red')

dif = Z-Y
dif_ = Z + Y
flag = False
for i in range(len(dif-1)):

	if round(dif[i],3) == 0 and not flag:

		plt.plot(X[i], 2*X[i], 'ro')
		plt.annotate('Q',(X[i], 2*X[i]),xytext=(-10,10), textcoords = 'offset points')
		flag = True
	elif round(dif[i],3) == 0 and flag:
		plt.plot(X[i], 2*X[i], 'ro')
		plt.plot(X[i], -2*X[i], 'ro')
		plt.plot([X[i]]*5000, Y_0,'--')
		plt.annotate('R\'',(X[i], 2*X[i]),xytext=(-10,10), textcoords = 'offset points')
		plt.annotate('R',(X[i], -2*X[i]),xytext=(-10,10), textcoords = 'offset points')

	elif round(dif_[i],3) == 0:
		plt.plot(X[i], 2*X[i], 'ro')
		plt.annotate('P',(X[i], 2*X[i]),xytext=(-10,10), textcoords = 'offset points')


plt.axis('off')
plt.savefig('elliptic.eps', format = 'eps')

plt.show()


