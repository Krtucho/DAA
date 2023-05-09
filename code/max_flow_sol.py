# 976F - Minimal k-covering
# To get the answer for some k we can build the following network: connect the source to every vertex of the first part with edge with capacity degx  -  k (where degx is the degree of vertex), then transform every edge of the original graph into a directed edge with capacity 1, and then connect each vertex from the second part to the sink with capacity degx  -  k. Then edges saturated by the maxflow are not present in the answer (and all other edges are in the answer).

# To solve it fastly, we might just iterate on k from its greatest value to 0 and each time augment the flow we found on previous iteration. Since maxflow in the network is at most m, and we will do not more than m searches that don't augment the flow, this solution is O((n + m)2).


import typing
from collections import deque
#1176E
INF = 1e9
n = -1000
 
 
def bfs(s, t, parent):
    #cleaning road
    for i in range(0, len(parent)):
        parent[i] = -1
 
    parent[s] = -2
    q = deque()
    q.append((s, INF))
 
    while len(q) != 0:
        u = q[0][0]
        flow = q[0][1]
        q.popleft()
 
        for v in adj[u]:
            if parent[v] == -1 and capacity[u][v][0]: # next has not been visited & the road has still capacity
                parent[v] = u
                new_flow = min(flow, capacity[u][v][0])#min c_p
                if v == t:
                    return new_flow
                q.append((v, new_flow))
    return 0
 
 
def maxflow(s, t):
    flow = 0
    parent = [-1 for x in range(0, n)]
 
    new_flow = bfs(s, t, parent)
 
    while new_flow != 0:
        flow += new_flow
        cur = t
        while cur != s:#recover path
            prev = parent[cur]
 
            cap = capacity[prev][cur][0]
            id = capacity[prev][cur][1]
 
            capacity[prev][cur] = (cap - new_flow, id) #new_flow #residual net
            capacity[cur][prev] = (cap + new_flow, id) #contrary +=
            cur = prev
 
        new_flow = bfs(s, t, parent)
 
    return flow
 
 
def getUntochedEdges(n1, n2):
    mylist = []
    for u in range(0, n1):
        for v in range(n1, len(capacity[u])):
            tuple = capacity[u][v]
            if tuple[0] == 1 and tuple[1] != -1:
                mylist.append(((u + 1,v - n1 + 1),tuple[1] + 1, len(adj[u]) -1, len(adj[v])-1))
    return mylist
 
 
def updateCapacities(plus):
    for i in range(n1):
        capacity[s][i] = (capacity[s][i][0] + 1, -1)
    for i in range(n1, n1 + n2):
        capacity[i][t] = (capacity[i][t][0] + 1, -1)
 
 
def addintermedio(a, b, id):
    global n
    v = n - 2
    n += 1
    adj[a].append(v)
    adj[v].append(a)
    adj.append([])
    adj[v].append(n1+b)
    adj[n1+b].append(v)
 
    #nuevas aristas a->v->b
    newrow = [(0,-1) for _ in range(n1+n2)]
    #newrow[a] = (1, -1)
    newrow[n1+b] = (1, -1)
 
    while len(capacity[a]) <= v + 2:
        capacity[a].append((0, -1))#basura
    capacity[a][v] = (1, id)
 
    while len(capacity[n1+b]) <= v + 2:
        capacity[n1+b].append((0, -1))#basura
    #capacity[n1+b][v] = (1, id)
 
    capacity[v] = newrow
    capacity.append([])
 
#//read//////////////////////////
n1, n2, m = [int(x) for x in input().split()]
n = n1+n2+2
 
capacity = [[(0,-1) for _ in range(n)] for i in range(n)]
adj = [[] for i in range(0, n)]
 
for i in range(0, m):
    a, b = [int(x)-1 for x in input().split()]
    #Its a MultiEdge
    if capacity[a][n1+b][0] == 1:
        addintermedio(a, b, i)
    else:
        adj[a].append(n1 + b)
        adj[n1+b].append(a)
        capacity[a][n1+b] = (1, i)
#////////////////////////////////
s = n-2
t = n-1
 
capacity[s] = [(0, -1) for _ in range(n1+n2)]
capacity[t] = [(0, -1) for _ in range(n1+n2)]
 
mindeg = 1e9
for j in range(0, n1+n2):
    mindeg = min(mindeg, len(adj[j]))
 
k = mindeg
for j in range(0, n1+n2): #asigno aristas (s,j), (j,t)
    deg_j = len(adj[j])
    if j < n1:
        adj[s].append(j)
        while len(capacity[j]) <= s:
            capacity[j].append((0, -1))#basura
        capacity[s][j] = (deg_j-k, -1)
    else :
        adj[j].append(t)
        while len(capacity[j]) <= t:
            capacity[j].append((0, -1))#basura
        capacity[j][t] = (deg_j-k, -1)
 
#main loop
liststrin = []
while k > 0:
    maxflow(s, t)
    lista_E = getUntochedEdges(n1, n2)#me da las aristas que no se tocaron
 
    #build string solution
    strin = str(len(lista_E))
    for i in lista_E:
        strin += ' ' + str(i[1])
    liststrin.append(strin)
 
    updateCapacities(1)
    k-=1
 
liststrin.append('0')
finalstrin = ''
for i in range(len(liststrin)-1, -1, -1):
    finalstrin += liststrin[i] + '\n'
 
print(finalstrin)
 
# maxflow(s, t)
# lista = getUntochedEdges(n1, n2)
#
# strin = str(len(lista))
# for i in lista:
#     strin += ' ' + str(i[1])
#
# print(strin)