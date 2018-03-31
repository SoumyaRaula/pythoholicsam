"""
__author__: sranjanr
__desc__: iterators
"""

list_of_values = [1,2,3,4,5]

# iteration using for loop
dict_new = {'a':1, 'b':2}

for i, j in dict_new.items():
    print (i, j)

# iter
x = iter([1,2,3,4,5])
print (x.__next__())
print (x.__next__())
print (x.__next__())
print (x.__next__())
print (x.__next__())

# iterator [1,2,3,4,5] -- stored
# generator [1,2,3,4,5] -- store them all at once.. if u call for a value then only it will store in the memory and will return u the
# reference

# [1,2,3,4,5]
# [a | 1 | b | 2 | c | 3 ] -- Iterator already has assigned them
# a --> 1 and will give u the generator object, till now 2, 3,4, 5 have not memory allocation

import random


def lottery():
    for i in range(6):
        print ('Inside the first loop... %d' % (i))
        yield random.randint(1, 10)

    print('Inside the second loop...')
    yield random.randint(1,20)


for random_numbers in lottery():
    print ('I came here...')
    print ('The number is %d' % (random_numbers))





