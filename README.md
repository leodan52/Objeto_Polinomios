# Objeto_Polinomios

El objeto Polinomio define un polinomio $P$ de la forma

$$ P(x) = a_0  + a_1 x + a_2x² + \cdots + a_{n-1}x^{n-1} + a_n x^n,$$

con $n$ el grado del polinomio y las $a_i$ los coeficientes. El módulo que se encuentra en la ruta `TOOLS/polinomial.py`, trabaja mediante el uso del módulo `scipy`, que se puede instalar usando la orden
> ~~~
> pip install scipy
> ~~~
en la terminal.

## Funcionamiento del módulo

La sintaxis del módulo es muy simple. Comienza definiendo una lista de la siguiente forma,
> ~~~
>  lista = [a0, a1, a2, ...., an]
>  ~~~
donde los elementos de la misma serán los coeficientes del polinomio $a_0$, $a_1$, $a_2$, $\dots$, $a_n$, respectivamente. Esta lista se usará como argumento del constructor
> ~~~
> p = polinomial.Polinomio(lista [, ordenDescendente])
> ~~~
De esta forma el objeto ya está construido.

El parámetro opcional `ordenDescendente` es un booleano que determina el orden en el que se imprime el polinomio, así como el orden de los coeficientes del método `coeficientes()`. Su valor por defecto es `False`

Para el uso de ejemplos en lineas posteriores, conviene definir algunos polinomios específicos. Definamos tres de ellos,

$$
\begin{eqnarray}
	P_1(x) &=& 1+x, \\
	P_2 (x) &=& -3 + 2x^2,\\
	P_3(x) &=& 2 + x -3x^2
\end{eqnarray}
$$

que serán guardadas en las variables `p1`, `p2`y `p3`, respectivamente. Un archivo nombrado `main.py` que contenga estás definiciones comenzaría de las siguiente forma
> ~~~
> import TOOLS.polinomial as *
> 	# Simplificamos el import para facilitar la escritura
>
> def main():
> 	lista1 = [1, 1]
>  	lista2 = [-3, 0, 2]
> 	lista3 = [2, 1, -3]
>
> 	p1 = Polinomio(lista1)
> 	p2 = Polinomio(lista2)
> 	p3 = Polinomio(lista3)
>
> 	print(p1)
> 	print(p2)
> 	print(p3)
>
> if __name__ == "__main__":
> 	main()
>  ~~~
y la salida que mostraría sería
> ~~~
> ( 1 + x )
> ( - 3 + 2x^2 )
> ( 2 + x - 3x^2 )
>~~~
Nótese que para definir `p2` fue necesario usar un cero para el termino lineal, ya que este no aparece en el polinomio.

### Métodos de clase

El objeto Polinomio contiene algunos métodos útiles para extraer o modificar atributos. Considerando los tres polinomios definidos anteriormente, ejemplifiquemos los métodos en el interprete de Python.

#### Orden del polinomio

Para conocer el orden del polinomio se usa el método `len()` como sigue
> ~~~
> >>> len(p2)
> 2
> >>> len(p1)
> 1
> ~~~
recordando que el orden del polinomio lo define el exponente mayor que posea la variable, en este caso $x$.

#### Obtener un coeficiente

Para obtener el coeficiente un término se usa el método `p[n]`, donde `n` es el grado del término del que pertenece dicho coeficiente. Por ejemplo,
> ~~~
> >>> p1[0]
> 1.0
> >>> p2[1]
> 0.0
> >>> p3[2]
> -3.0
> ~~~
cabe destacar que sí el polinomio no posee un coeficiente del grado indicado, retornará cero.

#### Modificar o añadir un término

Para modificar o añadir un termino solo se debe asignar el valor del coeficiente al término con el grado deseado. Por ejemplo,
> ~~~
> >>> p3
> ( 2 + x - 3x^2 )
> >>> p3[1] = -7
> >>> p3
> ( 2 - 7x - 3x^2 )
> ~~~
O bien,
> ~~~
> >>> p2
> ( - 3 + 2x^2 )
> >>> p2[3] = -13
> >>> p2
> ( - 3 + 2x^2 - 13x^3 )
> ~~~

