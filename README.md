
# Primer Proyecto de Diseño y Análisis de Algoritmos


## Carlos Carret Miranda C-312

<!-- ###Enunciado del problema -->

### Tito el tramposo

Tito está pasando un curso de Diseño y Análisis de Algoritmos. Este año, por primera vez en la historia, los profesores han decidido evaluar el curso mediante un examen final y Tito se ha dado cuenta de que, a grandes rasgos, está frito. A pesar de ser un poco barco, es de hecho un muchacho inteligente y rápidamente se da cuenta que su única forma de aprobar era hacer trampa. El día de la prueba, Tito se sentó en el asiento que estaba entre Hansel y Elena para fijarse, con la esperanza de que, uniendo las preguntas respondidas por cada uno, se pudiera formar un examen correcto.

El examen tiene $n$ preguntas, ordenadas en la hoja. Elena y Hansel pueden no ser capaces de responder cada uno el examen entero, pero todas las preguntas que responden, están correctas. Se conoce cuáles preguntas respondió cada uno y se reciben como dos listas ordenadas de enteros entre 1 y $n$. Tito tiene $p$ oportunidades para mirar hacia la izquierda (hoja de Hansel) o hacia la derecha (Hoja de Elena) y su agilidad mental le alcanza para ver las respuestas de $k$ preguntas consecutivas (en cualquier posición) cada vez que echa una mirada a un examen.

Ayude a Tito a saber la cantidad máxima de preguntas que puede responder con su (tramposa) estrategia.

### Descripción del problema

El problema que se presenta es el de ayudar a Tito a encontrar la cantidad máxima de preguntas que puede responder correctamente en un exámen, mediante la observación de las respuestas de Hansel y Elena. Se asume que Tito tiene la capacidad de ver $k$ preguntas consecutivas en cada oportunidad que tiene para mirar hacia la izquierda o hacia la derecha.

Se cuenta con dos listas ordenadas de enteros entre 1 y $n$, que indican las preguntas que fueron respondidas correctamente por Hansel y Elena, respectivamente. El objetivo de Tito es unir ambas listas de manera tal que se forme un examen correcto. 

Es importante destacar que Hansel y Elena pueden no haber respondido todas las preguntas del examen, pero las que respondieron son correctas. 

Se debe encontrar una estrategia tramposa que permita a Tito observar las respuestas de Hansel y Elena de tal forma que pueda responder la mayor cantidad posible de preguntas correctamente.
Aspectos a destacar del problema:
* Se trata de un problema de optimización, en el que se busca encontrar la cantidad máxima de preguntas que Tito puede responder correctamente.
* El problema implica el uso de listas ordenadas de enteros, lo que sugiere que debemos utilizar algoritmos que nos faciliten el trabajo con estas estructuras de datos para resolverlo, así como un buen manejo de los datos contenidos en las mismas.
* La capacidad de Tito para ver $k$ preguntas consecutivas en cada oportunidad que tiene para mirar hacia la izquierda o hacia la derecha es un aspecto clave del problema, ya que limita la cantidad de información que puede obtener en cada oportunidad.
* El hecho de que Hansel y Elena no hayan respondido todas las preguntas del exámen, pero las que respondieron son correctas, implica que algunas preguntas pueden estar ausentes de las listas y se deben manejar estos casos en la estrategia tramposa.
* Al parecer se puede seguir una estrategia $greedy$ para resolver el problema, ya que siempre nos queremos quedar con el valor óptimo. También parece que se puede lograr seguir una estrategia de divide y vencerás, ya que se puede dividir el problema en subproblemas mas pequeños, los cuales pueden ser resueltos de manera independiente.
* Dado que podemos dividir nuestro problema en subproblemas mas pequeños, podemos utilizar la programación dinámica para resolverlo, ya que esta técnica nos permite resolver problemas de optimización que pueden ser divididos en subproblemas mas pequeños.
* El ordenamiento de las preguntas es importante, ya que se debe preservar el orden original de las preguntas en el examen.

Ideas para atacar al problema
* Primeramente se busca dar solución al problema mediante la recursividad y fuerza bruta. Con esto buscamos resolver el problema para obtener resultados lo suficientemente correctos para luego compararlos con otras soluciones que sean mejores.
* Luego se realizaron modificaciones al algoritmo de fuerza bruta para obtener una solución mas eficiente. Se agrega un diccionario para guardar todas aquellas selecciones de $p$ miradas y no repetirlas, de esta forma se poda la búsqueda de soluciones repetidas o que no tendrían mucho sentido. Se realizaron pruebas con los datos de entrada para ver si el algoritmo obtenía resultados correctos.
* Siguiendo el camino de la recursividad y las mejoras a nuestro algoritmo, se puede notar que cada vez que vamos a escoger hacia que lado mirar, digamos consumir una instancia de $p = 1$, estamos escogiendo si mirar hacia la izquierda, derecha o si no mirar hacia ningún lado y mirar para el siguiente $p$. Es decir, nos encontramos con que podemos escoger entre 3 elecciones y nuestro problema quedaría subdividido en 3 subproblemas, por tanto, podemos hacer uso de la técnica de divide y vencerás para luego quedarnos con la solución que nos aporte un mayor número de preguntas respondidas.
* Observando un poco la manera de escoger hacia que lado mirar y la manera en que se resuelve el problema, se puede notar que la estrategia golosa es una buena opción para resolver el problema. Esto se debe a que siempre nos queremos quedar con el valor óptimo, por tanto, podemos escoger la mejor opción en cada momento y así obtener la solución óptima.
* Siguiendo una idea parecida a la de divide y vencerás podemos darnos cuenta que al dividir nuestro problema en subproblemas podemos utilizar programación dinámica para obtener una solución más rápida y que consuma menos memoria.

