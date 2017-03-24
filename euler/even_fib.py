def supersum(*args):
    y = 0
    for x in args:
        try:
            y += sum(x)
        except:
            y += x
    return y
#print supersum(1,2,3)
x = [1,2,3]
y = (4,5,6)
#print supersum(1,x)
#print supersum(1,2,x,y)
#print supersum(1,x,x,3)




def sumfabric(x):
    temp = []
    for i in x:
        temp2 = i
        temp.append(lambda y: temp2 + y)
    return temp
t0 = sumfabric((1,2))

print 'summ is %s'%(t0[0](5))
print 'summ is %s'%(t0[1](5))


def sumfabric(x):
    temp = x
    action = (lambda y : temp+y)
    return action

t = sumfabric(5)
#print t(3)

