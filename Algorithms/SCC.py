import datetime

filename = 'SCC.txt'
length = 875715
huge_list = {}
huge_list_rev = {}
exit_time = [0 for x in xrange(length)]
exit_time2 = [0 for x in xrange(length)]
explored2 = [0 for x in xrange (length)]
SCC_lens = []


print datetime.datetime.now()

for edge in open(filename):
    edge = edge.split()
    start_vertex = int(edge[0])
    end_vertex = int(edge[1])
    try:
        huge_list[start_vertex].append(end_vertex)
    except:
        huge_list[start_vertex] = [end_vertex]
    try:
        huge_list_rev[end_vertex].append(start_vertex)
    except:
        huge_list_rev[end_vertex] = [start_vertex]

temp_key_list = huge_list.keys()

y = 1
for vertex in temp_key_list:
    if exit_time[vertex]:
        continue
    current_route = []
    CurApp = current_route.append
    CurPop = current_route.pop
    current_vertex = vertex
    while True:
        try:
            temp_list = huge_list[current_vertex]
        except:
            exit_time[current_vertex] = y
            y += 1
            try:
                current_vertex = CurPop()
            except:
                break
            continue
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

k = 0
for y in exit_time:
    exit_time2[y] = k
    k += 1


for x in xrange(length-1, 0, -1):
    current_vertex = exit_time2[x]
    len_scc = 0
    current_route = []
    if explored2[current_vertex]:
        continue
    while True:
        try:
            temp_list = huge_list_rev[current_vertex]
        except:
            explored2[current_vertex] = 1
            len_scc += 1
            try:
                current_vertex = CurPop()
            except:
                break
            continue
        for m_next_vertex in temp_list:
            if explored2[m_next_vertex]:
                continue
            else:
                explored2[current_vertex] = 1
                CurApp(current_vertex)
                current_vertex = m_next_vertex
                break
        else:
            explored2[current_vertex] = 1
            len_scc += 1
            try:
                current_vertex = CurPop()
            except:
                break
    SCC_lens.append(len_scc)

SCC_lens.sort(reverse=True)
print datetime.datetime.now()
print sum(SCC_lens)
print SCC_lens[:10]
