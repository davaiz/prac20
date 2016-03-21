import matplotlib.pyplot as plt
import networkx as nx
def graf():
    G = {}
    for i in range(int(input('Количество рёбер в графе '))):
        a, b, weight = input().split()
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
zero = input('Введите начальную точку ')
shortest_path = dejkstra(G, zero)
print('Кратчайшие пути из ')
for vertex in G:
    print(vertex, shortest_path[vertex])
