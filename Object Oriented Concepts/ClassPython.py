#Creating class in Python
class Employee:
    #creating a common variable for all function
    empCount=0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary


    def displayCount(self):
        print("Total Employee: %d" %Employee.empCount)


    def displayEmployee(self):
        print("Name: ",self.name,"Salary: ",self.salary)


#creating the Instance

emp1=Employee("Zakir",2000)
emp2=Employee("Manni",5000)
emp1.displayEmployee()
emp2.displayCount()
emp1.age=22
