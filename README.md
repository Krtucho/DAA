
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

### Ideas para atacar al problema
* Primeramente se busca dar solución al problema mediante la recursividad y fuerza bruta. Con esto buscamos resolver el problema para obtener resultados lo suficientemente correctos para luego compararlos con otras soluciones que sean mejores.
* Luego se realizaron modificaciones al algoritmo de fuerza bruta para obtener una solución mas eficiente. Se agrega un diccionario para guardar todas aquellas selecciones de $p$ miradas y no repetirlas, de esta forma se poda la búsqueda de soluciones repetidas o que no tendrían mucho sentido. Se realizaron pruebas con los datos de entrada para ver si el algoritmo obtenía resultados correctos.
* Siguiendo el camino de la recursividad y las mejoras a nuestro algoritmo, se puede notar que cada vez que vamos a escoger hacia que lado mirar, digamos consumir una instancia de $p = 1$, estamos escogiendo si mirar hacia la izquierda, derecha o si no mirar hacia ningún lado y mirar para el siguiente $p$. Es decir, nos encontramos con que podemos escoger entre 3 elecciones y nuestro problema quedaría subdividido en 3 subproblemas, por tanto, podemos hacer uso de la técnica de divide y vencerás para luego quedarnos con la solución que nos aporte un mayor número de preguntas respondidas.
* Observando un poco la manera de escoger hacia que lado mirar y la manera en que se resuelve el problema, se puede notar que la estrategia golosa es una buena opción para resolver el problema. Esto se debe a que siempre nos queremos quedar con el valor óptimo, por tanto, podemos escoger la mejor opción en cada momento y así obtener la solución óptima.
* Siguiendo una idea parecida a la de divide y vencerás podemos darnos cuenta que al dividir nuestro problema en subproblemas podemos utilizar programación dinámica para obtener una solución más rápida y que consuma menos memoria.

% Herramientas y codigo auxiliar
Para la realizacion de este proyecto se utilizo Python en su version 3.7.4.
Se crearon las clases SOL y MatchedSOL que se encuentran en el archivo sol.py, asi como otros metodos auxiliares utiles para el manejo de las estructuras de datos y las soluciones que se van conformando.
Las clases SOL y MatchedSOL son utilizadas para representar soluciones, digase solucion la secuenta de selecciones que se hacen a medida que se escoge si mirar hacia el examen de elena a k preguntas o al de hansel a k preguntas.
Entonces estas clases tendrian un string que seria el nombre de la persona a la cual se observa el examen, un intervalo representado por una instancia del tipo range() que nos brindara informacion sobre que intervalos se escoge, es decir, se busca a partir de la pregunta i hasta la i+k, siendo i<=n-k.
Para el caso de la clase MatchedSOL tambien tendremos una lista de tipo bool de tamanno n que nos dira cuales preguntas tenia respondida esta persona en el intervalo desde i hasta i+k, asi como una variable para almacenar la cantidad de estas preguntas respondidas.

En lo adelante nos referiremos a una solucion como una concatenacion de selecciones(SOL)

% Algoritmo de solución

% Fuerza Bruta Backtracking - bf
% Idea Intuitiva
La idea intuitiva que se sigue en este algoritmo es la siguiente:
Se generan todas las combinaciones que puede escoger Tito mirando hacia ambos lados. Recalcar que en el primer algoritmo recursivo de backtrack que se crea se pueden tener selecciones repetidas. Por ejemplo, se puede mirar a la hoja de Hansel a las preguntas 1+k y luego volver a mirar a la hoja de Hansel a las preguntas 1+k, repitiendo asi
una seleccion y consumiendo 2 oportunidades, quedandonos solamente p-2 oportunidades para encontrar mas respuestas.
El algoritmo consta de dos ciclos for que llaman en su interior al metodo recursivo, que es en si mismo quien contiene el doble ciclo for. En el primer ciclo se itera por las personas disponibles para que Tito se fije, es decir Elena y Hansel (llamemosles dominios). En el segundo for se itera por los distintos intervalos que se pueden escoger de i+k preguntas.
Iterando desde i=0 hasta i=n+k-1, de esta manera no estamos teniendo en cuenta las soluciones de las ultimas n-k veces, ya que serian redundantes y estariamos repitiendo selecciones que ya tuvimos en cuenta, debido a que al escoger i=n-k+1 solo podemos obtener un menor valor de cantidad maxima de respuestas correctas al escoger n-k+2, n-k+3,...n-k+n.
Luego de esta forma estariamos escogiendo todas las posibles formas de seleccionar hacia donde mirar p veces.

