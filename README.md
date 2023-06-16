
# Tercer Proyecto de Diseño y Análisis de Algoritmos


## Carlos Carret Miranda C-412

<!-- ###Enunciado del problema -->

### Raul el Incongruente

Raul últimamente quiere impresionar a su novia Daniela, para esto va usar sus habilidades matemáticas, ya que Daniela tiene varias amigos en la facultad y puede apreciar las peripecias de Raul. Raul le pedirá a cada uno de los n amigos matemáticos de Daniela que le diga 2 numeros a_i, b_i, el segundo mayor o igual que el primero.

Ahora Raul va a efectuar su acto de alta pericia Matemática sin la ayuda siquiera de calculadora, Raul dirá un número entero x, tal que para todos los pares dichos por los amigos de Daniela, x no será congruente a_i módulo b_i.

### Descripción del problema

El problema de "Raúl el Incongruente" consiste en encontrar un número entero x que no sea congruente con ninguno de los pares (a_i, b_i) módulo b_i, donde a_i y b_i son dos números enteros dados y el segundo número es mayor o igual que el primero.

Para resolver el problema "Raúl el Incongruente", se deben tener en cuenta los siguientes aspectos:

* Raúl debe encontrar un número entero x que no sea congruente con ningún par (a_i, b_i) proporcionado por los amigos de Daniela.
* La congruencia se define como la relación en la que dos números tienen el mismo resto al dividirse por un número fijo (módulo). Por lo tanto, x debe ser diferente de cada a_i módulo b_i.
* Raúl tiene que encontrar una estrategia que le permita encontrar un valor de x que cumpla con la condición dada para todos los pares de números proporcionados por los amigos de Daniela.
* Dado que Raúl tiene que hacerlo sin la ayuda de una calculadora, es probable que necesite utilizar algún tipo de algoritmo o método matemático que le permita encontrar un número que cumpla con la condición dada de manera eficiente.

#### Ideas para atacar al problema
* Primeramente buscamos si existe algun problema que se pueda transformar o reducir al nuestro.
* Luego se busca dar solución al problema mediante la recursividad y fuerza bruta. Con esto buscamos resolver el problema para obtener resultados lo suficientemente correctos para luego compararlos con otras soluciones que sean mejores.
* Despues se buscara alguna metaheuristica para encontrar mas rapidamente la solucion del algoritmo que resolvera de nuestro problema.
* En caso de poder encontrar una solucion mas eficiente, procedemos a realizar las modificaciones necesarias al algoritmo de fuerza bruta o a la creacion de un nuevo algoritmo.

Este problema implica utilizar habilidades matemáticas avanzadas para encontrar una solución de manera eficiente, ya que el número de pares puede ser muy grande. Además, se requiere una comprensión sólida de la teoría de congruencia y aritmética modular para abordar el problema.

#### Congruencia y Teorema Chino del Resto
La congruencia es una relación entre dos números enteros que se basa en la divisibilidad. Dos números enteros a y b se dicen congruentes módulo n si la diferencia a - b es divisible por n, es decir:

a ≡ b (mod n) ⇔ n | (a - b)

Por ejemplo, 7 ≡ 2 (mod 5) ya que 7 - 2 = 5, que es divisible por 5.

En el problema de "Raúl el Incongruente", se busca un número entero x que no sea congruente con ningún a_i módulo b_i. Esto significa que para cada par (a_i, b_i), no existe ningún número entero k tal que:

x ≡ a_i + k * b_i (mod b_i)

Es decir, que el resto de la división de x entre b_i no sea igual al de a_i.

Una estrategia común para resolver este problema es aplicar el Teorema Chino del Resto, que establece que si tenemos un sistema de congruencias lineales de la forma:

x ≡ a_1 (mod n_1)
x ≡ a_2 (mod n_2)
...
x ≡ a_k (mod n_k)

donde los módulos n_1, n_2, ..., n_k son coprimos entre sí (es decir, no tienen factores comunes), entonces existe una única solución para x módulo N = n_1 * n_2 * ... * n_k.

