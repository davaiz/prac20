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
def friends(G, P, start, called):
    called.append(start)
    for neighbour in G[start]:
        if neighbour not in called:
            P.add_edge(start, neighbour)
            friends(G, P, neighbour, called)
P = nx.Graph()
G = graf()
called = []
zero = input('Введите начальную точку')
friends(G, P, zero, called)
nx.draw(P)
plt.savefig("simple_path.png") # save as png
plt.show() # display


  

  
                
            