Como caso de parada de nuestro algoritmo tenemos que cuando p sea 0 se detenga. En cada llamado recursivo vamos decrementando p y de esta forma sabemos que en el siguiente llamado recursivo tenemos que llamar recursivamente de nuevo p-1 veces que seran las restantes veces que Tito podria mirar hacia la hoja de Elena o la de Hansel.

% Demostracion de que esto funciona
Practicamente con nuestro algoritmo estamos probando todas las maneras posibles mediante las cuales se puede escoger hacia donde mirar p veces, solamente obviando aquellas selecciones donde se repiten respuestas que ya obtuvimos y que por tanto ya estan contenidas en otra, es decir las ultimas n-k.
Luego con demostrar que nuestro algoritmo las genera todas y que esas ultimas ya estan contenidas en otras nos basta para afirmar que nuestro algoritmo nos devuelve valores correctos.
Para demostrar que nuestro algoritmo genera todas las posibles selecciones nos apoyaremos en un poco de combinatoria.

Si para cada posicion(i donde i es la pregunta i) podemos escoger que la pregunta i sera escogida de elena o hansel y las siguientes n-i preguntas pueden ser escogidas de ambos igual, podemos notar que en el momento en el que se escoge la pregunta i nos quedan n-i * (cantidad de formas eswcogiendo primero elena + cantidad de formas escogiendo primero hansel) .
Diremos que el primer for se encarga de escoger primero a elena y luego a hansel, para asi calcular la cantidad de veces en la que primero escoge elena y en la que primero escoge hansel las restantes n-i preguntas. Mientras que el segundo ciclo for se encarga de brindarnos la posibilidad de movernos entre esas n-i preguntas, repitiendo las anteriores que sean menores que i en algunos casos, pero nos da igual porque al estar repetidas no influiran en el conteo a la hora de buscar el maximo.
Solo nos volvera mas ineficiente nuestro algoritmo, pero podemos continuar con la idea principal de que hasta el momento i se escogieron de alguna forma i preguntas, mirando hacia el examen de Elena o al de Hansel y sumando hasta el momento n preguntas correctos, nos falta entonces averiguar de las restantes n-i preguntas cuantas posibilidades tenemos. 

% Demostrar n-k
Con respecto a la demostracion de las ultimas n-k preguntas, se sabe que Tito puede ver desde la pregunta i hasta la i+k en cada mirada que hace a las hojas de Elena o Hansel, entonces cuando TIto mira a la pregunta i, este puede mirar la i + 1, i+2,...i+k, para el momento en que i = n-k, entonces Tito puede ver las preguntas n-k + 1, n-k+2,...n-k+k = n => TIto pudo ver las ultimas n-k preguntas que tenia respondidas Elena o Hansel mirando una sola vez.
Si permimos que Tito observe los proximos intervalos de (i=n-k, n-k+k), (n-k+1, n-k+k+1),(n-k+2, n-k+k+2),...,(n-k+n, n-k+k+n) nos damos cuenta de que solo estamos repitiendo respuestas porque en todos los casos el maximo de nuestro intervalo es n y en el primer caso al analizar i=n-k ya obtuvimos todos los valores en ese intervalo.

