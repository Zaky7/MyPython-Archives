#Interface in Python uses metaClass

from abc import ABCMeta, abstractmethod

#Interface
class Shape(object,metaclass = ABCMeta):

    #__metaclass__ = ABCMeta

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

#Inheriting the Interface
class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width  = width
        super(Rectangle,self).__init__()

    #Overring the method of Parent Class
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.width * 2 + self.length * 2

r=Rectangle(4,5)
print("Area and Perimeter is ",r.area())
print("Perimeter", r.perimeter())
