import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
N = int(input())
M = int(input())
for i in range(M):
    a = list(input().split())
    if len(a) == 2:
        G.add_edge(a[0], a[1])
    elif len(a) == 1:
        G.add_node(a[0])
    else:
        print('Введите правильно') 
nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display