% Complejidad Temporal
Como podemos ver estamos buscando todas las posibles variaciones con repeticion en un arreglo de tamanno n, teniendo como dominio un conjunto con 2 posibles valores para ubicar en cada posicion del arreglo. Luego nos queda que tendra una complejidad de:
T(n) = 2 elevado_a n + O(n*k)

% Fuerza Bruta Optimizada Backtracking con podas - bf_opt

% Idea
La idea es similar a la que sigue el algoritmo de fuerza bruta sin podas. La diferencia recae en la adicion de un diccionario para conocer en todo momento cuales selecciones ya han sido agregadas y de esta forma no repetir selecciones de una seleccion(SOL) que se encuentre en cierto rango. Si una seleccion ya fue agregada al diccionario, al indexar en la misma de la forma sols_dict[f"{domain}_{start_range}_{stop_range}"] obtendremos el valor de True si ya se esta utilizando en la confeccion de la solucion actual y el valor de False o que no se encuentra la llave en el caso contrario.

Se agrega como comprobacion al inicio lo siguiente k == n or n <= k*p y en caso de cumplirse alguna de las mismas se evalua la solucion que se esta formando actualmente. La idea detras de esto es que para el primer caso, si k==n, se estaria diciendo que si con p=1 puedo ver todas las respuestas en el examen de elena o hansel, pues que intento ver cuales se obtienen y no tengo que revisar solamente cuando p se haga 0.
En el caso de n <= k*p, se esta diciendo que si tenemos suficientes oportunidades de ver todas las preguntas(n, seleccionandolas una por una) con las k*p selecciones. Pues deberiamos de analizar esta solucion, ya que probablemente se encuentre entre las mejores selecciones de una solucion que podemos conformar.

% Correctitud
Debido a que este algoritmo es similar al de backtrack nos centraremos en las partes que fueron agregadas. Se puede asumir que las explicaciones restantes serian una copia de las explicaciones que se usaron para demostrar el backtrack sin podas.

% No repeticiones
Primeramente comencemos por demostrar que al agregar el nuevo diccionario las soluciones dejan de repetir ciertas elecciones que no nos aportaran mucho y solamente haran nuestro algoritmo aun mas costoso.
Para ello nos centraremos en las lineas donde se agrega al diccionario la nueva llave con la eleccion tomada en este instante antes de llamar recursivamente, tambien luego de salir del metodo recursivo, al modificar el valor en la llave que contiene a esta eleccion, poniendolo en False.
Al comienzo del doble ciclo for se esta verificando que la nueva eleccion no se haya tomado anteriormente, para ello se verifica su existencia en el diccionario sols_dict. 
Podemos decir que una vez se haya tomado esta eleccion al llamar recursivo no se volvera a tomar en los siguientes llamados, solo cuando se llegue a un caso de parada y se retorne se volvera a tener en cuenta esta eleccion.

% Genera todas las combinaciones
Demostremos entonces que esta solucion, en efecto, nos genera todas las posibles combinaciones que nos interesan, sin tener las repetidas y que esto da solucion a nuestro algoritmo.

Sabiamos que antes obteniamos el conjunto de todas las posibles formas de escoger p veces intervalos de tamanno k tanto de elena como de hansel. Al agregar a nuestra solucion el nuevo diccionario con sus respectivos codigos estamos eliminando el conjunto de soluciones donde se encuentra al menos una eleccion repetida(elemento de tipo SOL), por tanto obtenemos como resultado el conjunto de soluciones donde no se repiten 2 elecciones. Es decir no ocurre que:

Se puede mirar a la hoja de Hansel a las preguntas 1+k y luego volver a mirar a la hoja de Hansel a las preguntas 1+k, repitiendo asi
una seleccion y consumiendo 2 oportunidades, quedandonos solamente p-2 oportunidades para encontrar mas respuestas. Como bien habiamos dicho que ocurria en la solucion de fuerza bruta.

Luego tenemos que:
conjunto resultante =  (conjunto de todas las combinaciones) - (conjunto de combinaciones que repiten al menos 1 eleccion)

