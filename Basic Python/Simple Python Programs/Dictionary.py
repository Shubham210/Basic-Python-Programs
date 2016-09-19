# This script gives meaning of a word
import re
import urllib.request
try:
    word=input("Enter the word")
    url="http://www.dictionary.com/browse/"+word

    data=urllib.request.urlopen(url).read()
    data1=data.decode("utf-8")

    m = re.search('<meta name="description" content="',data1)
    start=m.start()+34

    m=re.search('" /><meta property="og:url" content="http://www.dictionary.com/browse/',data1)
    end=m.start()

    print(data1[start:end])

except:
    print("Sorry, the word is not in the dictionary.")
