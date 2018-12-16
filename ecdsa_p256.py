from fastecdsa import curve, ecdsa, keys


class Ecdsa_p256(object):
	"""
	Implementation of elliptic curve digital signature algorithm p256
	"""
	def __init__(self):
		self.clave_privada = keys.gen_private_key(curve.P256)
		self.clave_publica = keys.get_public_key(self.clave_privada, curve.P256)

	def firma(self, mensaje):
		if len(mensaje) > 0:
			r, s = ecdsa.sign(mensaje, self.clave_privada)
			return ((mensaje,(r,s), self.clave_publica))
		else:
			return (())

	def validacion(self, mensaje):
		m = mensaje[0]
		firma = mensaje[1]
		clave = mensaje[2]

		return ecdsa.verify(firma, m, clave)


