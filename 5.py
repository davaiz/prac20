import matplotlib.pyplot as plt
import networkx as nx
def graf():
    input3 = open("./graph_input3.txt","r")
    list3 = input3.readlines()
    G = {}
    for i in range(len(list3)):
        list3[i] = list3[i].rstrip()
        a, b, weight = list3[i].split()
        weight = float(weight)
        if a not in G:
            G[a] = {b:weight}
        else:
            G[a][b] = weight
        if b not in G:
            G[b] = {a:weight}
        else:
            G[b][a] = weight
    return G
def dejkstra(G, start):
    shortest_path = {vertex:float('+inf') for vertex in G}
    shortest_path[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        for neighbour in G[current]:
            offering_shortest_path = shortest_path[current] + G[current][neighbour]
            if offering_shortest_path < shortest_path[neighbour]:
                shortest_path[neighbour] = offering_shortest_path
                queue.append(neighbour)
    return shortest_path
G = graf()
zero = 'Апельсиновый'
shortest_path = dejkstra(G, zero)
print('Кратчайшие пути из ;')
for vertex in G:
    print(vertex, shortest_path[vertex])
