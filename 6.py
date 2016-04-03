import matplotlib.pyplot as plt
import networkx as nx
def graph():
    input4 = open("./graph_input4.txt","r")
    list4 = input4.readlines()
    N = int(list4[0])
    weight = [[float('+inf')]*N for j in range(N)]
    for i in range(N):
        weight[i][i] = 0
    for i in range():
        a, b, w = input().split()
        a, b, w = int(a), int(b), float(w)
        weight[a][b] = w
        weight[b][a] = w
    return weight

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


G = graph()
printm(G)
F = floyd(G)
printm(F)
