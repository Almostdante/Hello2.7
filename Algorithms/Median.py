import numpy
data = []

for line in open("Median.txt"):
    data.append(int(line))

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    return sortedLst[index]


print len(data)
median_list = []




for x in range(1, 10001):
    median_list.append(median(data[:x]))
print len(median_list)
print data[:6]
print median_list[:6]
print sum(median_list)