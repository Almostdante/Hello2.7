#encoding= Windows-1251
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res
def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
            return first
def min3(*args):
    tmp = list(args)   # Или, в Python 2.4+: return sorted(args)[0]
    tmp.sort()
    return tmp[0]
print(min3([2,2], [1,1], [3,3]))