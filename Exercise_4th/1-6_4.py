from Other import isinst
import itertools

n = 123
nn = 123.123
s = 'hello w'
d = {'z': 1, 'y': 2, 'x': 3}
l = [1, 2, 3]
t = (1, 2, 3)
d2 =  {x+'25':d[x]*25 for x in d}

#print d2
def test(x):
    print x

#test(n)
#test(s)
#test(d)
#test(l)
#test(t)


def adder_1(*x):
    s = x[0]
    for k in x[1:]:
        s = s + k
    return s


def adder_2(**x):
    s = x[sorted(x.keys())[0]]
    for k in sorted(x.keys())[1:]:
        s = s + x[k]
    return s

# print adder (n, n, nn, n)
#print adder_2(a = s, b = s, c = s[1:3]*4)
# adder (n, n)
# print adder (nn, nn)
# print adder (s, s)


def CD(dict):
    dict2 = {}
    for x in dict.keys():
        dict2[x] = dict[x]
    return dict2

#print CD(d)

def AD(dict1, dict2):
    dict_sum = {}
    for x in dict1.keys():
        dict_sum[x] = dict1[x]
    for x in dict2.keys():
        dict_sum[x] = dict2[x]
    return dict_sum
#print AD(d,d2)

#print '--'*33
#isinst.test([n, nn, s, d, t, l, d, d2 ])

#print dir(isinst)

for x in isinst.__dict__:
    if str(x).startswith('__'):
        continue
#    print x, isinst.__dict__[x]

t1 = ((x,(isinst.__dict__[x])) for x in isinst.__dict__ if str(x).startswith('__') == False)

#print sorted(t)
#print t == iter(t)
for x in t1:
    print x

try:
    print next(t1)
except:
    print 'haha'