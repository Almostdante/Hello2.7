L = [1, 2, 4, 8, 16, 32, 64]
X = 5
i = 0

#aaaaaaaaaaaaaaaaaaaaaaaa
while i < len(L):
    if 2 ** X == L[i]:
        print 'at index', i
        break
    else:
        i = i+1
else:
    print X, 'not found'

#bbbbbbbbbbbbbbbbbbbbbbbb
for x in L:
    if 2 ** X == x:
        print 'at index', L.index(x)
        break
else:
    print X, 'not found'

#cccccccccccccccccccccccc
if 2**X in L:
    print L.index(2**X)
else:
    print X, 'not found'

#dddddddddddddddddddddddd
L1 = []
for i in range(7):
    L1.append(2**i)
if 2**X in L:
    print L.index(2**X)
else:
    print X, 'not found'

