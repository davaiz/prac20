# prac20
import matplotlib.pyplot as plt
import networkx as nx
def graph():
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
          
def friends(G, P, start, called):
    called.append(start)
    for neighbour in G[start]:
        if neighbour not in called:
            P.add_edge(start, neighbour)
            friends(G, P, neighbour, called)
P = nx.Graph()
G = graf()
called = []
zero = input('Введите начальную точку ')
friends(G, P, zero, called)
nx.draw(P)
plt.savefig("simple_path.png") # save as png
plt.show() # display


  

  
                
            