En el problema de "Raúl el Incongruente", los módulos b_i no necesariamente son coprimos entre sí, por lo que es necesario encontrar una estrategia diferente para encontrar un número x que cumpla con las condiciones requeridas. Una posible solución es utilizar el Teorema Chino del Resto de forma recursiva para construir un número que no sea congruente módulo los b_i, pero este enfoque puede ser complejo y requiere de un conocimiento avanzado de la teoría de congruencia y aritmética modular.

#### TCR
Supongamos que tenemos dos pares (a_1, b_1) y (a_2, b_2) y queremos encontrar un número entero x que no sea congruente con ninguno de los dos pares módulo sus respectivos b_i. Primero, podemos aplicar el Teorema Chino del Resto para encontrar un número entero y que satisfaga las siguientes congruencias:

y ≡ a_1 (mod b_1)
y ≡ a_2 - 1 (mod b_2)

Es decir, que el número y tenga como resto a_1 módulo b_1 y como resto a_2 - 1 módulo b_2. Esto se puede hacer utilizando el algoritmo del Teorema Chino del Resto para dos congruencias.

Luego, podemos construir el número x = y + b_1 * b_2 y comprobar que x no es congruente con ninguno de los dos pares módulo sus respectivos b_i. Esto se puede demostrar utilizando la siguiente propiedad de la congruencia:

Si a ≡ b (mod n) entonces a + kn ≡ b (mod n) para cualquier entero k.

Por lo tanto, tenemos que:

x = y + b_1 * b_2 ≡ a_1 + kb_1 + b_1 * b_2 ≡ a_1 (mod b_1)

y

x = y + b_1 * b_2 ≡ a_2 - 1 + kb_2 + b_1 * b_2 ≡ a_2 - 1 (mod b_2)

Para generalizar este método a más de dos pares, podemos aplicar el Teorema Chino del Resto de forma recursiva. Supongamos que tenemos n pares (a_i, b_i) y queremos encontrar un número x que no sea congruente con ninguno de los pares módulo sus respectivos b_i. Podemos aplicar el Teorema Chino del Resto para los primeros dos pares, lo que nos dará un número y que cumple con las siguientes congruencias:

y ≡ a_1 (mod b_1)
y ≡ a_2 - 1 (mod b_2)

Luego, podemos aplicar el mismo proceso para los pares restantes, es decir, encontramos un número z que cumple con las siguientes congruencias:

z ≡ a_3 (mod b_3)
z ≡ a_4 - 1 (mod b_4)
...
z ≡ a_n - 1 (mod b_n)

Finalmente, podemos construir el número x = y + k * b_1 * b_2 + l * b_1 * b_2 * b_3 * ... * b_n, donde k y l son enteros suficientemente grandes, para que x no sea congruente con ninguno de los pares módulo sus respectivos b_i.

Este método es efectivo para resolver el problema de "Raúl el Incongruente" para cualquier número de pares de números enteros, pero puede ser computacionalmente costoso para grandes valores de n.

#### TCR y Euclides
<!--
El TCR establece que si tenemos un conjunto de congruencias lineales como:

x ≡ a_1 (mod n_1)
x ≡ a_2 (mod n_2)
...
x ≡ a_k (mod n_k)

Donde n_1, n_2, ..., n_k son coprimos entre sí, entonces existe una única solución para x módulo N = n_1 * n_2 * ... * n_k.
-->
Para aplicar el TCR de manera recursiva, se puede dividir el conjunto original de congruencias en subconjuntos de congruencias con módulos coprimos. Para ello, se puede utilizar el algoritmo de Euclides para encontrar el máximo común divisor (MCD) entre dos módulos:

1. Si n_1 y n_2 son coprimos, entonces se puede aplicar el TCR directamente para encontrar una solución a las congruencias:

x ≡ a_1 (mod n_1)
x ≡ a_2 (mod n_2)

2. Si n_1 y n_2 no son coprimos, se puede utilizar el algoritmo de Euclides para encontrar el MCD d = gcd(n_1, n_2), y expresar d como una combinación lineal de n_1 y n_2:

d = r * n_1 + s * n_2

