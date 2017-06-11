#Design Pattern 1 Duck Pattern
from abc import ABCMeta,abstractmethod

#FlyBehavior Interface
class FlyBehavior(object,metaclass=ABCMeta):

    #creating abstract method
    @abstractmethod
    def fly(self):
        pass

#implement the Flying Behavior
class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I m Flying")



    



#Quack Interface
class QuackBehavior(object,metaclass=ABCMeta):

    @abstractmethod
    def quack(self):
        pass

class Quack(QuackBehavior):

    def quack(self):
        print("Quack")









#creating an abstract Class
class Duck(object,metaclass=ABCMeta):

    #using Composition
    def __init__(self):
        self.flybehavior=FlyBehavior()
        self.quackbehavior=QuackBehavior()

  
    def performfly(self):
        self.flybehavior.fly()

    
    def performquack(self):
         self.quackbehavior.quack()     

    @abstractmethod
    def Display(self):
        pass

    def swim(self):
        print("All ducks float even decoy")

  

class MallardDuck(Duck):

     #overing the display
    def Display(self):
        print("I am Mallard Duck")

    def __init__(self):
        self.flybehavior=FlyWithWings()
        self.quackbehavior=Quack()

    def Display(self):
        print("I am a mallard Duck ")
    


#Driver Code
m=MallardDuck()
m.Display()    
m.performfly()
m.performquack()