Como no nos interesa repetir elecciones en nuestra solucion, podemos decir que el conjunto resultante nos resuelve nuestro problema. Por tanto, nuestro algoritmo funciona correctamente.

% Complejidad Temporal
Similar al algoritmo de fuerza bruta. 

% Divide y Venceras - div_n_con

% Idea
La idea a seguir es irnos moviendo en las p elecciones que podemos tomar a traves de las n preguntas que tenemos que responder y darnos cuenta de que tenemos 3 posibles elecciones para tomar en la eleccion numero i que influira en las elecciones i + 1, i + 2,..., i + k, siendo i+k<=p.
Para ello en cada llamado recursivo podremos seleccionar y subdividir nuestro problema en 3 nuevos problemas, restar 1 al valor de p y seleccionar mirar hacia la hoja de Elena, restar 1 al valor de p y seleccionar mirar hacia la hoja de hansel.
no restar 1 al valor de p y no mirar ni a la hoja de elena ni a la de hansel en este eleccion.

Destacar que cada vez que llamamos recursivamente a alguno de estos casos estamos creando una copia de la lista que tengamos actualmente y concatenando un elemento a esta que seria la eleccion que tomamos.
Luego, al encontrarse en algun caso de parada 

Como casos de parada tenemos que:
1- Si n - k <= pos - 2. En este caso estamos analizando que el indice de la pregunta actual por la que nos estamos moviendo sea menor que n-k, tomando en cuenta n-k-1, debido a que se puede optar por revisar 1 vez con n-k a elena y otra vez con n-k a hansel. De esta manera, aunque nuestro p aun no sea 0
podemos retornar en uno de nuestros llamados recursivos sin necesidad de probar las p veces restantes alguns soluciones que repetirian las que ya buscamos.
2 - Si p == 0. Este caso es utilizado en los momentos en que ya hemos hecho p elecciones.

% Correctitud
% Debemos demostrar que nuestro algoritmo analiza todas las posibles combinaciones que influyen en la seleccion del valor maximo de la cantidad de preguntas correctas que se pueden obtener. En el caso de este algoritmo cabe destacar que no se repiten elecciones en cada solucion, esto tambien lo demostraremos.

Para la primera parte, podemos partir de que en cada llamado recursivo estamos analizando una solucion en la cual se agrega el indice de la pregunta i siendo respondida por elena, hansel o por ninguno de ambos. De este modo, para cada indice i, nos faltarian analizar los n-i restantes. Luego, debido a la forma en la que funciona la recursividad, se cumplira que para cada i, se analizan los 3 casos por separados. Entonces es seguro que para todo indice i se exploran todas sus posibles vias sin repetir alguna y para los restantes n-i indices que se iran conformando en la ejecucion del algoritmo se repite el proceso, es decir, tambien se escogen las 3 posibles opciones posibles en cada uno de los n-i indices.

% No repeticion de soluciones

Debido a que en cada llamado recursivo llamamos aumentando i en 1 hacia un mayor valor que cada vez se acerca mas a n, no sera posible repetir una seleccion que se haya escogido en una misma solucion. Para mostrar mejor esto podemos decir que para todo valor de i, i < n, se escoge persona_x con preguntas i hasta k y en el llamado con i+n, no existe forma de volver a escoger persona_x con preguntas i hasta k, debido a que en los siguientes llamados se llama como minimo con i+1 y tampoco podria repetirse desde antes porque en los llamados anteriores se hicieron con i - x, donde x <= i. Por tanto no se volveria a crear una seleccion con i para todo i, i < n y no tendriamos soluciones con selecciones repetidas.

% Complejidad Temporal
Evaluar la solucion conformada sera O(n*k) a lo sumo, donde k < n para valores grandes de k. Esta evaluacion de la solucion seria recorrerla completa y para seleccion recorrer su rango, es decir k elementos.
3T(n-1) + O(n)

