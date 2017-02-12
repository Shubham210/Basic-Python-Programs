def double(x):
	return x*2
	
a = [1,2,3,4]

list(map(double,a))              # [2, 4, 6, 8]
# OR
for item in map(double,a):
    print(item)



	
def even(x):
	return x%2==0

list(filter(ev,a))			  # [2, 4]

def sum(x,y):
	return x+y
	
from functools import reduce
reduce(sum,a)  # 10

#########################################################
#
#  PROBLEM STATEMENT ->
#  Print the sum of squares of even nos. uptill 10
#
#########################################################

n  =input("Enter the no. for which you want sum of squares")
l = []
for i in range(int(n)):
	l.append(i+1)
	

def even(x):
	return x%2==0
	
l_even = list(filter(even,a))


def double_sq(x):
	return x*2
	
l_square = list(map(double_sq,l_even)) 

sum = 0

def sum(x,y):
	return x+y
	
from functools import reduce
reduce(sum,l_square)