#### Clonar polinomio

 Para copiar un polinomio y usarlo después, se puede usar el método `copy()`, como por ejemplo,
 > ~~~
> >>> p4 = p1.copy()
> >>> p4
> ( 1 + x )
> >>> p4[3] = -1
> >>> p4
> ( 1 + x - x^3 )
> >>> p1
> ( 1 + x )
 > ~~~
 de esta forma se puede modificar el nuevo polinomio, sin modificar al original.

#### Evaluar un polinomio

Evalúa el polinomio en un punto dado. Por ejemplo,
> ~~~
> >>> p1.evaluar(0)
> >>> 1
> ( 1 + x )
> >>> p4.evaluar(2)
> >>> -5
> ( 1 + x - x^3 )
> ~~~

#### Coeficientes

Regresa una lista con los coeficientes del polinomio, el orden de la lista es afectado por el valor de `ordenDescendente`. Por ejemplo,
> ~~~
> >>> p1.coeficientes()
> >>> [1, 1]
> ( 1 + x )
> >>> p2.coeficientes()
> >>> [-3, 0, 2]
> ( - 3 + 2x^2 )
> ~~~

#### Ordenación del polinomio
El orden del polinomio se puede modificar de diferentes maneras, como por ejemplo usando el metodo `OrdenarAscendente()` que establece el valor de `ordenDescendente` en `False`.

O el metodo `OrdenarDescendente()` que establece su valor en `True`

Alternativamente se puede usar la propiedad `ordenDescendente` para leer o establecer directamente su valor, por ejemplo,
> ~~~
> >>> p2.coeficientes()
> >>> [-3, 0, 2]
> >>> p2.ordenDescendente = True
> >>> p2.coeficientes()
> >>> [2, 0, -3]
> ~~~

### Comparación de polinomios

Las comparaciones de polinomios definidas son las de igualdad. Ya que el conjunto de polinomios no es ordenable, es imposible fijar las operaciones $>$ y $<$, por lo que se dejaron de lado. Dicho esto, veamos algunos ejemplos,
> ~~~
> >>> p1 == p2
> False
> >>> p2 == p2
> True
> >>> p1 != p3
> True
> >>> p3 != p3
> False
> ~~~
El criterio para la `==` es que ambos polinomios tengan exactamente los mismos coeficientes.

### Operaciones con polinomios

#### Suma y resta

La **suma** o adición de polinomios es sencilla, ya que se realiza entre términos del mismo grado. Veamos algunos ejemplos en el interprete de Python,
> ~~~
> >>> p1 + p2
> ( - 2 + x + 2x^2 )
> >>> p2 + p3
> ( - 1 + x - x^2 )
> >>> p1 + p3
> ( 3 + 2x - 3x^2 )
> ~~~
el resultado de la operación también es un objeto Polinomio. También es posible sumar un dato numérico, ya sea `int` o `float` con un Polinomio,
> ~~~
> >>> p1 + 2
> ( 3 + x )
> >>> 8 + p2
> ( 5 + 2x^2 )
> >>> p3 + 2.5
> ( 4.5 + x - 3x^2 )
El dato numérico será considerado como un polinomio de grado 0.

La **resta** o sustracción de polinomios es bastante similar, ya que el módulo también ha definido el inverso aditivo de la siguiente forma,
> ~~~
> >>> -p1
> ( - 1 - x )
> >>> -p2
> ( 3 - 2x^2 )
> ~~~
por lo que la resta se define, tal y como se hace en matemáticas, como la suma de un inverso aditivo. Dicho esto, veamos algunos ejemplos,
> ~~~
> >>> p1 - p2
> ( 4 + x - 2x^2 )
> >>> p2 - p3
> ( - 5 - x + 5x^2 )
> >>> 11 - p3
> ( - 9 + x - 3x^2 )

#### Producto

