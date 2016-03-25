import random
import datetime

huge = open('SCC_mini.txt').readlines()
print len(huge)

huge_list = {}

for edge in huge:
    start_vertex = int(edge.split()[1])
    end_vertex = int(edge.split()[0])
    if start_vertex in huge_list:
        huge_list[start_vertex].append(end_vertex)
    else:
        huge_list[start_vertex] = [end_vertex]

dict = {}
x = [5, 7,115, 1, 34, 45, 12]
for y in x:
    dict[y] = x.index(y)

print dict

print sorted(list(dict), reverse=y)

print dict[115]

print x.index(2323)