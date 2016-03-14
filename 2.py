# prac20
import matplotlib.pyplot as plt
import networkx as nx
def graf():
    N = int(input())
    G = {}
    for i in range(int(input())):
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
friends(G, P, '0', called)
nx.draw(P)
plt.savefig("simple_path.png") # save as png
plt.show() # display


  
                
            