### Herramientas y código auxiliar
Para la realización de este proyecto se utilizó Python en su versión 3.7.4.
Se crearon las clases SOL y MatchedSOL que se encuentran en el archivo $sol.py$, así como otros métodos auxiliares útiles para el manejo de las estructuras de datos y las soluciones que se van conformando.
Las clases SOL y MatchedSOL son utilizadas para representar soluciones, dígase solución la secuencia de selecciones que se hacen a medida que se escoge si mirar hacia el examen de elena a $k$ preguntas o al de hansel a $k$ preguntas.
Entonces estas clases tendrían un $string$ que sería el nombre de la persona a la cual se observa el exámen, un intervalo representado por una instancia del tipo $range$ que nos brindará información sobre que intervalos se escoge, es decir, se busca a partir de la pregunta $i$ hasta la $i+k$, siendo $i<=n-k$.
Para el caso de la clase MatchedSOL también tendremos una lista de tipo bool de tamaño n que nos dirá cuales preguntas tenía respondida esta persona en el intervalo desde $i$ hasta $i+k$, así como una variable para almacenar la cantidad de estas preguntas respondidas.

En lo adelante nos referiremos a una solución como una concatenación de selecciones(SOL)

```python
class SOL:
    def __init__(self, domain, start, stop) -> None:
        self.domain = domain
        self.ranges:range = range(start, stop)

    # Redefinir el print de la clase SOL
    def __str__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop}"
    
    def __repr__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop}"

    @staticmethod
    def concat_sol(left_sol: list, right_sol):
        tmp_left_sol = left_sol.copy()
        tmp_left_sol.append(right_sol)
        return tmp_left_sol

class MatchedSOL(SOL):
    def __init__(self, domain, start, stop, matched_mask: list=[], matched_number: int=0) -> None:
        super().__init__(domain, start, stop)
        self.matched_mask = matched_mask
        self.matched_number = matched_number # Matched number is the number of indices in mask that are true

    def __str__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop} matched: {self.matched_number}"

    def __repr__(self) -> str:
        return f"Domain: {self.domain} Range: start: {self.ranges.start+1} end: {self.ranges.stop} matched: {self.matched_number}"
 
```
### Generador
```python
def problem_generator():
    n = random.randint(1, 20)
    k = random.randint(1, n)
    p = random.randint(1, n)
    elena = []
    hansel = []

    for i in range(0, n):
        elena.append(random.randint(1, n))
        hansel.append(random.randint(1, n))

    elena.sort()
    hansel.sort()
    # Remove duplicates from the lists
    elena = list(dict.fromkeys(elena))
    hansel = list(dict.fromkeys(hansel))
    
    filename = save_params(elena, hansel, k, p, n)
    print(f"Problem saved in {filename}")

    return elena, hansel, k, p, n
```

### Tester
```python
def test_sol(elena, hansel, k, p, n, sol, method="bf", test_alg_time=""):
    ans = 0

    ts = time.time()
    
    if method == "bf":
        ans = bf.solve(elena, hansel, k, p, n)
    elif method == "bf_opt":
        ans = bf_opt.solve(elena, hansel, k, p, n)
    elif method == "div_n_con":
        ans = div_n_con.solve(elena, hansel, k, p, n)
    elif method == "greedy":
        ans = greedy.solve(elena, hansel, k, p, n)

    te = time.time()
    time_str = f"Time: {round(te-ts, 5)}"

    if ans == sol:
        printg(f"maximum: {sol} {test_alg_time} expected: {method}_solution: {ans} SUCCESS! {time_str}")
    else:
        printr(f"maximum: {sol} expected: {ans} !FAILED {time_str}")
        return False

    return True
```

### Algoritmos de solución

#### Fuerza Bruta (Backtracking) - bf

