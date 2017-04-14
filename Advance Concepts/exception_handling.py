try:
    2 + 's'
except TypeError:
    print "There was a type Error"
except Exception as ex1:
    print (ex1)
    print (type(ex1))
finally:
    print "This is the final statement"

###########################################################################

try:
    s = 1/0
except TypeError:
    print "There was a type Error"
except Exception as ex1:
    print (ex1)
    print (type(ex1))
finally:
    print "This is the final statement"

###########################################################################

def ask_if_integer():

    while True:
        try:
            val = int(raw_input('Please enter an integer: '))
        except Exception as ex1:
            print "Looks like you didnt enter an integer. The exeption encountered is %s. Its type is %s" %(ex1,type(ex1).__name__)
            #You can also substitute above print statement with:
            #template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            #message = template.format(type(ex1).__name__, ex1.args)
            #print message
            continue
        else:
            print "Correct! You have Entered an integer of value %s" %(val)
            break
        finally:
            print "Finally, the whole block is executed"

ask_if_integer()