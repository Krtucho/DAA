class Vertex:
    def __init__(self, capacity) -> None:
        pass

class Edge:
    def __init__(self, u, v, index, capacity) -> None:
        self.u = u
        self.v = v
        self.capacity = capacity
        self.index = index
    
    def __repr__(self) -> str:
        return f"{self.u} - {self.v} ... flow = {self.capacity} ... index = {self.index}"

# Bipartite Graph
class Graph:
    def __init__(self, n_u, n_v, u_adjacency_list: dict, v_adjacency_list: dict, s, t, edges=[]) -> None:
        # U vertices
        self.u_vertex = [u for u in range(n_u)]
        # V vertices
        self.v_vertex = [v for v in range(n_u, n_u+n_v)]
        self.neg_vertex = []

        self.u_adjacency_list: dict = u_adjacency_list

        # S
        self.s = s
        self.t = t


    def get_edge(self, u, v)->Edge:
        try:
            for edge in self.u_adjacency_list[u]:
                if edge.v == v:
                    return edge
        except:
            return None
    
    def has_undirected_edge(self, u, v):
        if not self.u_adjacency_list.__contains__(u):
            return False
        adj_lst = self.u_adjacency_list[u]
        
        for edge in adj_lst:
            if edge.v == v:
                return True
        return False
    
    def modify_edge(self, u, v, index=-2, capacity=-1):
        if index == -2 and capacity==-1:
            return
        try:
            edge: Edge = self.get_edge(u, v)
            if capacity != -1:
                edge.capacity += capacity
            if index != -2:
                edge.index = index
        except:
            pass
                

    def add_edge(self, u, v, index, capacity=0):
        # Adding directed edges
        try:
            self.u_adjacency_list[u].append(Edge(u, v, index, capacity=capacity))
        except:
            self.u_adjacency_list[u] = []
            self.u_adjacency_list[u].append(Edge(u, v, index, capacity=capacity))

        # Adding undirected edges (Only used in the phase of building the network graph adding edges from every v that belongs to V to t)
        try: # residual flow network => capacity=0
            self.u_adjacency_list[v].append(Edge(v, u, index, capacity=0))
        except:
            self.u_adjacency_list[v] = []
            self.u_adjacency_list[v].append(Edge(v, u, index, capacity=0))

    def add_cross_edge(self, u, v, cross_edge_index, capacity=0):
        self.add_edge(u, cross_edge_index, cross_edge_index, capacity=capacity)
        self.add_edge(cross_edge_index, v, cross_edge_index, capacity=capacity)
        self.neg_vertex.append(cross_edge_index)

    def remove_edge(self, u, v):
        pass