import sys
y = ['1','2','3']
a = [[1,],(1,2), {'a':1, 'b':2}, 'spam', {1,2,3}, y]
b = 'dsfgsdfgs'
def test(A):
    for x in A:
        if isinstance(x, list) or isinstance(x, dict):
            print 1, type(x)
        else:
            print 0, type(x)
Ltest = lambda x: map(sys.stdout.write, x)
Ltest2 = lambda x: [sys.stdout.write('1\n' if isinstance(y, list) else str(type(y))+'\n') for y in x]
#Ltest(y)
#test(a)
#showall = lambda x: [sys.stdout.write(line) for line in x]
#showall(y)

#Ltest2(a)
#Ltest(y)