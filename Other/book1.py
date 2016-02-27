import sys
import time

reps1 = 1000
repslist1 = range(reps1)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist1:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)

reps = 10000
repslist = range(reps)
def forLoop():
    res = []
    for x in repslist:
        res.append(x+10)
    return res
def listComp():
    return [x+10 for x in repslist]
def mapCall():
    return map((lambda x:x+10), repslist)
def genExpr():
    return list(x+10 for x in repslist)
def genFunc():
    def gen():
        for x in repslist:
            yield x+10
    return list(gen())
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print '\n'
    print ('%-9s: %.5f => [%s...%s]' % (test.__name__, elapsed, result[0], result[-1]))