Por el Teorema maestro, tenemos:
a = 3, b = 1 => T(n) = a elevado_a n/1 + n = O(3 elevado_a n + n)

% Solucion greedy(golosa) - greedy

<!-- Idea -->
En este algoritmo se hara un uso mas extenso de la clase MatchedSOL.
Primero se crean dos diccionarios para ubicar en estos los valores de cantidad de soluciones en intervalos cualesquiera.
Se itera desde 0 hasta n-k+1 para ir ubicando en cada diccionario las selecciones que pueden hacerse para los rangos desde i hasta i+k. Estas selecciones se van agregando de manera tal que en todo momento obtengamos la cantidad de preguntas correctas que tenian elena y hansel, en un diccionario para las de elena y otro para las de hansel respectivamente. Para ello se cuenta con la clase MatchedSOL y sus arreglo de tipo bool para decirnos en cada posicion cual se encuentra respondida correctamente y un entero con la cantidad de estas preguntas que se haya respondido.
Luego pasamos al procedimiento principal de nuestro algoritmo, en este se tiene un ciclo for que iterara p veces, donde cada vez nos iremos quedando con la seleccion que nos brinde mas respuestas correctas, siguiendo asi una estrategia golosa.
Buscaremos el valor maximo en cada diccionario para asi saber cual seleccion escoger, en caso de coincidir estos valores procedemos a ver si sus rangos se superponen de alguna forma, en caso de que no se superpongan procedemos a escoger cualquiera, en otro caso tendremos que analizar que sucede en el siguiente paso, es decir, al reducir p en 1 al escoger como siguiente mirar hacia elena o hacia hansel. En caso de volver a coincidir ambos valores al buscar el maximo siguiendo el procedimiento que se menciono anteriormente, escogemos por defecto a Elena para que luego en la siguiente iteracion al restarle 1 a p esta vez, se pueda volver a buscar un nuevo maximo y repetir este procedimiento. Destacar sobre esta ultima parte del algoritmo, que en caso de querer obtener mayor seguridad a la hora de hallar el maximo siguiendo esta via en este instante que se tiene este p y ambos valores coinciden, se podria llevar a cabo una busqueda mas profundas para valores menores que p hasta que no se encuentre conflicto conque ambos valores coincidan, pero en ese caso el costo computacional de la solucion aumentaria.
Luego de escoger esta mejor seleccion, pasamos a modificar aquellas selecciones cuyos rangos se superponen de alguna forma con el rango de la seleccion escogida.

<!-- Correctitud -->
En cada iteracion del algoritmo nos estamos quedando con la eleccion que nos brinde la mayor cantidad de respuestas que podemos escoger en ese instante o sino la mayor cantidad de respuestas que podamos escoger en total a lo largo del algoritmo.
Debemos de demostrar como ambas selecciones nos brindan al final la mejor solucion. Es decir, como escogemos entre cada subproblema el optimo.

Practicamente siempre queremos quedarnos con lo mejor y podemos afirmar que esta es la via a seguir ya que si puedo escoger de cierta forma mas respuestas que de otra forma, escojo la que mas respuestas me brinde. En caso de que ambas se superpongan podemos decir que la que mas nos aporte puede contener a la que menos nos aporte, en este caso, prefeririamos escoger la que contiene a la que menos nos otorga. Para el caso en que no se superpongan, ambas se encontrarian en rangos aislados uno del otro, en este caso, nos queremos quedar con la mejor respuesta porque en caso de no escoger la mayor, no encontrariamos nada mejor que esa mayor que no escogimos, en otras palabras todas las restantes serian menores o iguales que la que no es la mayor. En caso de que se superpongan pero ninguna contenga completamente a la otra, se tendria que buscarla mejor forma de escoger las soluciones dando 1 o mas pasos probando asi para menores valores de p. Los pasos anteriormente descritos son los que sigue nuestro algoritmo y luego de llevarlos a cabo se puede afirmar que siguiendo esa estrategia nos podemos quedar en todo momento con la mejor solucion.

