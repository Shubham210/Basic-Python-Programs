# Program which checks wheather a number mobile number is correct or not

import re

message = 'Call me at +91-9964459758 or +91-7066616977 tomorrow'
phoneNumRegex = re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d')
# Matched object
print("Here we are printing first occourance using search method")
mo=phoneNumRegex.search(message)
print(mo.group())


print("Here we are printing all occourances using findall method")
mo=phoneNumRegex.findall(message)
print(mo)

# Program which checks STD code landline numbers

message = "My landline number for Jaipur is 0141-2762217"
landlineNumRegex = re.compile(r'(\d\d\d\d)-(\d\d\d\d\d\d\d)')
mo=landlineNumRegex.search(message)
print("Area code=" + mo.group(1))
print("Number=" + mo.group(2))

# Using Pipes
batRegex = re.compile(r'Bat(man|mobile|copter|gun|woman)')
mo=batRegex.search('Tony Stark was driving Batmobile')
print(mo.group()+"\n"+mo.group(1))