3. Si a_1 y a_2 no son congruentes módulo d, entonces el sistema de congruencias no tiene solución. En caso contrario, se puede utilizar el TCR para resolver las siguientes congruencias:

x ≡ a_1 (mod d)
x ≡ a_2 (mod d)

4. Una vez encontrada la solución x = b módulo d, se puede construir una solución para el sistema original de congruencias utilizando la fórmula:

x ≡ b (mod d * lcm(n_1/d, n_2/d))

Donde lcm(n_1/d, n_2/d) es el mínimo común múltiplo entre n_1/d y n_2/d.

Este proceso se puede repetir de manera recursiva para resolver sistemas de congruencias con módulos que no son coprimos entre sí. Al final, se obtendrá una solución única para el sistema original de congruencias.

En el problema de "Raúl el Incongruente", se puede utilizar este enfoque para encontrar un número entero x que no sea congruente con ningún a_i módulo b_i. Primero, se deben dividir los pares (a_i, b_i) en subconjuntos de pares con módulos coprimos, y luego aplicar el TCR de manera recursiva para encontrar un número x que cumpla con las condiciones requeridas.

### Reduccion, encontrando y demostrando que el problema es NP-Completo

Luego de haber analizado por un tiempo considerable nuestro problema, se pudo notar cierto parecido al problema de satisfacibilidad, en especial 3-satisfacibilidad(3SAT). Se pudo notar esto porque nuestro problema es practicamente un problema de incongruencias simultaneas.

Dada una fórmula 3-SAT $\phi$ con $n$ variables y $m$ cláusulas, construimos un sistema de in-congruencias $I$ de la siguiente manera:

1. Representamos cada variable en $\phi$ como un número primo distinto. Por ejemplo, si $x_i$ es una variable, la representamos con el $i$-ésimo número primo $p_i$. Para ello tendremos que encontrar $n$ enteros relativamente primos $p_{1},...,p_{n} \geq 2$ de tamaño polinómico (por ejemplo, los primeros $n$ primos).

2. Para cada cláusula $C_j$ en $\phi$, creamos una in-congruencia de la forma:

$$\prod_{x_i \in C_j} p_i \equiv 1 \pmod{N_j}$$

donde $N_j$ es el producto de todos los números primos correspondientes a las variables en $C_j$, negadas o no. Cada cláusula que involucra $p_{i},p_{j},p_{k}$ corresponde a un valor prohibido de $x$ mod $p_{i}p_{j}p_{k}$ a través del teorema del resto chino.  En otras palabras, 

$$N_j = \prod_{x_i \in C_j} p_i \prod_{\neg x_i \in C_j} p_i$$

Por ejemplo, supongamos que tenemos la cláusula $C = (x_1 \lor \neg x_2 \lor x_3)$. Representamos las variables como primos $p_1$, $p_2$ y $p_3$ y las negaciones como $q_2$. Entonces tenemos: 

$$N_C = p_1 q_2 p_3 = p_1 p_2 p_3$$

y la in-congruencia es:

$$p_1 \cdot q_2 \cdot p_3 \equiv 1 \pmod{p_1 \cdot q_2 \cdot p_3}$$

3. El sistema de in-congruencias $I$ consiste en las in-congruencias creadas para cada cláusula en $\phi$.

Ahora mostramos que $\phi$ es satisfacible si y solo si $I$ tiene una solución simultánea.

$(\Rightarrow)$ Supongamos que $\phi$ es satisfacible. Entonces existe una asignación de valores verdadero/falso a las variables en $\phi$ que satisface todas las cláusulas. Sea $S$ el conjunto de variables que se establecen en verdadero en esta asignación. Para cada cláusula $C_j$ en $\phi$, sea $N_j$ el producto de primos correspondientes a variables en $C_j$ que no están en $S$. Entonces podemos elegir un elemento $t_j \in \mathbb{Z}_{N_j}$ tal que $\prod_{x_i \in C_j, x_i \in S} p_i \cdot \prod_{\neg x_i \in C_j, x_i \notin S} p_i \cdot t_j \equiv 1 \pmod{N_j}$. Sea $T$ el conjunto de todos los valores $t_j$. Entonces tenemos una solución simultánea para $I$ en la que cada variable $p_i$ se establece en 1 si y solo si $x_i \in S$, y $p_i$ se establece en 0 en caso contrario. Observa que cada in-congruencia en $I$ corresponde a una cláusula en $\phi$, y la in-congruencia se satisface con los valores asignados a las variables en la cláusula.

