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

main()
