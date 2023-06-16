
# Tercer Proyecto de Diseño y Análisis de Algoritmos


## Carlos Carret Miranda C-412

<!-- ###Enunciado del problema -->

### Sin imaginación

Kevin estaba leyendo un libro sobre Diseño y Análisis de Algoritmos
cuando se topó con un problema que llamó su atención. El texto era el
siguiente:

Se tiene un grafo bipartito $G$ con $U$ nodos en la primera parte y $V$ nodos en la segunda parte. Un subgrafo de $G$ está $k$-cubierto si todos sus
nodos tienen al menos grado $k$. Un subgrafo $k$-cubierto es mínimo si su cantidad de vértices es la mínima posible. Encuentre el mínimo grafo
$k$-cubierto para todo $k$ entre 0 y $MinDegree$ (grado mínimo del grafo $G$).

Luego de entender el problema, automáticamente pensó dos cosas:

-   Quiero resolver este problema.

-   ¿A los profesores se les habrá acabado la imaginación para los textos de los proyectos?


### Descripción del problema

El texto presenta un problema de optimización en el contexto de grafos bipartitos, en el que se busca encontrar el mínimo grafo $k$-cubierto para todo $k$ entre 0 y el grado mínimo del grafo $G$. Un subgrafo $k$-cubierto es aquel en el que todos sus nodos tienen al menos grado $k$, y es mínimo si su cantidad de aristas es la mínima posible. 

Es importante destacar que en caso de que el grado minimo sea 0, es decir, que exista algun nodo que no tenga arista hacia el, se debera de tener en cuenta para dar la respuesta para cuando $k$ sea igual a 0.

Se debe encontrar una estrategia tramposa que permita a Tito observar las respuestas de Hansel y Elena de tal forma que pueda responder la mayor cantidad posible de preguntas correctamente.

Aspectos a destacar del problema:
- Se trata de un problema de optimización.
- El problema se enfoca en un grafo bipartito con nodos en dos partes distintas ($U$ y $V$).
- Se define un subgrafo $k$-cubierto como aquel en el que todos sus nodos tienen al menos grado $k$.
- Se busca encontrar el mínimo grafo $k$-cubierto para cada valor de $k$ entre 0 y el grado mínimo del grafo $G$.
- Este problema puede ser transformado a otro de flujos que sea mas facil de solucionar.
- Sera necesario utilizar alguna estructura de datos para el manejo de grafos.

Ideas para atacar al problema
* Primeramente se busca dar solución al problema mediante la recursividad y fuerza bruta. Con esto buscamos resolver el problema para obtener resultados lo suficientemente correctos para luego compararlos con otras soluciones que sean mejores.
* Observando un poco la manera de escoger cuales aristas pertenecen a nuestra solucion poco a poco se va pensando en una estrategia utilizando flujos para dar solucion a nuestro problema.


### Herramientas y código auxiliar
Para la realización de este proyecto se utilizó Python en su versión 3.7.4.
Se crearon las clases SOL y AlgSol que se encuentran en el archivo $sol.py$, así como otros métodos auxiliares útiles para el manejo de las estructuras de datos y las soluciones que se van conformando.
Las clases SOL y AlgSol son utilizadas para representar soluciones, dígase solución la secuencia de selecciones que se hacen a medida que se escogen ciertas aristas.

La clase SOL tendría un entero $k$ que sería el grado minimo de todos los vertices que pertenecen a seleccionar las aristas representadas por los indices que esten en $True$ en el arreglo $mask$ al indexar en el arreglo $edges$. La variable $count$ representa la cantidad de aristas necesarias (o seleccionadas en $mask$ como True) para esta solucion.

Para el caso de la clase AlgSol se espera que se pase en la variable minimums un diccionario con cada llave siendo el varlor de $k$ y cada valor asociado siendo la cantidad de aristas necesarias(mínimas) para que el grafo sea $k$-cubierto. La variable edges es opcional y sería una representacion de estas aristas, de forma que el usuario la use a su conveniencia.

También contamos con el método estático AlgSol.compare_sol(ans, sol), el cual utilizaremos para comparar 2 soluciones que contengan ambas todos los valores de $k$, para $0 \leq k \leq minDegree$ y sus valores de cantidad de aristas minimas correspondientes.

En lo adelante nos referiremos a una solución como una concatenación de selecciones(SOL) o un diccionario donde este contiene las soluciones desde $k = 0$ hasta $k = minDegree$.

También, a lo largo del texto nos referiremos a minDegree como el valor de grado mínimo que pueden tener los vértices de nuestro grafo.

