import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
input1 = open("./graph_input1.txt","r")
list1 = input1.readlines()
for i in range(len(list1)):
    list1[i] = list1[i].rstrip()
    a = list(list1[i].split())
    if len(a) == 2:
        G.add_edge(a[0], a[1])
    elif len(a) == 1:
        G.add_node(a[0])
    else:
        print('Введите правильно! ')
nx.draw(G)
plt.savefig("simple_path.png") # save as png
plt.show() # display