Destacar que en nuestro algoritmo no se tiene en cuenta el caso en que se tengan 2 selecciones de una misma persona con el mismo numero de respuestas correctas y que este numero sea el maximo. Para dar solucion al mismo se puede seguir el mismo enfoque del cual se hablo o que se sigue para el caso en que tanto las selecciones con los valores maximos de Elena y Hansel coincidan.

% Complejidad Temporal
Primero tenemos un ciclo for desde 0 hasta n-k+1(desde 1 hasta n-k). Este tendria a lo sumo complejidad n, dado que n >= k.
Luego se itera por cada elemento agregado al diccionario para confeccionar su lista de respuestas correctas y su entero con la cantidad de respuestas correctas que tenga.
En estos 2 dobles ciclos for, un doble ciclo para Elena y otro doble ciclo para Hansel, se iteran n * k veces, donde k representa el rango. Destacar que para un valor de k muy alto, k=n, esta parte del codigo parece que tomaria O(n*n) para hacerse, pero al haber seleccionado en el primer for que se iterase desde 0 hasta n-k, estamos garantizando que esto no ocurra, ya que en caso de tener un k muy grande tendriamos n-k elementos en el diccionario. Luego, al multiplicarlo por k, nos quedaria como complejidad del doble ciclo for un numero que es menor que n multiplicado por k, obteniendose una complejidad menor que O(n*n). Luego a lo sumo tendriamos que recorrer n elementos y hacer k recorridos para cada uno de esos n, lo cual resulta en O(n*k)=O(n).
Posteriormente analizamos el bucle que itera p veces:
* En sus primeras lineas se buscan los mayores en el diccionario de Elena y luego el de Hansel. A lo sumo sera O(n) ya q estaremos recorriendo todos los elementos de los diccionarios.
* Luego Tenemos una condicional if, que si no se cumple entraria en el else que se ejecutaria en O(1). Veamos el caso peor y supongamos que se cumpla el if. Primero le haremos una copia ambos diccionarios. Digamos que para esto recorreremos todos los elementos de cada uno y luego cada lista de tipo bool de cada uno, es decir, a lo sumo seria O(n*k) donde como bien ya sabemos esto sera menor que O(n). Luego vamos a analizar que sucederia si damos 1 paso mas y reducimos en 1 el valor de p. Para ello hacemos uso del metodo update_matched_number. Analicemos el costo de $update_matched_number()$, en este se hace un for desde 0 hasta el minimo entre el valor de inicio del rango de la seleccion que tomamoes y el valor maximo del rango que tomamos. Destacar que si el minimo es menor que 0, pues seria hasta 0 y si el maximo es mayor que n pues seria hasta n. Se realizarian a lo sumo 3*k iteraciones. Las k-1 primeras que puedan contener al primer numero del rango, las k iteraciones del rango y las k-1 ultimas que puedan contener al rango tb. Luego,  para casos grandes de n, 3*k sigue siendo menor que n. Para el caso de $update_mask()$ se tiene un for itera k veces, debido a que itera en el rango de una seleccion. Luego nos queda para el caso peor O(3*k * k), donde k <= n y para valores muy grandes de k como bien se ha explicado anteriormente la cantidad de elementos que tendremos sera pequenna, luego el k del metodo $update_mask()$ sera menor que n, obteniendose asi algo menor que O(n*n) y menor que O(k*n).
* Por ultimo, una vez que salgamos de la condicional if tendremos otra llamada al metodo $update_matched_number()$ el cual ya analizamos anteriormente.
Finalmente podemos calcular que nuestro algoritmo tendra una complejidad de:
O(n) + O(p*k*n) = O(p*n), siendo k menor que n, y teniendo en cuenta que O(k*n) <= O(n) para un n muy grande, tomando a k como constante.
Si p=n entonces con escribir unas lineas de codigo que analicen este caso bastara para evitar que nuestra solucion tenga complejidad n alcuadrado.