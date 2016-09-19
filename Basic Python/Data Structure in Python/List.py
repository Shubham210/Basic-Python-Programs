newlist=[1,2,3,4,'red','blue',98.6,[11,22]]
print(newlist)
emptylist=list() # or []

for i in range(len(newlist)):
    print('Item '+str(i)+' = '+str(newlist[i]))

emptylist.append('book')
emptylist.append('99')
emptylist.append('cookie')

print('99' in emptylist)
emptylist.sort()
print(emptylist)

nums=[1,3,5,6,7,33,45,23,75]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

newstr='This is a sentence which will be broken into list'
slist=newstr.split()
print(slist)
pstr='int x; int y; z=x+y;'
plist=pstr.split(';')  