##### Idea
La idea intuitiva que se sigue en este algoritmo es la siguiente:
Se generan todas las combinaciones que puede escoger Tito mirando hacia ambos lados. Recalcar que en el primer algoritmo recursivo de backtrack que se crea se pueden tener selecciones repetidas. Por ejemplo, se puede mirar a la hoja de Hansel a las preguntas $1+k$ y luego volver a mirar a la hoja de Hansel a las preguntas $1+k$, repitiendo así
una selección y consumiendo $2$ oportunidades, quedandonos solamente $p-2$ oportunidades para encontrar más respuestas.
El algoritmo consta de dos ciclos $for$ que llaman en su interior al metodo recursivo, que es en si mismo quien contiene el doble ciclo $for$. En el primer ciclo se itera por las personas disponibles para que Tito se fije, es decir Elena y Hansel (llamémosles dominios). En el segundo $for$ se itera por los distintos intervalos que se pueden escoger de $i+k$ preguntas.
Iterando desde $i=0$ hasta $i=n+k-1$, de esta manera no estamos teniendo en cuenta las soluciones de las últimas $n-k$ veces, ya que serían redundantes y estaríamos repitiendo selecciones que ya tuvimos en cuenta, debido a que al escoger $i=n-k+1$ solo podemos obtener un menor valor de cantidad máxima de respuestas correctas al escoger $n-k+2, n-k+3,..., n-k+n$.
Luego de esta forma estaríamos escogiendo todas las posibles formas de seleccionar hacia donde mirar $p$ veces.

Como caso de parada de nuestro algoritmo tenemos que cuando $p$ sea $0$ se detenga. En cada llamado recursivo vamos decrementando $p$ y de esta forma sabemos que en el siguiente llamado recursivo tenemos que llamar recursivamente de nuevo $p-1$ veces que serán las restantes veces que Tito podría mirar hacia la hoja de Elena o la de Hansel.

##### Correctitud
Prácticamente con nuestro algoritmo estamos probando todas las maneras posibles mediante las cuales se puede escoger hacia donde mirar $p$ veces, solamente obviando aquellas selecciones donde se repiten respuestas que ya obtuvimos y que por tanto ya están contenidas en otra, es decir las ultimas $n-k$.
Luego, con demostrar que nuestro algoritmo las genera todas y que esas últimas ya están contenidas en otras nos basta para afirmar que nuestro algoritmo nos devuelve valores correctos.
Para demostrar que nuestro algoritmo genera todas las posibles selecciones nos apoyaremos en un poco de combinatoria.

Si para cada posición($i$ donde $i$ es la pregunta $i$) podemos escoger que la pregunta $i$ será escogida de elena o hansel y las siguientes $n-i$ preguntas pueden ser escogidas de ambos igual, podemos notar que en el momento en el que se escoge la pregunta $i$ nos quedan $n-i$ * ($cantidad-de-formas-escogiendo-primero-a-elena$ + $cantidad-de-formas-escogiendo-primero-a-hansel$) .
Diremos que el primer $for$ se encarga de escoger primero a elena y luego a hansel, para así calcular la cantidad de veces en la que primero escoge elena y en la que primero escoge hansel las restantes $n-i$ preguntas. Mientras que el segundo ciclo $for$ se encarga de brindarnos la posibilidad de movernos entre esas $n-i$ preguntas, repitiendo las anteriores que sean menores que $i$ en algunos casos, pero nos da igual porque al estar repetidas no influirán en el conteo a la hora de buscar el máximo.
Solo nos volvera más ineficiente nuestro algoritmo, pero podemos continuar con la idea principal de que hasta el momento $i$ se escogieron de alguna forma $i$ preguntas, mirando hacia el exámen de Elena o al de Hansel y sumando hasta el momento $n$ preguntas correctas, nos falta entonces averiguar de las restantes $n-i$ preguntas cuantas posibilidades tenemos. 

###### Demostrar $n-k$
Con respecto a la demostración de las últimas $n-k$ preguntas, se sabe que Tito puede ver desde la pregunta $i$ hasta la $i+k$ en cada mirada que hace a las hojas de Elena o Hansel, entonces cuando TIto mira a la pregunta $i$, este puede mirar la $i + 1, i+2,...i+k$, para el momento en que $i = n-k$, entonces Tito puede ver las preguntas $n-k + 1, n-k+2,...n-k+k = n$ $=>$ Tito pudo ver las últimas $n-k$ preguntas que tenía respondidas Elena o Hansel mirando una sola vez.
Si permitimos que Tito observe los próximos intervalos de $(i=n-k, n-k+k), (n-k+1, n-k+k+1),(n-k+2, n-k+k+2),...,(n-k+n, n-k+k+n)$ nos damos cuenta de que solo estamos repitiendo respuestas porque en todos los casos el máximo de nuestro intervalo es $n$ y en el primer caso, al analizar $i=n-k$ ya obtuvimos todos los valores en ese intervalo.

##### Complejidad Temporal
Como podemos ver estamos buscando todas las posibles variaciones con repetición en un arreglo de tamaño $n$, teniendo como dominio un conjunto con 2 posibles valores para ubicar en cada posición del arreglo. Luego nos queda que tendrá una complejidad de:
$T(n) = 2^{n} + O(n*k)$

