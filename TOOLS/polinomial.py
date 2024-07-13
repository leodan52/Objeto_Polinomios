
import numpy as np
import scipy.integrate as integrate
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
		return f'{self.__representacion}'

	# ------------ Definición de las operaciones del objeto ---------------------------------

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

	def evaluar(self, x):
		salida = 0

		for exponente in range(self.__grado + 1):
			salida += self.__vector[exponente]*(x**exponente)

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

	def coeficientes(self):
		''' Retorna una lista con los coeficientes del polinomio en el orden establecido por "ordenDescendente" '''
		return [coef for coef in (self.__vector if not self.__ordenDescendente else self.__vector[::-1])]

	def obtenerOrdenDescendente(self):
		''' Permite obtener el valor de "ordenDescendente" '''
		return self.__ordenDescendente

	def establecerOrdenDescendente(self, descendente):
		''' Permite establecer el valor de "ordenDescendente" '''
		self.__ordenDescendente = descendente
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

	def __lt__(self, other):
		return self.__vector[0] < other.__vector[0]


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

	@staticmethod
	def CambioBase(poli, *base):
		''' Retorna los coeficientes de la combinacion lineal que representa al polinomio "poli" en la base "base" '''
		gradoPolinomio = len(poli)
		gradoBase = 0

        # Obtiene el grado de la base como el mayor grado entre polinomios de la base
		for vector in base:
			if len(vector) > gradoBase:
				gradoBase = len(vector)

		# El grado del polinomio debe de ser igual o menor que el de la base
		if gradoPolinomio > gradoBase:
			raise ValueError("El grado de la base debe de ser igual o mayor que el del polinomio")


		estandar2base = np.zeros((gradoBase + 1, len(base))) # Matriz que transforma de la base estandar a la nueva base
		coefPolinomio = poli.coeficientes() if not poli.ordenDescendente else poli.coeficientes()[::-1]

		# Llena los coeficientes con cero si el rango del polinomio es menor que el de la base,
		#  necesario para hacer la multiplicacion matricial
		candidato = np.zeros(gradoBase + 1)
		candidato[: len(coefPolinomio)] = coefPolinomio

		# Llena la matriz de transformacion
		for i in range(len(base)):
			coef = base[i].coeficientes()
            # Si el vector está en orden descendente lo "voltea"
			if base[i].ordenDescendente:
				coef = coef[::-1]

			estandar2base[: len(coef), i] = coef

		# Matriz que transforma de la base nueva a la base estandar
		base2estandar = np.linalg.inv(estandar2base) # Solo invierte la matriz
		newCoef = np.matmul(base2estandar, candidato) # Realiza la multiplicacion matricial

		return newCoef.tolist() # Regresa los datos como una lista de numeros.


	@staticmethod
	def ortogonalizar( base, normalizar=False, productoInterno=lambda a, b: Polinomio.productoInternoIntegral(a, b) ):
		''' Regresa un conjunto de polinomios ortogonales a partir de una base dada '''

		# El primer elemento de la nueva base es el mismo que el de la original
		nuevaBase = [base[0]]

        #Procedimiento de Gram-Schmidt
		for i in range(1, len(base)):
			candidato = base[i]
			# Calcula la proyeccion de los polinomios de la base sobre la nueva base
			for j in range(i):
				candidato -= Polinomio.__proj(nuevaBase[j], base[i], productoInterno)

			nuevaBase.append(candidato) # Añade el nuevo polinomio calculado

		# Normaliza la base en caso de ser necesario
		if normalizar:
			nuevaBase = [base * (1/productoInterno(base, base))**(1/2) for base in nuevaBase]

		return nuevaBase


	# Regresa el valor del producto interno entre dos polinomios de la forma < 'p' , 'q' > = ∫p(x)q(x)w(x)dx
	# desde 'limiteInferior' hasta 'limiteSuperior', tanto los limites de integracion
	# como la funcion de poderacion son editables
	@staticmethod
	def productoInternoIntegral( p, q, limiteInferior=-1, limiteSuperior=1, ponderacion=lambda x: 1 ):
		''' Calcula el producto interno entre polinomios con la definicion integral '''
		polinomioInterno = p * q # p(x)q(x)

		# Integra p(x)q(x)w(x) entre los limites dados
		resultado = integrate.quad(
            lambda x: polinomioInterno.evaluar(x) * ponderacion(x),
            limiteInferior,
            limiteSuperior,
        )

		# La funcion quad de scipy regresa un tupla con dos valores: la integral y el error, regresa solo la integral
		return resultado[0]

	# Metodo para uso interno del modulo, usado en ortogonalizar()
	@staticmethod
	def __proj(u, v, producto):
		''' Calcula la proyeccion del vector v sobre el vector u usando el producto interno dado '''
		return u * (producto(v, u) / producto(u, u))