$(\Leftarrow)$ Supongamos que $I$ tiene una solución simultánea. Sea $S$ el conjunto de variables correspondientes a los primos que se establecen en 1 en la solución, y sea $S'$ el conjunto de variables correspondientes a los primos que se establecen en 0. Afirmamos que $S$ satisface todas las cláusulas en $\phi$. Supongamos por contradicción que existe una cláusula $C_j$ tal que ninguna variable en $C_j$ está en $S$. Entonces el producto de primos correspondientes a variables en $C_j$ que no están en $S$ no es divisible por ningún primo correspondiente a una variable en $C_j$ que está en $S$. Esto contradice el hecho de que la in-congruencia correspondiente a $C_j$ se satisface con la solución simultánea. Por lo tanto, $S$ satisface todas las cláusulas en $\phi$, y por lo tanto, $\phi$ es satisfacible.

Esto completa la prueba de que 3-SAT se reduce al problema de In-Congruencia Simultánea.

### Solucion de Fuerza Bruta
Para resolver el problema "Raúl el Incongruente", se podría seguir el siguiente procedimiento:

1. Leer los pares de números (a_i, b_i) proporcionados por los amigos de Daniela.
2. Identificar el número más grande, digamos M, que se encuentra entre todos los valores de b_i dados por los amigos de Daniela.
3. Comenzar a probar valores enteros positivos para x, empezando por x = M + 1.
4. Para cada valor de x, verificar si es congruente con alguno de los pares (a_i, b_i) proporcionados. Esto se puede hacer verificando si el residuo de x al dividirlo por b_i es igual a a_i para cada par (a_i, b_i).
5. Si se encuentra algún par (a_i, b_i) para el cual x es congruente, pasar al siguiente valor de x y repetir el paso 4.
6. Si para todos los pares (a_i, b_i) proporcionados, x no es congruente, entonces se ha encontrado un valor de x que cumple la condición dada.

Es importante destacar que este método no es el más eficiente para encontrar la solución, especialmente si los números b_i son muy grandes. En ese caso, se pueden utilizar otros métodos más avanzados, como el teorema chino del resto o el algoritmo de Euclides extendido, que permiten encontrar una solución más rápida y eficiente.

#### Rango de valores de x
El rango de valores que se deben probar para x en el problema depende de los valores de los pares (a_i, b_i) proporcionados por los amigos de Daniela.

En general, se puede decir que el valor de x debe ser mayor que el máximo valor de b_i proporcionado por los amigos de Daniela. Esto se debe a que si x es menor o igual que algún valor de b_i, entonces x podría ser congruente con algún a_i módulo b_i, lo que violaría la condición dada en el problema.

Por lo tanto, una forma de determinar el rango de valores a probar para x es encontrar el valor más grande de b_i proporcionado por los amigos de Daniela y sumarle 1. Este valor se puede denotar como M, y se puede utilizar como el valor inicial de x a probar. A partir de ahí, se pueden probar valores enteros positivos para x, comenzando por x = M + 1, y verificar si se cumple la condición dada para todos los pares (a_i, b_i) proporcionados.

Cabe destacar que este método no garantiza que se encuentre el valor más pequeño de x que cumple la condición dada, pero sí garantiza que se encontrará al menos uno. Si se desea encontrar el valor más pequeño de x que cumple la condición dada, se pueden utilizar métodos más avanzados, como el teorema chino del resto o el algoritmo de Euclides extendido.

#### Valores maximos de x
Sin embargo, en general, se puede decir que el valor máximo que tomaría x es un valor arbitrariamente grande. Esto se debe a que no existe un límite superior conocido para los enteros, y por lo tanto, no se puede decir con certeza cuál sería el valor máximo de x necesario para garantizar que se cumple la condición dada para todos los pares (a_i, b_i) proporcionados.