```python
def bf(domains, n, k, p, sol, e, h):
    if not p:
        return evaluate(sol, n, e ,h)

    ans = 0
    for domain in domains:
        for i in range(0, n-k+1):
            tmp_sol = make_sol(domain, i, i+k)
            concat_sol:list = SOL.concat_sol(sol, tmp_sol)

            # Logs
            # printb(tmp_sol)

            ans = max(ans, bf(domains, n, k, p-1, concat_sol, e, h))
            
            # Remover el ultimo elemento de una lista
            concat_sol.pop()

    return ans
```
#### Fuerza Bruta Optimizada (Backtracking con podas) - bf_opt

##### Idea
La idea es similar a la que sigue el algoritmo de fuerza bruta sin podas. La diferencia recae en la adición de un diccionario para conocer en todo momento cuáles selecciones ya han sido agregadas y de esta forma no repetir selecciones de una selección($SOL$) que se encuentre en cierto rango. Si una selección ya fue agregada al diccionario, al indexar en la misma de la forma sols_dict[f"{domain}_{start_range}_{stop_range}"] obtendremos el valor de $True$ si ya se está utilizando en la confección de la solución actual y el valor de $False$ o que no se encuentra la llave en el caso contrario.

Se agrega como comprobación al inicio lo siguiente $k == n$ or $n <= k*p$ y en caso de cumplirse alguna de las mismas se evalúa la solución que se está formando actualmente. La idea detrás de esto es que para el primer caso, si $k==n$, se estaría diciendo que si con $p=1$ puedo ver todas las respuestas en el exámen de elena o hansel, pues que intento ver cuáles se obtienen y no tengo que revisar solamente cuando $p$ se haga $0$.
En el caso de $n <= k*p$, se esta diciendo que si tenemos suficientes oportunidades de ver todas las preguntas($n$, seleccionándolas una por una) con las $k*p$ selecciones. Pues deberíamos de analizar esta solución, ya que probablemente se encuentre entre las mejores selecciones de una solución que podemos conformar.

##### Correctitud
Debido a que este algoritmo es similar al de backtrack nos centraremos en las partes que fueron agregadas. Se puede asumir que las explicaciones restantes serían una copia de las explicaciones que se usaron para demostrar el backtrack sin podas.

##### No repeticiones
Primeramente comencemos por demostrar que al agregar el nuevo diccionario las soluciones dejan de repetir ciertas elecciones que no nos aportarán mucho y solamente harán nuestro algoritmo más costoso.
Para ello nos centraremos en las líneas donde se agrega al diccionario la nueva llave con la elección tomada en este instante antes de llamar recursivamente, también luego de salir del método recursivo, al modificar el valor en la llave que contiene a esta elección, poniendolo en $False$.
Al comienzo del doble ciclo $for$ se esta verificando que la nueva elección no se haya tomado anteriormente, para ello se verifica su existencia en el diccionario sols_dict. 
Podemos decir que una vez se haya tomado esta elección al llamar recursivo no se volverá a tomar en los siguientes llamados, solo cuando se llegue a un caso de parada y se retorne se volverá a tener en cuenta esta elección.

##### Genera todas las combinaciones
Demostremos entonces que esta solución, en efecto, nos genera todas las posibles combinaciones que nos interesan, sin tener las repetidas y que esto da solución a nuestro algoritmo.

Sabíamos que antes obteníamos el conjunto de todas las posibles formas de escoger $p$ veces intervalos de tamanno $k$ tanto de elena como de hansel. Al agregar a nuestra solución el nuevo diccionario con sus respectivos códigos estamos eliminando el conjunto de soluciones donde se encuentra al menos una elección repetida(elemento de tipo $SOL$), por tanto obtenemos como resultado el conjunto de soluciones donde no se repiten $2$ elecciones. Es decir no ocurre que:
Se puede mirar a la hoja de Hansel a las preguntas $1+k$ y luego volver a mirar a la hoja de Hansel a las preguntas $1+k$, repitiendo así una selección y consumiendo $2$ oportunidades, quedándonos solamente $p-2$ oportunidades para encontrar maás respuestas. Como bien habíamos dicho que ocurría en la solución de fuerza bruta.

Luego tenemos que:
conjunto resultante =  (conjunto de todas las combinaciones) - (conjunto de combinaciones que repiten al menos 1 elección)

Como no nos interesa repetir elecciones en nuestra solución, podemos decir que el conjunto resultante nos resuelve nuestro problema. Por tanto, nuestro algoritmo funciona correctamente.

##### Complejidad Temporal
Similar al algoritmo de fuerza bruta sin podas. La simple adición del diccionario y la comprobación de los valores que se encuentran en el mismo no quita que para el caso peor se recorran ambos ciclos $for$. 