```python
class SOL:
    def __init__(self, k: int, mask: bool, edges: list, count: int) -> None:
        self.k = k
        self.mask = mask
        self.edges = edges
        self.count = count

class AlgSol:
    def __init__(self, minimums: dict, edges:list = []) -> None: # Minimums debe de ser un diccionario donde las llaves seran los valores de k y los values seran la cantidad minima necesaria de aristas
        self.minimums = minimums
        self.edges = edges

    @staticmethod
    def compare_sol(correct_sol, target_sol):
        for i in range(len(correct_sol)):
            if correct_sol[i] != target_sol[i]:
                return False
        return True
 
```
### Generador
```python
def problem_generator():
    n_u = random.randint(1, 3)
    n_v = random.randint(1, 3)
    edges_count = random.randint(max(n_u, n_v), 20)
    edges = []
    for i in range(edges_count):
        edges.append((random.randint(1,n_u), random.randint(1, n_v)))

    filename = save_params(n_u, n_v, edges)
    print(f"Problem saved in {filename}")

    return n_u, n_v, edges
```

### Tester
```python
def test_sol(n_u, n_v, edges, sol, method="bf", test_alg_time=""):
    ans = 0

    ts = time.time()
    
    if method == "bf":
        ans = bf.solve(n_u, n_v, edges)
    elif method == "max_flow":
        ans = max_flow.solve(n_u, n_v, edges)

    te = time.time()
    time_str = f"Time: {round(te-ts, 5)}"

    if AlgSol.compare_sol(ans, sol):
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
Se generan todas las combinaciones que se pueden escoger de entre las m aristas que contiene el grafo G. Para cada combinacion generada se verifica el grado minimo que contienen nuestros vertices. Si este grado minimo es menor o igual que minDegree, entonces se procede a actualizar nuestro variable(diccionario) que contiene todos los grados posibles(k) con su valor de cantidad de aristas minimas, asi como las aristas que se escogieron.

El algoritmo consta de dos llamados recursivos y un caso de parada. El primer llamado recursivo se utiliza para avanzar una posicion en el indice actual de las aristas que se estan escogiendo sin tener en cuenta a la arista que se encuentra en la posicion actual, es decir, en la solucion que estamos conformando si entramos en este llamado recursivo, siendo el indice actual i, la arista ubicada en la posicion i del arreglo $edges$ no se encontrara entre las aristas que hacen que nuestro grafo k-cubierto sea minimo para el k en el que se obtuvo al evaluar la solucion que se esta conformando actualmente. Para el caso del segundo llamado recursivo, la diferencia con el primero seria que esta vez si se tiene en cuenta la arista ubicada en el indice i.

Llegaremos al caso de parada cuando nos encontremos en el indice i = cantidad de aristas que contiene el grafo $G$. Luego se llamara al metodo evaluate, el cual primero verificara que todos los nodos tengan grado mayor igual que uno. En el caso de que sea 0, no tendriamos un grafo k-cubierto. Luego, obtenemos el menor grado de esos vertices y comparamos si es menor o igual que el grado minimo(minDegree).
Por ultimo, actualizamos nuestra solucion que contiene todos los valores posibles de k con sus respectivos valores de la cantidad de aristas minimas. En caso de que la solucion con la que contamos actualmente requiera un numero menor de aristas, no actualizamos nada y seguimos con la ejecucion de nuestro algoritmo.

##### Correctitud
Prácticamente con nuestro algoritmo estamos probando todas las maneras posibles mediante las cuales se pueden escoger desde 0 hasta m aristas.
Luego, con demostrar que nuestro algoritmo las genera todas y que siempre garantizamos quedarnos con el minimo de aristas necesarias para k, 0 <= k <= minDegree nos basta para afirmar que nuestro algoritmo nos devuelve soluciones correctas.

##### Genera todas las posibles selecciones
Para demostrar que nuestro algoritmo genera todas las posibles selecciones nos apoyaremos en un poco de combinatoria.

Si para cada posición($i$, donde $i$ es la arista $i$-esima) podemos escoger que la arista $i$ será tomada en cuenta en la solucion que se forme para determinado k y las siguientes $n-i$ aristas pueden ser escogidas igualmente, podemos notar que en el momento en el que se escoge la arista $i$ nos quedan $m-i$ * ($cantidad-de-formas-escogiendo-arista-i$ + $cantidad-de-formas-sin-escoger-arista-i$) .

Entonces, podemos partir de que en cada llamado recursivo estamos analizando una solución en la cual se tiene en cuenta el índice de la arista $i$  o no se tiene en cuenta. De este modo, para cada índice $i$, nos faltarían analizar los $n-i$ restantes. Luego, debido a la forma en la que funciona la recursividad, se cumplirá que para cada $i$, se analizan los $2$ casos por separados. Entonces es seguro que para todo índice $i$ se exploran todas sus posibles vías sin repetir alguna y para los restantes $n-i$ índices que se iran conformando en la ejecución del algoritmo se repite el proceso, es decir, también se escogen las $2$ posibles opciones posibles en cada uno de los $n-i$ índices.

###### Demostrar que siempre obtenemos el minimo de aristas necesarias para cada k
En nuestro algoritmo solamente se modifica el valor de cantidad de aristas necesarias para k en el metodo evaluate y solamente si se cumplen las condiciones de que todos los vertices tengan degree mayor que 0 y q el mismo sea menor que minDegree.
Luego, al llamar al metodo update_minimums(mask, minimums, deg, edges), sera necesario que se cumpla la invariante de que minimums[deg].count > count, es decir que el valor actual minimo sea mayor que el nuevo valor de la solucion formada. Luego para valores que sean mayores no ocurriran cambios, por tanto siempre nos quedaremos con el menor valor posible.
El otro caso posible que puede ocurrir en cuanto a agregar algun valor a nuestro diccionario que contiene todos los valores minimos es que no se encuentre ningun par <llave,valor> para cierto $k$, en este caso se agrega el valor y luego se regresaria al primer caso que se menciono anteriormente, en el cual se cumpliria la invariante.

##### Complejidad Temporal
Evaluar la solución conformada será $O(n_u+n_v)+O(m)+O(n_u+n_v)$ lo anterior respecto a antes del metodo de update_minimums(), es decir, el metodo same_degrees(), luego para el caso del metodo update_minimum tenemos: $O(m)$ quedandonos un total de $O(n_u+n_v) + O(m)$ a lo sumo, siendo m la cantidad de aristas y n_u la cantidad de vertices pertenecientes a U y n_v la cantidad de vertices pertenecientes a V. Esta evaluación de la solución sería recorrerla completa y para cada selección recorrer su rango, es decir $k$ elementos.
$2T(m-1) + O(n_u+n_v+m)$
Debido a que probablemente $m\geq n$
Por el Teorema maestro, tenemos:
$a = 2, b = 1$ => $T(m) = a^{m/1} + m = O(2^{m} + m)$

```python
def bf(n_u: int, n_v: int, edges: list, mask: list, index: int, minimums: dict, min_degree)-> None:
    # If ends
    if index == len(edges):
        evaluate(n_u, n_v, edges, mask, minimums, min_degree)
        return
    # Update minimums

    # LLamar al metodo recursivo sin tener en cuenta esta arista
    bf(n_u, n_v, edges, mask, index+1, minimums, min_degree)

    mask[index] = True
    bf(n_u, n_v, edges, mask, index+1, minimums, min_degree) # Llamar al metodo recursivo teniendo en cuenta esta arista
    mask[index] = False
