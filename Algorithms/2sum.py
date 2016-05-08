import datetime
import math

target_numbers = 0
hash_set = set ()
hash_set_minus = set ()
hash_set_plus = set ()
range_m = [t for t in range(-5000,1)]

for x in open('2sum.txt'):
    hash_set.add(int(x))
    if int(x) < 0:
        hash_set_minus.add(int(x))
    else:
        hash_set_plus.add(int(x))


'''
print datetime.datetime.now()
for z in range_m:
    for y in hash_set_plus:
        if z-y in hash_set_minus:
            target_numbers += 1
            print target_numbers, z, y, z-y
            break

print target_numbers
print datetime.datetime.now()'
'''


target_numbers = {}
print datetime.datetime.now()
for x in hash_set_plus:
#    hash_set_plus2 = ([y-x for y in range_m])
    try:
        w = set([y-x for y in range_m]).intersection(hash_set_minus).pop() + x
        target_numbers[w] = 0
    except:
        pass

print target_numbers.keys()
print len(target_numbers)
print datetime.datetime.now()