```python
def bf_opt(domains, n, k, p, sol, e, h, sols_dict):
    ans = 0
    if k == n or n <= k*p: # Si la cantidad de intentos que puedo usar me basta para encontrar las 9 preguntas entre ambas pruebas
        if not sol:
            pass
        else:
            ans = evaluate(sol, n, e, h)
    if not p:
        return evaluate(sol, n, e ,h)

    # ans = 0
    for domain in domains:
        for i in range(0, n-k+1): # for i in range(0, n-k+1): 
            if contains_sol(sols_dict, domain, i, i+k): # If has choosen the sol, just continue
                continue
            tmp_sol = make_sol(domain, i, i+k)
            concat_sol:list = SOL.concat_sol(sol, tmp_sol)

            # Logs
            # printb(tmp_sol)
            sols_dict[f"{domain}_{i}_{i+k}"] = True

            ans = max(ans, bf_opt(domains, n, k, p-1, concat_sol, e, h, sols_dict))

            sols_dict[f"{domain}_{i}_{i+k}"] = False

            # Remover el ultimo elemento de una lista
            concat_sol.pop()

    return ans
```

##### Divide y Venceras - div_n_con

##### Idea
La idea a seguir es irnos moviendo en las $p$ elecciones que podemos tomar a través de las $n$ preguntas que tenemos que responder y darnos cuenta de que tenemos $3$ posibles elecciones para tomar en la elección número $i$ que influirá en las elecciones $i + 1, i + 2,..., i + k$, siendo $i+k<=p$.
Para ello en cada llamado recursivo podremos seleccionar y subdividir nuestro problema en $3$ nuevos problemas, restar $1$ al valor de $p$ y seleccionar mirar hacia la hoja de Elena, restar $1$ al valor de $p$ y seleccionar mirar hacia la hoja de hansel, no restar $1$ al valor de $p$ y no mirar ni a la hoja de elena ni a la de hansel en este elección.

Destacar que cada vez que llamamos recursivamente a alguno de estos casos estamos creando una copia de la lista que tengamos actualmente y concatenando un elemento a esta que sería la elección que tomamos.
Luego, al encontrarse en algun caso de parada retornará la solución completa.
Como casos de parada tenemos que:
* Si $n - k \leq pos - 2$. En este caso estamos analizando que el índice de la pregunta actual por la que nos estamos moviendo sea menor que $n-k$, tomando en cuenta $n-k-1$, debido a que se puede optar por revisar $1$ vez con $n-k$ a elena y otra vez con $n-k$ a hansel. De esta manera, aunque nuestro $p$ aún no sea $0$
podemos retornar en uno de nuestros llamados recursivos sin necesidad de probar las $p$ veces restantes alguns soluciones que repetirian las que ya buscamos.
* Si $p == 0$. Este caso es utilizado en los momentos en que ya hemos hecho $p$ elecciones.

##### Correctitud
Debemos demostrar que nuestro algoritmo analiza todas las posibles combinaciones que influyen en la selección del valor máximo de la cantidad de preguntas correctas que se pueden obtener. En el caso de este algoritmo cabe destacar que no se repiten elecciones en cada solución, esto también lo demostraremos.

Para la primera parte, podemos partir de que en cada llamado recursivo estamos analizando una solución en la cual se agrega el índice de la pregunta $i$ siendo respondida por elena, hansel o por ninguno de ambos. De este modo, para cada índice $i$, nos faltarían analizar los $n-i$ restantes. Luego, debido a la forma en la que funciona la recursividad, se cumplirá que para cada $i$, se analizan los $3$ casos por separados. Entonces es seguro que para todo índice $i$ se exploran todas sus posibles vías sin repetir alguna y para los restantes $n-i$ índices que se iran conformando en la ejecución del algoritmo se repite el proceso, es decir, también se escogen las $3$ posibles opciones posibles en cada uno de los $n-i$ índices.

##### No repetición de soluciones

Debido a que en cada llamado recursivo llamamos aumentando $i$ en $1$ hacia un mayor valor que cada vez se acerca más a $n$, no será posible repetir una selección que se haya escogido en una misma solución. Para mostrar mejor esto podemos decir que para todo valor de $i, i < n$, se escoge $persona_x$ con preguntas $i$ hasta $k$ y en el llamado con $i+n$, no existe forma de volver a escoger $persona_x$ con preguntas $i$ hasta $k$, debido a que en los siguientes llamados se llama como mínimo con $i+1$ y tampoco podría repetirse desde antes porque en los llamados anteriores se hicieron con $i - x$, donde $x \leq i$. Por tanto no se volvería a crear una selección con $i$ para todo $i, i < n$ y no tendríamos soluciones con selecciones repetidas.

##### Complejidad Temporal
Evaluar la solución conformada será $O(n*k)$ a lo sumo, donde $k < n$ para valores grandes de k. Esta evaluación de la solución sería recorrerla completa y para cada selección recorrer su rango, es decir $k$ elementos.
3T(n-1) + O(n)

