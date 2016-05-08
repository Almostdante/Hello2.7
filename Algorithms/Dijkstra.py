edges = {}

for line in open('dijkstraData.txt'):
    temp = int(line.split()[0])
    edges[temp] = {}
    for x in line.split()[1:]:
        edges[temp][int(x.split(',')[0])] = int(x.split(',')[1])

distances = {1:0}

while True:
    temp_min = 100000
    for x in distances:
        try:
            cur_distance = min(edges[x][y] + distances[x] for y in edges[x] if y not in distances)
            if cur_distance < temp_min:
                temp_min = cur_distance
                new_vertex = edges[x].keys()[edges[x].values().index(cur_distance - distances[x])]
        except:
            continue
    try:
        distances[new_vertex]
        break
    except:
        distances[new_vertex] = temp_min

print distances[7], distances[37], distances[59], distances[82], distances[99], distances[115], distances[133], distances[165], distances[188], distances[197]

