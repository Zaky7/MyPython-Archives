#Accessing Parent Class Function in Child Class
class Base(object):
    def __init__(self,x):
        self.x = x

class Derived(Base):
    def __init__(self,x,y):

        super().__init__(x)
        self.y = y

    def printXY(self):
        print(self.x, self.y)

d=Derived(23,45)
d.printXY(self)