Por el Teorema maestro, tenemos:
$a = 3, b = 1$ => $T(n) = a^{n/1} + n = O(3^{n} + n)$

```python
def div_n_con(domains, n, k, p, elena, hansel, pos, sol):
    # if n == pos + k: if theres is no more choices
    if n - k <= pos - 2:
        return evaluate(sol, n, elena, hansel)
    # if p == 0: if there is no more choices
    if p == 0:
        return evaluate(sol, n, elena, hansel)

    # Try choosing elena, then choosing hansel and then choosing no one
    return max(div_n_con(domains, n, k, p - 1, elena, hansel, pos+1, SOL.concat_sol(sol, SOL("elena", pos, pos+k))), 
               div_n_con(domains, n, k, p - 1, elena, hansel, pos+1, SOL.concat_sol(sol, SOL("hansel", pos, pos+k))),
               div_n_con(domains, n, k, p, elena, hansel, pos+1, sol))
```

#### Solución greedy(golosa) - greedy

##### Idea
En este algoritmo se hará un uso más extenso de la clase $MatchedSOL$.
Primero se crean dos diccionarios para ubicar en estos los valores de cantidad de soluciones en intervalos cualesquiera.
Se itera desde $0$ hasta $n-k+1$ para ir ubicando en cada diccionario las selecciones que pueden hacerse para los rangos desde $i$ hasta $i+k$. Estas selecciones se van agregando de manera tal que en todo momento obtengamos la cantidad de preguntas correctas que tenían elena y hansel, en un diccionario para las de elena y otro para las de hansel respectivamente. Para ello se cuenta con la clase $MatchedSOL$ y sus arreglo de tipo $bool$ para decirnos en cada posición cual se encuentra respondida correctamente y un entero con la cantidad de estas preguntas que se haya respondido.
Luego pasamos al procedimiento principal de nuestro algoritmo, en este se tiene un ciclo $for$ que iterara $p$ veces, donde cada vez nos iremos quedando con la selección que nos brinde mas respuestas correctas, siguiendo asi una estrategia golosa.
Buscaremos el valor máximo en cada diccionario para así saber cual selección escoger, en caso de coincidir estos valores procedemos a ver si sus rangos se superponen de alguna forma, en caso de que no se superpongan procedemos a escoger cualquiera, en otro caso tendremos que analizar que sucede en el siguiente paso, es decir, al reducir $p$ en $1$ al escoger como siguiente mirar hacia elena o hacia hansel. En caso de volver a coincidir ambos valores al buscar el máximo siguiendo el procedimiento que se mencionó anteriormente, escogemos por defecto a Elena para que luego en la siguiente iteración al restarle $1$ a $p$ esta vez, se pueda volver a buscar un nuevo máximo y repetir este procedimiento. Destacar sobre esta última parte del algoritmo, que en caso de querer obtener mayor seguridad a la hora de hallar el maximo siguiendo esta vía en este instante que se tiene este $p$ y ambos valores coinciden, se podría llevar a cabo una búsqueda más profunda para valores menores que $p$ hasta que no se encuentre conflicto conque ambos valores coincidan, pero en ese caso el costo computacional de la solución aumentaria.
Luego de escoger esta mejor seleccion, pasamos a modificar aquellas selecciones cuyos rangos se superponen de alguna forma con el rango de la seleccion escogida.

##### Correctitud
En cada iteración del algoritmo nos estamos quedando con la elección que nos brinde la mayor cantidad de respuestas que podemos escoger en ese instante o sino la mayor cantidad de respuestas que podamos escoger en total a lo largo del algoritmo.
Debemos de demostrar como ambas selecciones nos brindan al final la mejor solución. Es decir, como escogemos entre cada subproblema el óptimo.

Practicamente siempre queremos quedarnos con lo mejor y podemos afirmar que esta es la vía a seguir ya que si puedo escoger de cierta forma más respuestas que de otra forma, escojo la que más respuestas me brinde. En caso de que ambas se superpongan podemos decir que la que más nos aporte puede contener a la que menos nos aporte, en este caso, preferiríamos escoger la que contiene a la que menos nos otorga. Para el caso en que no se superpongan, ambas se encontrarían en rangos aislados uno del otro, en este caso, nos queremos quedar con la mejor respuesta porque en caso de no escoger la mayor, no encontraríamos nada mejor que esa mayor que no escogimos, en otras palabras todas las restantes serían menores o iguales que la que no es la mayor. En caso de que se superpongan pero ninguna contenga completamente a la otra, se tendria que buscarla mejor forma de escoger las soluciones dando $1$ o más pasos probando así para menores valores de $p$. Los pasos anteriormente descritos son los que sigue nuestro algoritmo y luego de llevarlos a cabo se puede afirmar que siguiendo esa estrategia nos podemos quedar en todo momento con la mejor solución.

