#Checking given Class is subclass of Parent Class

class Base(object):  #Creating a empty class
    pass

class Derived(Base): #Creating another empty class
    pass

print(issubclass(Derived,Base))
print(issubclass(Base,Derived))

d=Derived()
b=Base()

print(isinstance(b,Derived))
print(isinstance(d,Base))
