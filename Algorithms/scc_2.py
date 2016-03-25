import random
import datetime

huge = open('SCC_mini.txt').readlines()


huge_list = {}

for edge in huge:
    start_vertex = int(edge.split()[1])
    end_vertex = int(edge.split()[0])
    if start_vertex in huge_list:
        huge_list[start_vertex].append(end_vertex)
    else:
        huge_list[start_vertex] = [end_vertex]


exit_time = [0 for x in xrange (1, 1000000)]
y = 1
temp_key_list = huge_list.keys()
filee =  open('temp.txt', 'w')



for vertex in temp_key_list:
    if exit_time[vertex]:
        continue
    current_route = []
    CurApp = current_route.append
    CurPop = current_route.pop
    full_path = []
    current_vertex = vertex
    while True:
        if y%1000 == 0:
            print y, len(current_route)
            print datetime.datetime.now()
        temp_list = huge_list[current_vertex]
        for m_next_vertex in temp_list:
            if exit_time[m_next_vertex]:
                continue
            if m_next_vertex not in temp_key_list:
                exit_time[m_next_vertex] = y
                y += 1
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

filee.write (str(exit_time) + '\n')
huge_list = {}

for edge in huge:
    start_vertex = int(edge.split()[0])
    end_vertex = int(edge.split()[1])
    if start_vertex in huge_list:
        huge_list[start_vertex].append(end_vertex)
    else:
        huge_list[start_vertex] = [end_vertex]

SCC_lens = []
temp_key_list = huge_list.keys()
#print huge_list
#print exit_time

while True:
    vertex = exit_time.index(max(exit_time))
    if not exit_time[vertex]:
        break
    exit_time[vertex] = 0
    current_vertex = vertex
    len_scc = []
    while True:
        if not current_vertex in temp_key_list:
            SCC_lens.append(1)
            break
        for m_next_vertex in huge_list[current_vertex]:
            if not exit_time[m_next_vertex]:
                continue
            if m_next_vertex not in temp_key_list:
                exit_time[m_next_vertex] = 0
                len_scc.append(m_next_vertex)
                continue
            exit_time[current_vertex] = 0
            current_route.append(current_vertex)
            current_vertex = m_next_vertex
            break
        else:
            exit_time[current_vertex] = 0
            len_scc.append(current_vertex)
            if not current_route:
                SCC_lens.append(len(len_scc))
                break
            current_vertex = current_route.pop()
SCC_lens.sort(reverse=y)
print SCC_lens