En la práctica, se suele encontrar una solución para un valor de x razonablemente pequeño, especialmente si los valores de b_i proporcionados por los amigos de Daniela no son muy grandes. Si los valores de b_i son muy grandes, se pueden utilizar algoritmos más avanzados para encontrar una solución más eficiente.

En nuestro caso, el valor máximo que tomará x depende de los valores de los pares (a_i, b_i) proporcionados por los amigos de Daniela. Para determinar este valor máximo, se puede utilizar el teorema chino del resto.

<!--
El teorema chino del resto establece que si tenemos un sistema de ecuaciones lineales congruentes de la forma:

x ≡ a_1 (mod b_1)
x ≡ a_2 (mod b_2)
...
x ≡ a_n (mod b_n)

donde b_1, b_2, ..., b_n son números coprimos entre sí (es decir, no tienen factores comunes), entonces existe una solución única para x que se encuentra en el intervalo [0, b_1 * b_2 * ... * b_n).
-->
Por lo tanto, si se conocen los valores de los pares (a_i, b_i) proporcionados por los amigos de Daniela y se pueden verificar que los b_i son coprimos entre sí, entonces se puede utilizar el teorema chino del resto para determinar el valor máximo que tomará x. Este valor máximo será igual a b_1 * b_2 * ... * b_n - 1.

Cabe destacar que si los valores de b_i no son coprimos entre sí, entonces el teorema chino del resto no se puede aplicar directamente, y se necesitará utilizar otros métodos para determinar el valor máximo de x.

#### Pseudocódigo
```
// Leer los pares de números (a_i, b_i) proporcionados por los amigos de Daniela
Leer a_i y b_i para i = 1 hasta n

// Verificar que los b_i son coprimos entre sí
Si mcd(b_1, b_2, ..., b_n) ≠ 1 entonces
    // Los b_i no son coprimos, no se puede aplicar el teorema chino del resto
    Imprimir "No se puede aplicar el teorema chino del resto"
Sino
    // Calcular el valor de M
    M = 1
    Para i = 1 hasta n hacer
        M = M * b_i

    // Encontrar el valor de x
    Encontrado = Falso
    x = Max(b_i) + 1
    Mientras no se haya encontrado un valor para x hacer
        // Verificar si x cumple la condición dada
        CumpleCondicion = Verdadero
        Para i = 1 hasta n hacer
            Si x % b_i = a_i entonces
                CumpleCondicion = Falso
                Salir Para
            Fin Si
        Fin Para

        // Si x cumple la condición, se ha encontrado la solución
        Si CumpleCondicion entonces
            Encontrado = Verdadero
            Imprimir "El valor de x es: ", x
        Sino
            // Pasar al siguiente valor de x
            x = x + 1
        Fin Si
    Fin Mientras
Fin Si
```

Este pseudocódigo comienza verificando si los valores de b_i son coprimos entre sí. Si lo son, entonces calcula el valor de M mediante la multiplicación de todos los valores de b_i. Luego, comienza a probar valores enteros positivos para x, comenzando por Max(b_i) + 1, y verifica si cada valor de x cumple la condición dada. Si se encuentra un valor de x que cumple la condición, se imprime y se detiene el proceso. De lo contrario, se continúa probando valores de x hasta encontrar una solución.

En cuanto a la correctitud de nuestro algoritmo de fuerza bruta podemos decir que encontrara la solucion correcta en caso de existir, ya que explora todas las posibles combinaciones para todos los pares (a_i, b_i) con cualquier valor de x.

#### Sin utilizar TCR
Se presenta otra solucion sin utilizar el teorema chino del resto:

