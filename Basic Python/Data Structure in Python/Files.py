# handle=open(filename,mode)
fhand=open('read.txt' )
count=0


#The bellow commented code is equivalent of bellow uncomented code.
'''
for x in fhand:
    x=x.rstrip()
    print(x)
    count+=1
print('Line Count='+str(count))

'''
i_p=fhand.read()
print(i_p)
for x in i_p:
    if x=='\n':
        count+=1
print('Line Count='+str(count+1)) # While reading the last newline gets truncated#


# Search for lines beginning with letter a
for line in fhand:
    if line.startswith('A'):
        print(line)
