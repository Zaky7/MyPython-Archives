#Inplace operator change the first argument in case of mutable Targets e.g. iadd()
#Normal operator dont change e.g add()
import operator

l=[1,2,3,4]
z=operator.add(l,[5,6,7])
print(z,l,end=" ")
p=operator.iadd(l,[5,6,7])
print("\n",p,l,end=" ")
#Immutable Targets
#print(operator.add(3,4))
