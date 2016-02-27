__author__ = 'andreydmitriev'
import random


def findmincut(graph):
    while len(graph) > 2:
        first_vertex = random.choice(graph.keys())
        second_vertex = random.choice(graph[first_vertex])
        graph[first_vertex] = [x for x in graph[first_vertex] if x != second_vertex]
        graph[second_vertex] = [x for x in graph[second_vertex] if x != first_vertex]
        for x in graph[second_vertex]:
            graph[first_vertex].append(x)
            graph[x] = [first_vertex if y == second_vertex else y for y in graph[x]]
        del graph[second_vertex]
    return len(random.choice(graph.values()))

fin = 1000
for t in xrange(10):
    graph1 = {}
    for x in open('kargerMinCut.txt').readlines():
        graph1[x.split()[0]] = [y for y in x.split()[1:]]
    fin = min(findmincut(graph1), fin)
print 'fin', fin