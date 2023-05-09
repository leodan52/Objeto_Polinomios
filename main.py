# Descripción

from TOOLS.polinomial import *

def main():

	f = [1,1]
	g = [1, -1]
	h = [-3, 2]
	I = [2, 1, -3]

	g_ = Polinomio(g)
	h_ = Polinomio(h)
	f_ = Polinomio(f)
	I_ = Polinomio(I)

	tupla = (f_, g_, h_, I_)

	print("Sean los polinomios:")
	print(f'f(x) = {f_}')
	print(f'g(x) = {g_}')
	print(f'h(x) = {h_}')
	print(f'I(x) = {I_}')
	print(f'parte del grupo de polinimos de grado n, P_n(x)')

	segundo = ''' Donde se definen las operaciones de suma (+), producto (*) y
composición (&).

Ejemplos:'''
	print(segundo)
	print("Suma de polinomios:\n")

	for i in tupla:
		for j in tupla:
			print(i, "+", j, "=", i + j)
		print()


	print("\nMultiplicación algebraica:\n")

	for i in tupla:
		for j in tupla:
			print(i, "*", j, "=", i * j)
		print()

	print("\nPotencia:\n")

	for poli in tupla:
		for n in (2,3):
			print(poli, "^", n, " = ", poli**n, sep="")
		print()

	print("\nComposición:\n")

	for i in tupla:
		for j in tupla:
			print(i, "&", j, "=", i & j)
		print()

	print("\nCon su conmutador:\n")

	for i in tupla:
		for j in tupla:
			print("[", i, ", ", j, "]", " = ", Polinomio.Conmu(i,j), sep="")
		print()

	print(Polinomio.Identity_composicion() & tupla[0])
	print(Polinomio.Tensor_producto(2,2))

	print("\n\n")
	test = Polinomio([5,4,3])
	base0 = Polinomio([1,0,1])
	base1 = Polinomio([1,0,-1])
	base2 = Polinomio([0,1,2])

	print(f'Sea P = {test} un polinomio representado en la base estandar')
	print(f'Y una base alternativa representada por los polinomios')
	print(f'b1 = {base0}')
	print(f'b2 = {base1}')
	print(f'b3 = {base2}')

	coeficientes = Polinomio.CambioBase(test, base0, base1, base2)
	
	result = coeficientes[0]*base0 + coeficientes[1]*base1 + coeficientes[2]*base2

	print(f'P puede ser representado en la base b de la siguiente manera')
	print(f'P = {coeficientes[0]}*b1 + {coeficientes[1]}*b2 + {coeficientes[2]}*b3')
	print("")
	print(f'Si se realiza las operaciones se obtiene: P = {result}')
	print("")









main()
