# prac20
import matplotlib.pyplot as plt
import networkx as nx
def graf():
    input2 = open("./graph_input2.txt","r")
    list2 = input2.readlines()
    G = {}
    for i in range(len(list2)):
        list2[i] = list2[i].rstrip()
        a, b = list2[i].split()
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
print('Компонента связности = ', komp)
