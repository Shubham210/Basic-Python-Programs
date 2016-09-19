#Simple Graph from coordinates given in file

import matplotlib.pyplot as p1

x=[]
y=[]
readfile=open("new.txt","r")
data=readfile.read().split("\n")
arrLen=len(data)
del(data[arrLen-1])

for i in data:
	val=i.split(",")
	x.append(int(val[0]))
	y.append(int(val[1]))
	

p1.title("Rain in December")
p1.xlabel("Days in December")
p1.ylabel("Inches of rain")
p1.plot(x,y)
p1.show()


