# Descripcion

import numpy as np

class Polinomio:

	def __init__(self, lista):

		''' Define un objeto polinomio en forma de serie de potencias. Está definida la suma (+)
la resta (-), el producto (*) y la composición (&)'''

		self.p = np.array(lista).astype(np.float64)
		self.n = len(lista)
		self.grado = self.p.size - 1
		self.representacion = ""

		self.Representacion()

	def __repr__(self):
		return f'( {self.representacion} )'

	# Definición de la operaciones del objeto

	def __add__(self, other):

		if not isinstance(other, Polinomio):
			other = Polinomio.Nuevo_polinomio([other])

		p1, p2, l = Polinomio.Igualar_len(self.p, other.p)
		suma = p1 + p2

		return Polinomio.Nuevo_polinomio(suma)

	def __radd__(self, other):
		return Polinomio.Suma(self, other)

	def __sub__(self, other):
		return Polinomio.Resta(self, other)

	def __rsub__(self, other):
		return Polinomio.Resta(self, other)

	def __neg__(self):
		aux = self.p.copy()
		aux = (-1)*aux

		return Polinomio.Nuevo_polinomio(aux)

	def __pos__(self):
		return self

	def __mul__(self, other):

		if not isinstance(other, Polinomio):
			other = Polinomio.Nuevo_polinomio([other])

		p1, p2, l = Polinomio.Igualar_len(self.p, other.p)
		Tensor = Polinomio.Tensor_producto(l,l)
		salida = np.einsum('ijk,j,k -> i',Tensor,p1,p2)

		return Polinomio.Nuevo_polinomio(salida)

	def __rmul__(self, other):
		return Polinomio.Producto(self, other)

	def __pow__(self, n_):
		if not isinstance(n_, int):
			raise TypeError(f'El exponente es {type(n_)}. Debe ser int')
		elif n_ < 0:
			raise TypeError(f'El exponente es negativo. Aún no se define')
		elif n_ == 0:
			return Polinomio.Identity_producto()
		elif n_ == 1:
			return self

		Tensor = Polinomio.Tensor_producto(self.n, self.n)
		salida = Polinomio.Nuevo_polinomio(self.p.copy())
		m = 1

		while m < n_:
			salida = Polinomio.Producto(salida, self)
			m += 1

		return salida

	def __and__(self, other):
		m = 0
		salida = 0
		for a in self.p:
			aux0 = Polinomio.Potencia(other, m)
			aux = Polinomio.Producto(aux0, a)
			salida = Polinomio.Suma(aux, salida)

			m += 1

		return salida

	# Definición de métodos de extración de atributos

	def __len__(self):
		return self.grado

	def __getitem__(self, n):
		try:
			return self.p[n]
		except IndexError:
			return 0


	def __setitem__(self, n, nuevo):
		if not isinstance(nuevo, int) and not isinstance(nuevo, float):
			raise TypeError(f'Debe ser un número real, no un {type(nuevo)}')
		try:
			self.p[n] = nuevo
		except IndexError:
			aux = np.zeros(n+1)
			self.p, aux, ll =  Polinomio.Igualar_len(self.p, aux)
			self.p[n] = nuevo

		while self.p[-1] == 0:
			self.p = np.delete(self.p, -1)

		self.Representacion()

	def copy(self):
		return Polinomio.Nuevo_polinomio(self.p.copy())

	#-------------------------------------------------------

	def Representacion(self):

		# Construye la representación del objeto

		entradas = Polinomio.Nume2strs(self.p)
		salida = []
		m = 0

		for termino in entradas:
			if termino in ["+1", "-1"] and m != 0:
				termino = termino.replace("1", "")

			if termino == "+0":
				pass
			elif m == 0:
				salida.append(termino)
			elif m == 1:
				aux = f'{termino}x'
				salida.append(aux)
			else:
				aux = f'{termino}x^{m}'
				salida.append(aux)
			m += 1

		salida = "".join(salida)

		if salida == "":
			salida = "0"
		elif salida[0] == "+":
			salida = salida[1:]

		salida = salida.replace("+", " + ")
		salida = salida.replace("-", " - ")

		self.representacion = salida.strip()


	@classmethod
	def Nuevo_polinomio(cls, lista):

		# Regresa un objeto del tipo Polinomio. Necesario para definir operaciones.

		return cls(lista)

	@classmethod
	def Zero(cls):

		# Regresa el objeto Polinomio 0, el neutro aditivo

		return cls([0])

	@classmethod
	def Identity_producto(cls):

		# Regresa el objeto Polinomio 1, la identidad, el neutro multiplcativo

		return cls([1.0])

	@classmethod
	def Identity_composicion(cls):

		# Regresa como objeto Polinomio la identidad o neutro de la composición

		return cls([0, 1.0])

	# Metodos para realizar operaciones dentro del módulo

	@staticmethod
	def Resta(a, b):
		return a + (-b)

	@staticmethod
	def Suma(a, b):
		return a + b

	@staticmethod
	def Producto(a, b):
		return a*b

	@staticmethod
	def Potencia(a, n):
		return a**n

	# Métodos para la comparación

	def __eq__(self, other):

		if not isinstance(other, Polinomio):
			other = Polinomio.Nuevo_polinomio([other])

		p1, p2, l = Polinomio.Igualar_len(self.p, other.p)


		return all(p1 == p2)

	def __ne__(self, other):
		return not (self == other)


	# ---------------------------------------------------------------------------

	@staticmethod
	def Conmu(a,b):

		# Se define el conmutador de la composición

		return (a&b)-(b&a)

	@staticmethod
	def Igualar_len(p1_, p2_):

		# Iguala la longitud de los vectores numpy para las operaciones

		p1 = p1_.copy()
		p2 = p2_.copy()

		l1 = len(p1)
		l2 = len(p2)

		while l1 != l2:
			if l1 > l2:
				p2 = np.append(p2, 0)
				l2 += 1
			elif l1 < l2:
				p1 = np.append(p1, 0)
				l1 += 1

		return p1, p2, len(p1)


	@staticmethod
	def Nume2strs(Array):

		# Convierte los datos númericos en strings. Herramienta para la representación

		salida = []
		for i in Array:
			delta = abs(i - int(i))

			if i >= 0:
				signo = "+"
			else:
				signo = ""

			if delta == 0.0:
				salida.append(signo + str(int(i)))
			else:
				salida.append(signo + str(i))
		return salida

	@staticmethod
	def Tensor_producto(jj,kk):

		''' Contruye el tensor de jj x kk que define el producto polinomial '''

		tensor = np.zeros((jj + kk -1, jj, kk))

		for i in range(jj + kk -1):
			for j in range(jj):
				for k in range(kk):
					if i == j + k:
						tensor[i,j,k] = 1
		return tensor
