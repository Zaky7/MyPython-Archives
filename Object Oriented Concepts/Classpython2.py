#Using class in Python
class CSStudent:
    #class Variable
    stream="CSE"

    #initialising variable using constructor
    def __init__(self,roll):
        self.roll=roll

    #initialising using setter function
    def setAddress(self,address):
        self.address=address

    #Getter function for python
    def getAddress(self):
        return self.address

#driver function
a=CSStudent(101)
a.setAddress("NOIDA ,UP")
print(a.getAddress())
print(CSStudent.stream)
    
