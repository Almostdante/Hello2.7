#coding: windows-1251
import math
import time
import sys
from mymod import *

reps1 = 10
repslist1 = range(reps1)

def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)         # Переменное число позиционных аргументов
def f3(a, **b): print(a, b)        # Переменное число именованных аргументов
def f4(a, *b, **c): print(a, b, c) # Смешанный режим
def f5(a, b=2, c=3): print(a, b, c)# Аргументы со значениями по умолчанию
def f6(a, b=2, *c): print(a, b, c)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist1:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)

'''
print f1(1, 2)  #1, 2
print f1(b=2, a=1)  #1, 2
print f2(1, 2, 3)   #1, (2, 3)
print f3(1, x=2, y=3)   #1, {x:2, y:3}
print f4(1, 2, 3, x=2, y=3)     #1, (2,3), {x:2, y:3}
print f5(1)     # 1, 2, 3
print f5(1, 4)      #1, 4, 3
print f6(1)     #1, 2, ()
print f6(1, 3, 4)   #1, 3, (4,)
'''

def IsPrime(y):
    if y <> int(y):
        print y, 'is not an integer'
        return
    else:
        x = abs(y/2)
    while x > 1:
        if y%x == 0:
            print y, 'has factor', x
            break
        x -= 1
    else:
        print y, 'is prime'

print math.sqrt(25)

def IsPrimeFast(y):
    if y <> int(y):
        print y, 'is not an integer'
        return
    for x in range(2,int(math.sqrt(abs(y)))):
        if y%x == 0:
            print y, 'has factor', x
            return
    print y, 'is prime'




years = range(2000,2020)
years = years + [19.5, 346346, -3811, 234.111, 6284560583]
#for y in years:
#    IsPrimeFast(y)

L = [2, 4, 9, 16, 25]
L1= []
for x in L:
    L1.append(math.sqrt(x))

#print L1
L1 = []
L1 =map(math.sqrt, L)

#print L1
L1 = []
L1 = [math.sqrt(x) for x in L]


test('mymod.py')