```
// Leer los pares de números (a_i, b_i) proporcionados por los amigos de Daniela
Leer a_i y b_i para i = 1 hasta n

// Encontrar el valor máximo de b_i
Max_b = 0
Para i = 1 hasta n hacer
    Si b_i > Max_b entonces
        Max_b = b_i
    Fin Si
Fin Para

// Encontrar el valor máximo de x
Encontrado = Falso
x = Max_b + 1
Mientras no se haya encontrado un valor para x hacer
    // Verificar si x cumple la condición dada
    CumpleCondicion = Verdadero
    Para i = 1 hasta n hacer
        Si x % b_i = a_i entonces
            CumpleCondicion = Falso
            Salir Para
        Fin Si
    Fin Para

    // Si x cumple la condición, se ha encontrado la solución
    Si CumpleCondicion entonces
        Encontrado = Verdadero
        Imprimir "El valor de x es: ", x
    Sino
        // Pasar al siguiente valor de x
        x = x + 1
    Fin Si
Fin Mientras

// Imprimir el valor máximo de x probado
Si Encontrado entonces
    Imprimir "El valor máximo de x es: ", x - 1
Sino
    Imprimir "No se encontró ningún valor de x que cumpla la condición dada"
Fin Si
```

Este pseudocódigo comienza encontrando el valor máximo de los b_i proporcionados por los amigos de Daniela. Luego, comienza a probar valores enteros positivos para x, comenzando por Max(b_i) + 1, y verifica si cada valor de x cumple la condición dada. Si se encuentra un valor de x que cumple la condición, se imprime y se detiene el proceso. De lo contrario, se continúa probando valores de x hasta encontrar una solución. Finalmente, se imprime el valor máximo de x que se probó.

#### Utilizando Metaheurísticas
Se presenta un pseudocódigo que utiliza una metaheurística para resolver el problema. En este caso, utilizaremos un algoritmo de recocido simulado:

```
// Leer los pares de números (a_i, b_i) proporcionados por los amigos de Daniela
Leer a_i y b_i para i = 1 hasta n

// Definir la temperatura inicial y la tasa de enfriamiento
T0 = 1000
alpha = 0.99

// Definir la función de energía
E = función que mide la cantidad de pares (a_i, b_i) que no se cumplen para un valor dado de x

// Generar un valor aleatorio inicial para x
x_actual = valor aleatorio positivo

// Iniciar el proceso de recocido simulado
T = T0
Mientras T > 0 hacer
    // Generar una solución vecina de x_actual
    x_vecino = x_actual + valor aleatorio en el rango [-1, 1]

    // Calcular la energía de las dos soluciones
    energia_actual = E(x_actual)
    energia_vecino = E(x_vecino)

    // Si la solución vecina es mejor, se acepta automáticamente
    Si energia_vecino < energia_actual entonces
        x_actual = x_vecino
    Sino
        // Si la solución vecina es peor, se acepta con una probabilidad dada por la temperatura
        probabilidad_aceptacion = exp(-(energia_vecino - energia_actual) / T)
        Si valor aleatorio entre 0 y 1 < probabilidad_aceptacion entonces
            x_actual = x_vecino
        Fin Si
    Fin Si

    // Enfriar la temperatura
    T = T * alpha
Fin Mientras

// Imprimir la solución encontrada
Imprimir "El valor de x es: ", x_actual
```

Este pseudocódigo comienza definiendo la temperatura inicial y la tasa de enfriamiento para el algoritmo de recocido simulado. Luego, define una función de energía que mide la cantidad de pares (a_i, b_i) que no se cumplen para un valor dado de x. A continuación, genera un valor aleatorio inicial para x y comienza el proceso de recocido simulado.

Durante cada iteración del proceso, se genera una solución vecina de x_actual, se calcula la energía de ambas soluciones y se decide si se acepta la solución vecina o no. Si la solución vecina es mejor que la actual, se acepta automáticamente. Si la solución vecina es peor, se acepta con una probabilidad dada por la temperatura. Luego, se enfría la temperatura y se repite el proceso.

Una vez que se completa el proceso de recocido simulado, se imprime la solución encontrada para x. Cabe destacar que, al igual que con otros métodos heurísticos, no se puede garantizar que se encuentre la solución óptima utilizando este enfoque, pero es posible encontrar una solución razonablemente buena en un tiempo razonable.