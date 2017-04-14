
def generate_cubes(n):
    for num in range(n):
        yield num**3

for x in generate_cubes(10):
    print x

'''
#The alternate of above code would be:

def generate_cubes(n):
    out = []
    for num in range(n):
        out.append(num**3)
    return out

for x in generate_cubes(10):
    print x

But, we would run into problems of slower execution if the no was like 1000000000000000000
'''

def simple_gen():
    for x in range(4):
        yield x

g = simple_gen()
print next(g)
print next(g)
print next(g)
print next(g)
# One more g will give error
# We will convert an iterable object into an iterator
s = "This"
s_iter = iter(s)
print next(s_iter)
print next(s_iter)