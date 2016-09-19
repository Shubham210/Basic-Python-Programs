##  In Python a regular expression search is typically written as:
##
##   match = re.search(pat, str)

##The re.search() method takes a regular expression pattern and a string
##and searches for that pattern within the string. If the search is successful,
##search() returns a match object or None otherwise. Therefore, the search is
##usually immediately followed by an if-statement to test if the search succeeded,
##as shown in the following example which searches for the pattern 'word:' followed
##by a 3 letter word

import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)   #The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change which is very handy for regular expressions. I recommend that you always write pattern strings with the 'r' just as a habit.
# If-statement after search() tests if it succeeded
if match:                      
    print ('found' + match.group()) ## 'found word:cat'
else:
    print ('did not find')


## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig')# =>  found, match.group() == "iii"
match = re.search(r'igs', 'piiig') #=>  not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig')# =>  found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g')# =>  found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!')# =>  found, match.group() == "abc"


## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig')# =>  found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii')# =>  found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # =>  found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')#  =>  found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx')# =>  found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar')# =>  not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar')# =>  found, match.group() == "bar"

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
# do something with each found email string
print email



###SOURCE-
###     https://developers.google.com/edu/python/regular-expressions
###