```

#### Metodo De Flujo Maximo (Max Flow)

#### Idea
Luego de resolver el problema medianta recursividad y fuerza bruta, se pudo notar que este problema era parecido a resolver otros problemas, como por ejemplo, problemas relacionados con grafos bipartitos y flujos. Entonces se procede a buscar como darle solucion utilizando flujos, ya que se sabe que una vez que se obtenga una solucion utilizando por ejemplo, flujo maximo, tendremos un arma poderosa, la cual como dimos en clases sabremos que nos devuelve una solucion correcta.

Primeramente se procede armando un nuevo grafo de la siguiente manera: conectamos la fuente a cada vértice de la parte izquierda(vértices pertenecientes a U) con arista con capacidad deg_u - k(donde deg_u es el grado del vértice), luego transformamos cada arista del grafo original en una arista dirigida con capacidad 1. Despues conectamos cada vertice de la parte derecha(vértices pertenecientes a
Luego de tener nuestro grafo conformado procedemos a buscar el grado minimo en el mismo, es decir minDegree, hacemos a $k = min(0, minDegree)$ e iteramos k veces(donde $0 \leq k \leq minDegree$) repitiendo el siguiente procedimiento: 
- Hallamos el flujo maximo utilizando bfs. 
- Nos quedamos con las aristas que no hayan sido saturadas. 
- Aumentamos en 1 el flujo de las aristas que se tenia en la iteracion anterior.
- Extraemos las aristas que no esten saturadas y estas seran las aristas que pertenezcan a nuestra solucion para este valor de k.
- Por ultimo decrementamos a k en 1.
- Cuando el valor de $k$ sea menor o igual a 0 se detiene la ejecucion del ciclo while.

Para la creacion de nuestro algoritmo creamos una clase $Graph$ y una clase $Edge$, ambos en el archivo $graph.py$. La clase $Graph$ representara a un grafo bipartito.
Al principio en el diccionario u_djacency_list de la clase $Graph$ se iran insertando las aristas dirigidas desde los nodos de $U$ hacia los de $V$, pero a su vez también se insertarán las aristas en sentido contrario desde $V$ hasta $U$, para que estas funcionen como aristas de la red residual luego al ejecutar el algoritmo de flujo máximo.

#### Correctitud
Para la demostracion de nuestro algoritmo debemos de demostrar el porque este nos proporciona una respuesta válida. Para ello nos enfocaremos en porque son esas aristas no saturadas las que forman la respuesta correcta.

Debido a que a cada arista desde $s$ hasta $u \in U$ y desde $t$ hasta $v \in V$ le estamos dando $degre = deg_u - k$, con esto estamos diciendo que al intentar mandar flujo, se saturarán aquellas aristas que influyen en que estos vertices $u's$ y $v's$ tengan grado $deg_u-k$, pero como tal a nosotros nos interesa que tengan al menos grado $k$, luego en ese instante nos quedarian $m_{uf} = m_u - (deg_u - k)$ de las $m_u$ aristas que se conectaban con el vértice $u$. Como $k$ va desde minDegree hasta 0, para valores mayores de $k$ tendremos menor cantidad de aristas saturadas y para menores valores de $k$, el caso contrario. Lo que si debemos de darnos cuenta es que con esa cantidad de aristas que quedaron siendo $m_{uf}$ se puede lograr mantener todos los vértices con al menos el mismo degree, ya que nos quedamos en un comienzo con $k$ como el minDegree o 0, es decir, en todo momento los vértices tendrán valor mayor o igual a $k \leq minDegree$, incluso luego de quitarles las $(deg_u) - k$
aristas.

#### Complejidad Temporal
Primeramente iteramos por cada vertice $O(n_u+n_v)$. Luego, iteramos por cada arista y puede que en esos momentos recorramos cada vértice o arista para ver si ya se encuentra, luego $O((n_u+n_v) * m)$. Luego hacemos varios recorridos por los vertices y las aristas, es decir, nada muy grande comparado con el costo calculado hasta el momento. Luego llegamos al ciclo while desde k=minDegree hasta 0, en este ciclo, el bfs costara a lo sumo $O(V+E)$ y por último tenemos que debido a que el flujo máximo en la red es a lo sumo m y no se realizarán más de m búsquedas que no aumenten el flujo, nuestra solución tendrá una complejidad temporal de $O((n+m)^{2})$, lo cual es mayor que lo calculado hasta el momento.

```python
def solve(n_u, n_v, edges: list):
    edges = [(u-1, v-1+n_u) for (u, v) in edges]

    s = -1  # Source
    t = n_u + n_v  # Sink

    g = Graph(n_u, n_v, dict(), dict(), s, t)

    # Building graph edges
    for index, (u, v) in enumerate(edges):
        # u,v = edge
        if g.has_undirected_edge(u, v):
            # Debido a que la arista se encuentra repetida, se agrega un vertice intermedio entre la arista nueva que se creara, de esta manera si antes se tenia la arista (u,v) ahora se tendran las aristas (u,i) e (i,v), todas con capacidad=1
            g.add_cross_edge(u, v, (-index)-1, 1)
        else:
            g.add_edge(u, v, index, 1)

    # Hallando min_degree
    min_degree = 1e8
    for adjacency_list in g.u_adjacency_list.values():
        # has_cross_edges = [True for edge in adjacency_list if edge.u < 0]
        min_degree = min(min_degree, len(adjacency_list))

    k = min_degree
    # Agregando aristas desde s hasta los nodos de U y desde los nodos de V hasta t
    for u in g.u_vertex:  # Agregando para s
        if not g.u_adjacency_list.__contains__(u):
            return {0: 0}
        g.add_edge(s, u, s, len(g.u_adjacency_list[u]) - k)

    for v in g.v_vertex:  # Agregando para t
        if not g.u_adjacency_list.__contains__(v):
            return {0: 0}
        # Las aristas desde v-> u serian las aristas de retroceso que tendria la red residual
        g.add_edge(v, t, t, len(g.u_adjacency_list[v]) - k)

    # Loop para iterar desde 0 hasta k
    ans = dict()
    list_ans = []
    while k > 0:
        max_flow(s, t, g)
        sol_edges = get_unsaturated_edges(n_u, n_v, g)

        print(sol_edges)
        augment_flow(1, g)

        # Updating answer
        ans[k] = len(sol_edges)
        list_ans.append((k, sol_edges))

        k -= 1

    ans[0] = 0
    show_answer(list_ans)
    return ans
```