newdict={ 'key':12,'candy':13,'asdf':14 }
newdict['money']=11
print(newdict['asdf'])
newdict['asdf']+=4
print(newdict)

#in order to count no of each element in a list

counts=dict()
names=['a','b','a','c','b','b']
for name in names:
    counts[name]=counts.get(name,0)+1
print(counts)

print(counts.keys())
print(counts.values())
