class Shape_2D(object):

    pi = float(22)/7    # class variable shared by all the instances

    def __init__(self,radius=0,length=0,breadth=0,side=0):
        self.radius = radius    # Instance variable unique to each instance
        self.length = length
        self.breadth = breadth
        self.side = side
        self.name = ""
        self.count = -1

    def add_element_in_count(self,number = 1):
        self.count += number

    def area_circle(self):
        return Shape_2D.pi * self.radius**2

    def area_square(self):
        return self.side**2

    def area_rectangle(self):
        print "I dont know that. Sorry"

circle1 = Shape_2D(3,0,0,0)
print ("{0}".format(circle1.area_circle()))


class Rectangle(Shape_2D):

    def __init__(self,radius=0,length=0,breadth=0,side=0):
        Shape_2D.__init__(self,radius,length,breadth,side)
        print "Rectangle Created"

    def area_rectangle(self):
        return self.length * self.breadth

rectangle1 = Rectangle(length=3, breadth=5)
print rectangle1.area_rectangle()
print rectangle1


###############################################################################################################

class Book(object):

    def __init__(self,title,author,pages):
        print "A book has been created!!!"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s" %(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print "The book is deleted"


shin_chan = Book("Shin Chan", "Japan", 136)
print shin_chan
print len(shin_chan)
del shin_chan
#This will give error -> print shin_chan
