import random
import datetime

file = 'SCC_mini.txt'
length = 20

def file_to_dict(file_name, rev):
    file_lines = open(file_name).readlines()
    graph_in_dict = {}
    a, b = int(rev==0), int(rev<>0)
    for edge in file_lines:
        start_vertex = int(edge.split()[a])
        end_vertex = int(edge.split()[b])
        try:
            graph_in_dict[start_vertex].append(end_vertex)
        except:
            graph_in_dict[start_vertex] = [end_vertex]
    return graph_in_dict

huge_list = file_to_dict(file, 0)
exit_time = [0 for x in xrange (1, length)]
y = 1
temp_key_list = huge_list.keys()


for vertex in temp_key_list:
    if exit_time[vertex]:
        continue
    current_route = []
    CurApp = current_route.append
    CurPop = current_route.pop
    full_path = []
    current_vertex = vertex
    while True:
        if y%10000 == 0:
            print y, len(current_route)
            print datetime.datetime.now()
        try:
            temp_list = huge_list[current_vertex]
        except:
            exit_time[current_vertex] = y
            y += 1
            try:
                current_vertex = CurPop()
            except:
                break
        for m_next_vertex in temp_list:
            if exit_time[m_next_vertex]:
                continue
            exit_time[current_vertex] = 'n'
            CurApp(current_vertex)
            current_vertex = m_next_vertex
            break
        else:
            exit_time[current_vertex] = y
            y += 1
            try:
                current_vertex = CurPop()
            except:
                break

huge_list = file_to_dict(file, 1)
SCC_lens = []
temp_key_list = huge_list.keys()
exit_dict = {}
k = 0
for y in exit_time:
    exit_dict[y] = k
    k += 1
del exit_dict[0]
explored = []
max = max(list(exit_dict))

for x in xrange(max, 0, -1):
    current_vertex = exit_dict[x]
    len_scc = []
    if x in explored:
        continue
    if len(SCC_lens)%1000 == 0:
        print len(SCC_lens), len(explored)
    while True:
        try:
            temp_list = huge_list[current_vertex]
        except:
            explored.append(current_vertex)
            len_scc.append(current_vertex)
            if not current_route:
                SCC_lens.append(len(len_scc))
                break
            current_vertex = current_route.pop()
            continue
        for m_next_vertex in temp_list:
            try:
                explored.index(m_next_vertex)
                continue
            except:
                explored.append(current_vertex)
                current_route.append(current_vertex)
                current_vertex = m_next_vertex
                break
        else:
            explored.append(current_vertex)
            len_scc.append(current_vertex)
            if not current_route:
                SCC_lens.append(len(len_scc))
                break
            current_vertex = current_route.pop()
SCC_lens.sort(reverse=True)
print SCC_lens