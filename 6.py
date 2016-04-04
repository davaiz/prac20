import matplotlib.pyplot as plt
import networkx as nx
def graph():
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
def printm(A):
    for i in range(len(A)):
        print(*A[i], sep='\t')
    print()

from copy import deepcopy

def floyd(w):
    N = len(w)
    F = deepcopy(w)
    for k in range(N):
        for i in range(N):
            for j in range(N):
                F[i][j] = min(F[i][j], F[i][k] + F[k][j])
    return F

G = graph_input()
printm(G)
F = floyd(G)
printm(F)
