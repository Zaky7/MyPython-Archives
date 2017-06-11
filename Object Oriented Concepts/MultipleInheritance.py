#Multiple Inheritance in Python
class Base1(object):

    #creating Constructor
    def __init__(self):
        self.str1="Geeks"
        print("Base1")

class Base2(object):

    #creating Constructor
    def __init__(self):
        self.str2="for Geeks"
        print("Base2")


class MultipleDerived(Base1, Base2):

    def __init__(self):

        #Calling Constructor of Base1 and 2
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")


    def printStrs(self):
        print(self.str1,self.str2)


ob=MultipleDerived()
ob.printStrs()
