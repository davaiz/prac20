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
    queue = [start]
    fired.add(start)
    while len(queue) != 0:
        current = queue.pop(0)
        for neighbour in G[current]:
            if neighbour not in fired:
                P.add_edge(current, neighbour)
                fired.add(neighbour)
                queue.append(neighbour)
P = nx.Graph()
G = graf()
fired = set()
zero = input('Введите начальную точку')
bsf(G, P, zero, fired)
nx.draw(P)
plt.savefig("simple_path.png") # save as png
plt.show() # display


                
            
