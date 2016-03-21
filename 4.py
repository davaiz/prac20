# prac20
import matplotlib.pyplot as plt
import networkx as nx
def graf():
    G = {}
    for i in range(int(input('Количество рёбер в графе'))):
        a, b = input().split()
        if a not in G:
            G[a] = {b}
        else:
            G[a].add(b)
        if b not in G:
            G[b] = {a}
        else:
            G[b].add(a)
    return G

def bsf(G, P, start, fired):
    fired.add(start)
    queue=[start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                P.add_edge(current, neighbour)
                fired.add(neighbour)
                queue.append(neighbour)
def svyaz(G, fired, komp):
    for x in G:
        if x not in fired:
            komp += 1
            bsf(G, P, x, fired)
    return komp
P = nx.Graph()
fired = set()
G = graf()
komp = svyaz(G, fired, 0)
nx.draw(P)
plt.savefig("simple_path.png") # save as png
plt.show() # display
print('Компонента связности:', komp)
