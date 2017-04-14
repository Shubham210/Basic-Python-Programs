'''
Examples of Map
'''
def square(no):
    return no**2
numbers= [1,2,3,4,5,6,7,8,9]
numbers_square = map(square,numbers)
print numbers_square

temperatures = map(lambda T:(9.0/5.0)*T + 32.0 , numbers)
print temperatures

l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]
list_addition = map(lambda x,y,z: x+y+z,l1,l2,l3)
print list_addition

#######################################################
'''
Examples of Reduce
'''
red = reduce(lambda x,y:x+y,l1)
print red

def find_max(a,b):
    if a>b:
        return a
    else:
        return b

red = reduce(find_max,numbers)
print red

######################################################

'''
Examples of Filter
'''

def even_check(no):
    if no%2==0:
        return True
    else:
        return False
even = filter(even_check,numbers)
print even

list_comb = [1,2,4,'a','b',6,8,'y']
is_char = filter((lambda a:type(a) is str),list_comb)
print is_char

######################################################

'''
Example of Zip
'''
x = [1,2,88,4,99]
y = [11,22,33,44,55]
print zip(x,y)

for pair in zip(x,y):
    print max(pair)

print map(lambda pair: max(pair), zip(x,y))

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
print zip(d1,d2)
print zip(d1,d2.itervalues())

######################################################

'''
Enumerate
'''
l = ['a','b','c']
for (count,item) in enumerate(l):
    print item
    print count

for count,item in enumerate(l):
    if count>=2:
        break
    else:
        print item