El producto o multiplicación de polinomios es más complejo que su suma y su resta. No nos vamos a detener a explicar los procedimientos que tienen la multiplicación algebraica, por lo que se supondrá que el usuario entiende y domina dichos procedimientos. Por lo tanto, vamos directo a los ejemplos.

Por regla general, el resultado de un producto de polinomios tiene un grado igual o mayor a los originales,
> ~~~
> >>> p1 * p2
> ( - 3 - 3x + 2x^2 + 2x^3 )
> >>>   p2 * p3
> ( - 6 - 3x + 13x^2 + 2x^3 - 6x^4 )
> >>> p1 * p3 * p3
> ( - 6 - 9x + 10x^2 + 15x^3 - 4x^4 - 6x^5 )
> ~~~
Los tres polinomios definidos son de grado 1, para `p1`, y grado 2 para los demás, por lo que la regla se cumple, además hacer un producto múltiple es posible. Adicionalmente, también podemos multiplicar una variable numérica por un Polinomio,
> ~~~
> >>> 3 * p1
> ( 3 + 3x )
> >>>   2.5 * p2
> ( - 7.5 + 5x^2 )
> >>> p3 * 0.5
> ( 1 + 0.5x - 1.5x^2 )
> ~~~
tanto por la izquierda como por la derecha.

#### Composición

En general, la **composición** de dos funciones, $f(x)$ y $g(x)$, se define como

$$ (f \circ g)(x) = f\left(g(x)\right),$$

donde la función resultante se denomina *función compuesta*. La composición es una operación algebraica que puede aplicarse también a los polinomios.

Infortunadamente, el operador de la composición $\circ$,  no está definido en Python, por lo que se estará sobrecargando el operador `&` para este propósito. Dicho esto, aquí algunos ejemplos de composición,

> ~~~
> >>> p1 & p2
> ( - 2 + 2x^2 )
> >>> p2 & p3
> ( 5 + 8x - 22x^2 - 12x^3 + 18x^4 )
> ~~~
A diferencia de la suma y el producto, la composición no es conmutativa, es decir, el resultado cambiará al invertir el orden de la operación,
> ~~~
> >>> p1 & p3
> ( 3 + x - 3x^2 )
> >>> p3 & p1
> ( - 5x - 3x^2 )
> ~~~

Al no ser una operación conmutativa, es posible definir también su conmutador[^1],
> ~~~
> >>> Polinomio.Conmu(p1, p2)
> ( - 1 - 4x )
> >>> Polinomio.Conmu(p2, p3)
> ( 33 + 8x - 60x^2 - 12x^3 + 30x^4 )
> >>> Polinomio.Conmu(p1, p3)
> ( 3 + 6x )
> ~~~
Ya que es un método estático, lo debe anteceder siempre el nombre de la clase.

#### Jerarquía de operaciones

La jerarquía de las operaciones básicas es la misma que viene definida en Python: paréntesis, multiplicación, suma (y resta). El problema viene con la composición, qué matemáticamente tiene prioridad antes de la suma y resta, pero que al relacionarla al operador `&`, esto se invierte. En otras palabras, para siempre obtener los resultados esperados, hay que considera el orden como: paréntesis, multiplicación, suma (y resta) y al final composición.

#### Cambio de base

Los polinomios, junto con la suma de polinomios y la multiplicación por un escalar, pueden entenderse como un espacio vectorial y por ende puede ser definida una base de polinomios que generen todo el espacio. Por ejemplo.

Tomemos el conjunto de todos los polinomios de rango 2, estos polinomios tienen la forma

$$ P_2(x) = a_0  + a_1 x + a_2x² $$

Si tomamos como base los polinomios:

$$
\begin{eqnarray}
	\epsilon_1(x) &=& 1, \\
	\epsilon_2 (x) &=& x,\\
	\epsilon_3(x) &=& x^2
\end{eqnarray}
$$

Podemos ver que el polinomio $P_2(x)$ es una combinación lineal de esta base, pudiendo ser representado por el vector 

$$ P_2 = [a_0, a_1, a_2]$$
___

[^1]:  Commutator, Wikipedia, <https://en.wikipedia.org/wiki/Commutator>
