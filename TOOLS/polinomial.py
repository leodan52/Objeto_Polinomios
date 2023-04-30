
import numpy as np

class Polinomio:

	''' Define un objeto polinomio en forma de serie de potencias. Está definida la suma (+)
la resta (-), el producto (*) y la composición (&)'''

	def __init__(self, lista, ordenDescendente = False):

		self.__vector = np.array(lista).astype(np.float64)
		self.__grado = self.__vector.size - 1
		self.__representacion = ""
		self.__ordenDescendente = ordenDescendente

		self.__toString()

	def __repr__(self):
		return f'( {self.__representacion} )'

	# ------------ Definición de la operaciones del objeto ---------------------------------

	def __add__(self, other):

		if not isinstance(other, Polinomio):
			other = Polinomio.__Nuevo_polinomio([other])

		p1, p2, l = Polinomio.__Igualar_len(self.__vector, other.__vector)
		suma = p1 + p2

		return Polinomio.__Nuevo_polinomio(suma)

	def __radd__(self, other):
		return Polinomio.__Sumar(self, other)

	def __sub__(self, other):
		return Polinomio.__Restar(self, other)

	def __rsub__(self, other):
		return Polinomio.__Restar(self, other)

	def __neg__(self):
		aux = self.__vector.copy()
		aux = (-1)*aux

		return Polinomio.__Nuevo_polinomio(aux)

	def __pos__(self):
		return self

	def __mul__(self, other):

		if not isinstance(other, Polinomio):
			other = Polinomio.__Nuevo_polinomio([other])

		p1, p2, l = Polinomio.__Igualar_len(self.__vector, other.__vector)
		Tensor = Polinomio.Tensor_producto(l,l)
		salida = np.einsum('ijk,j,k -> i',Tensor,p1,p2)

		return Polinomio.__Nuevo_polinomio(salida)

	def __rmul__(self, other):
		return Polinomio.__Multiplicar(self, other)

	def __pow__(self, n_):
		if not isinstance(n_, int):
			raise TypeError(f'El exponente es {type(n_)}. Debe ser int')
		elif n_ < 0:
			raise TypeError(f'El exponente es negativo. Aún no se define')
		elif n_ == 0:
			return Polinomio.One()
		elif n_ == 1:
			return self

		Tensor = Polinomio.Tensor_producto(self.__grado + 1, self.__grado + 1)
		salida = Polinomio.__Nuevo_polinomio(self.__vector.copy())
		m = 1

		while m < n_:
			salida = Polinomio.__Multiplicar(salida, self)
			m += 1

		return salida

	def __and__(self, other):
		m = 0
		salida = 0
		for a in self.__vector:
			aux0 = Polinomio.__Potenciar(other, m)
			aux = Polinomio.__Multiplicar(aux0, a)
			salida = Polinomio.__Sumar(aux, salida)

			m += 1

		return salida

	#----------------- Definición de métodos de extracción de atributos ------------------------------

	def __len__(self):
		return self.__grado

	def __getitem__(self, n):
		try:
			return self.__vector[n]
		except IndexError:
			return 0


	def __setitem__(self, n, nuevo):
		if not isinstance(nuevo, int) and not isinstance(nuevo, float):
			raise TypeError(f'Debe ser un número real, no un {type(nuevo)}')
		try:
			self.__vector[n] = nuevo
		except IndexError:
			aux = np.zeros(n+1)
			self.__vector, aux, ll =  Polinomio.__Igualar_len(self.__vector, aux)
			self.__vector[n] = nuevo

		while self.__vector[-1] == 0:
			self.__vector = np.delete(self.__vector, -1)

		self.__toString()

	def copy(self):
		return Polinomio.__Nuevo_polinomio(self.__vector.copy())

	def OrdenarAscendente(self):

		self.__ordenDescendente = False

		self.__toString()

	def OrdenarDescendente(self):

		self.__ordenDescendente = True

		self.__toString()


	#-------------------------------------------------------

	def __toString(self):

		''' Construye la representación del polinomio '''

		entradas = Polinomio.__Num2strg(self.__vector)
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

		if self.__ordenDescendente:
			salida = "".join(salida[::-1])
		else:
			salida = "".join(salida)

		if salida == "":
			salida = "0"
		elif salida[0] == "+":
			salida = salida[1:]

		salida = salida.replace("+", " + ")
		salida = salida.replace("-", " - ")

		self.__representacion = salida.strip()


	@classmethod
	def __Nuevo_polinomio(cls, lista):

		'''Regresa un objeto del tipo Polinomio. Necesario para definir operaciones. '''

		return cls(lista)

	@classmethod
	def Zero(cls):

		'''Retorna el objeto Polinomio 0, el neutro aditivo '''

		return cls([0])

	@classmethod
	def One(cls):

		'''Regresa el objeto Polinomio 1, la identidad, el neutro multiplcativo '''

		return cls([1.0])

	@classmethod
	def Identity_composicion(cls):

		''' Regresa como objeto Polinomio la identidad o neutro de la composición '''

		return cls([0, 1.0])

	# ---------- Metodos para realizar operaciones dentro del módulo --------------------------------

	@staticmethod
	def __Restar(a, b):
		return a + (-b)

	@staticmethod
	def __Sumar(a, b):
		return a + b

	@staticmethod
	def __Multiplicar(a, b):
		return a*b

	@staticmethod
	def __Potenciar(a, n):
		return a**n

	# ------------------- Métodos para la comparación -------------------------------------------

	def __eq__(self, other):

		if not isinstance(other, Polinomio):
			other = Polinomio.__Nuevo_polinomio([other])

		p1, p2, l = Polinomio.__Igualar_len(self.__vector, other.__vector)


		return all(p1 == p2)

	def __ne__(self, other):
		return not (self == other)


	# ------------------- Métodos estáticos del la clase --------------------------------------

	@staticmethod
	def Conmu(a,b):

		'''Se define el conmutador de la composición '''

		return (a&b)-(b&a)

	@staticmethod
	def __Igualar_len(p1_, p2_):

		''' Iguala la longitud de los vectores numpy para las operaciones '''

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
	def __Num2strg(Array):

		'''Convierte los datos numéricos en strings. Herramienta para la representación '''

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
