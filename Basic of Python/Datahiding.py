#python class hidden variable
#double underscore is used for declaring the hidden Variable

class MyClass:
    #hidden Variable
    __hiddenVariable=0

    def add(self,increment):
        self.__hiddenVariable+=increment
        print(self.__hiddenVariable)

myObject=MyClass()
myObject.add(2)
myObject.add(5)