Destacar que en nuestro algoritmo no se tiene en cuenta el caso en que se tengan $2$ selecciones de una misma persona con el mismo número de respuestas correctas y que este número sea el máximo. Para dar solución al mismo se puede seguir el mismo enfoque del cual se hablo o que se sigue para el caso en que tanto las selecciones con los valores máximos de Elena y Hansel coincidan.

##### Complejidad Temporal
Primero tenemos un ciclo $for$ desde $0$ hasta $n-k+1$(desde $1$ hasta $n-k$). Este tendría a lo sumo complejidad $n$, dado que $n \geq k$.
Luego se itera por cada elemento agregado al diccionario para confeccionar su lista de respuestas correctas y su entero con la cantidad de respuestas correctas que tenga.
En estos $2$ dobles ciclos $for$, un doble ciclo para Elena y otro doble ciclo para Hansel, se iteran $n * k$ veces, donde $k$ representa el rango. Destacar que para un valor de $k$ muy alto, $k=n$, esta parte del codigo parece que tomaria $O(n*n)$ para hacerse, pero al haber seleccionado en el primer for que se iterase desde $0$ hasta $n-k$, estamos garantizando que esto no ocurra, ya que en caso de tener un $k$ muy grande tendriamos $n-k$ elementos en el diccionario. Luego, al multiplicarlo por $k$, nos quedaria como complejidad del doble ciclo $for$ un número que es menor que n multiplicado por $k$, obteniéndose una complejidad menor que $O(n*n)$. Luego a lo sumo tendríamos que recorrer $n$ elementos y hacer k recorridos para cada uno de esos $n$, lo cual resulta en $O(n*k)=O(n)$.
Posteriormente analizamos el bucle que itera $p$ veces:
* En sus primeras lineas se buscan los mayores en el diccionario de Elena y luego el de Hansel. A lo sumo sera $O(n)$ ya q estaremos recorriendo todos los elementos de los diccionarios.
* Luego Tenemos una condicional $if$, que si no se cumple entraría en el $else$ que se ejecutaría en $O(1)$. Veamos el caso peor y supongamos que se cumpla el $if$. Primero le haremos una copia ambos diccionarios. Digamos que para esto recorreremos todos los elementos de cada uno y luego cada lista de tipo $bool$ de cada uno, es decir, a lo sumo sería $O(n*k)$ donde como bien ya sabemos esto será menor que $O(n)$. Luego vamos a analizar que sucedería si damos $1$ paso más y reducimos en $1$ el valor de $p$. Para ello hacemos uso del método $update\_matched\_number$. Analicemos el costo de $update\_matched\_number()$, en este se hace un $for$ desde $0$ hasta el mínimo entre el valor de inicio del rango de la selección que tomamos y el valor maximo del rango que tomamos. Destacar que si el mínimo es menor que $0$, pues sería hasta $0$ y si el maximo es mayor que $n$ pues sería hasta $n$. Se realizarían a lo sumo $3*k$ iteraciones. Las $k-1$ primeras que puedan contener al primer número del rango, las $k$ iteraciones del rango y las $k-1$ últimas que puedan contener al rango también. Luego,  para casos grandes de $n$, $3*k$ sigue siendo menor que n. Para el caso de $update\_mask()$ se tiene un for itera $k$ veces, debido a que itera en el rango de una selección. Luego nos queda para el caso peor $O(3*k * k)$, donde $k \leq n$ y para valores muy grandes de k como bien se ha explicado anteriormente la cantidad de elementos que tendremos sera pequeña, luego el $k$ del método $update\_mask()$ sera menor que n, obteniéndose así algo menor que $O(n*n)$ y menor que $O(k*n)$.
* Por último, una vez que salgamos de la condicional $if$ tendremos otra llamada al metodo $update\_matched\_number()$ el cual ya analizamos anteriormente.
Finalmente podemos calcular que nuestro algoritmo tendrá una complejidad de:
$O(n) + O(p*k*n) = O(p*n)$, siendo $k$ menor que n, y teniendo en cuenta que $O(k*n) \leq O(n)$ para un $n$ muy grande, tomando a $k$ como constante.
Si $p=n$ entonces con escribir unas lineas de código que analicen este caso bastará para evitar que nuestra solución tenga complejidad $n^{2}$.

