import typing
from collections import deque
from graph import *


def show_answer(ans):
    output = ""
    for (k, edges) in ans:
        edges_output = ""
        for edge in edges:
            edges_output += f"({edge.u} {abs(edge.v)})-index:{abs(edge.index)} "
        output = f"k={k} {edges_output}" + output

    print(output)
    return output


def augment_flow(amount, g: Graph):
    for u in g.u_vertex:  # Directed Edges
        g.modify_edge(g.s, u, capacity=amount)

    for v in g.v_vertex:  # Directed Edges
        g.modify_edge(v, g.t, capacity=amount)


def get_unsaturated_edges(n_u, n_v, g):
    ans = []
    for u in range(n_u):
        for v in g.v_vertex + g.neg_vertex:
            edge: Edge = g.get_edge(u, v)
            if not edge:
                continue
            if edge.capacity == 1 and edge.index != g.s and edge.index != g.t:
                ans.append(edge)
    return ans


def bfs(s, t, g):
    mask = {x: -1 for x in range(0, len(g.u_vertex)+len(g.v_vertex))}
    for x in g.neg_vertex:  # Adding cross Vertex
        mask[x] = -1

    mask[s] = -2  # Adding source
    mask[t] = -1  # Adding sink

    q = deque()
    q.append((s, 1e8))

    while len(q) != 0:
        u = q[0][0]
        flow = q[0][1]
        q.popleft()

        for edge in g.u_adjacency_list[u]:
            if mask[edge.v] == -1 and g.get_edge(u, edge.v).capacity:
                mask[edge.v] = u
                next_flow = min(flow, edge.capacity)
                if edge.v == t:
                    return next_flow, mask
                q.append((edge.v, next_flow))

    return 0, mask


def max_flow(s, t, g):
    flow = 0

    next_flow, mask = bfs(s, t, g)

    while next_flow != 0:
        flow += next_flow
        current = t
        while current != s:
            prev = mask[current]

            edge: Edge = g.get_edge(prev, current)  # .u_adjacency_list[]
            capacity = edge.capacity

            # prev-current cap
            edge.capacity = (capacity - next_flow)  # modifying residual network

            # current-prev
            edge: Edge = g.get_edge(current, prev)  # .u_adjacency_list[]
            capacity = edge.capacity

            # prev-current cap
            edge.capacity = (capacity + next_flow)  # not residual network

            # Updating current
            current = prev

        next_flow, mask = bfs(s, t, g)

    return flow


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