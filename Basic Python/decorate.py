
def func():
    return 1

s = "This is a global variable"

def func():
    print "Now we will print all the local variables - variables corresponding to this function"
    print locals()

print globals().keys()
print globals()['s']
func()

def func_name(name="Shubham"):
    print "Hello " + name

func_name()

greet = func_name
greet("Jain")

del func_name
greet() # Still works after deleting func_name

############################################################################

def hello(name="SJ"):
    def greet():
        return "This is inside greet func"
    def welcome():
        return "This is inside welcome func"
    if name=="SJ":
        return greet
    else:
        return welcome

x = hello()
print x()
x = hello("BlaBlaBla")
print x()

############################################################################

def hello():
    return "Hi User!"
def other(funct):
    print "Other code starts here!"
    print funct()
other(hello)

############################################################################

def new_decorator(func1):

    def wrap_func():
        print "This code is before func"
        func1()
        print "This code is after func"

    return wrap_func

def func_needs_decorator():
    print "This function needs a decorator"

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()

#The above 2 lines of code can be re-written as a decorator by-

@new_decorator
def func_needs_decorator():
    print "This function needs a decorator"

func_needs_decorator()