```python
def update_mask(marked:MatchedSOL, target:MatchedSOL, k):
    for index in marked.ranges:
        val = marked.matched_mask[index]
        if val and target.matched_mask[index]:
            target.matched_mask[index] = False
            target.matched_number -= 1


def update_matched_number(matched_sol: MatchedSOL, k: int, n: int, elena_dict, hansel_dict):
    # Update matched_mask for overlapping indices in ranges of elena_dict.values and hansel_dict.values()
    clone = MatchedSOL(matched_sol.domain, matched_sol.ranges.start, matched_sol.ranges.stop, matched_sol.matched_mask.copy(), matched_sol.matched_number)
    # Create a clone of matched_sol
    for i in range(max(0, clone.ranges.start-k), min(clone.ranges.start+k, n-k+1)):
        update_mask(clone, elena_dict[i], k)
        update_mask(clone, hansel_dict[i], k)
    
    # Update elements with the same range or overlapping range with the matched element. Update matched_mask and matched_number. matched_mask is a boolean list with indices meaning that the index is matched or not. matched_number is the number of indices in mask that are true


def greedy(n, k, p, elena, hansel):
    # Get all combinations with k for elena and hansel
    elena_dict = {}
    hansel_dict = {}

    for i in range(0, n-k+1): # Cost n*k - (n-k+1)*k = n*k - n*k + k*k = k*k
        elena_dict[i] = MatchedSOL(domain="elena", start=i, stop=i+k)
        hansel_dict[i] = MatchedSOL(domain="hansel", start=i, stop=i+k)

    # Set the matched mask and matched number for elena and hansel
    for elena_sol in elena_dict.values():
        matched_mask = [False]*n
        matched_number = 0
        for ans in elena_sol.ranges:
            if ans+1 in elena:
                matched_mask[ans] = True
                matched_number += 1
        elena_sol.matched_mask = matched_mask
        elena_sol.matched_number = matched_number
    
    for hansel_sol in hansel_dict.values():
        matched_mask = [False]*n
        matched_number = 0
        for ans in hansel_sol.ranges:
            if ans+1 in hansel:
                matched_mask[ans] = True
                matched_number += 1
        hansel_sol.matched_mask = matched_mask
        hansel_sol.matched_number = matched_number
    
    ans = 0

    while p:
        # Get the maximum element by matcher_number
        max_elena: MatchedSOL = max(elena_dict.values(), key=lambda x: x.matched_number)
        max_hansel: MatchedSOL = max(hansel_dict.values(), key=lambda x: x.matched_number)

        matched_sol: MatchedSOL = max_elena

        # if are the same matched_number, look if they overlap and chose one
        if max_elena.matched_number == max_hansel.matched_number:
            # If ranges overlap, choose the one with the smallest start index
            if abs(max_elena.ranges.start - max_hansel.ranges.start) < k:
                # Looking for the best choice
              
                # Make a copy of elena_dict and hansel_dict to not modify the original one and update the matched_number
                elena_dict_copy = copy.deepcopy(elena_dict)#.copy()
                hansel_dict_copy = copy.deepcopy(hansel_dict)#.copy()

                # Update the matched_number for the elena_dict_copy and hansel_dict_copy
                update_matched_number(max_elena, k, n, elena_dict_copy, hansel_dict_copy)
                max_elena_copy = max(max(elena_dict_copy.values(), key=lambda x: x.matched_number).matched_number, max(hansel_dict_copy.values(), key=lambda x: x.matched_number).matched_number)

                # Make a copy of elena_dict and hansel_dict to not modify the original one and update the matched_number
                elena_dict_copy = copy.deepcopy(elena_dict)#.copy()
                hansel_dict_copy = copy.deepcopy(hansel_dict)#.copy()

                # Update the matched_number for the elena_dict_copy and hansel_dict_copy
                update_matched_number(max_hansel, k, n, elena_dict_copy, hansel_dict_copy)

                max_hansel_copy = max(max(elena_dict_copy.values(), key=lambda x: x.matched_number).matched_number, max(hansel_dict_copy.values(), key=lambda x: x.matched_number).matched_number)

                if max_elena_copy > max_hansel_copy:
                    matched_sol = max_elena
                else:
                    matched_sol = max_hansel
        # else, choose the biggest
        else:
            matched_sol = max_elena if max_elena.matched_number > max_hansel.matched_number else max_hansel

        ans += matched_sol.matched_number # Update the answer


        # Logs
        # print(max_elena)
        # print(max_hansel)

        # Update elements with the same range or overlapping range with the matched element
        update_matched_number(matched_sol, k, n, elena_dict, hansel_dict)
        # Add the element back to the result

        p -= 1

    return ans
```

#### Algoritmo de Programación Dinámica
Este no llegó a impolementarse, pero mientras se analizaba el problema se pudo notar que era posible implementar un algoritmo de este tipo apoyándonos en una matriz o varias listas para guardar los valores, primero obteniendo los mejores para cualquier intervalo con $p=1$, luego con $p=2$ y seguirnos apoyando en los menores $p$ para obtener $p$ mayores, guardando todos estos valores en la matriz o la lista. La idea sería parecida a la llevada a cabo en el algoritmo $div\_n\_con$. Ir buscando si es mejor mirar hacia la derecha, hacia la izquierda o si es mejor no mirar para este $p$ que se consumirá, lo que por supuesto, al ser una solución que utiliza programación dinámica nos apoyaremos en los mejores valores que ya hemos ido encontrando para valores de $p$ menores que en el que nos encontremos analizando en cada iteración.