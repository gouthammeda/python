class Employee:
    # <attributes>
    employee_id = None
    firstname = "Goutham"
    lastname = "Meda"
    age = 30

    # constructor is method to pass values to objects in run time
    def __init__(self, employee_id, firstname, lastname, age):
        self.employee_id = employee_id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    # <methods>
    # if we define a function inside a class then that is called as method but if we define the function outside then it is called as function.
    def print_employee_details(self):
        print(f"employee_id:{self.employee_id},firstname:{self.firstname},lastname:{self.lastname},age:{self.age}")


# object is physical entity i.e., it is something that is exists inside the memory and class is logical entity which is defined in english language.
# this variable is holding the memory address or reference of this object, and we can create multiple references for same object.
employee = Employee(1, "Goutham", "Meda", 30)
# using the reference operator we can access the attributes or methods of the class
employee.print_employee_details()
employee1 = Employee(2, "Sindhur", "Bathala", 29)
employee1.print_employee_details()
employee2 = Employee(3, "Sureesh", "kuppala", 40)
employee2.print_employee_details()

# class and object
# Employee
# Employee id
# firstname
# lastname
# age

# Capture and collect information of 3 employees
employee_list = []
inc = 1
while True:
    print("----------")
    print(f"Enter employee:{inc} info")
    emp_id = input("Enter employee id:")
    firstname = input("Enter employee firstname:")
    lastname = input("Enter employee lastname:")
    age = int(input("Enter employee age:"))
    employee_list.append(Employee(emp_id, firstname, lastname, age))
    inc += 1
    if inc == 4:
        break

# here we are accessing the values using the aliases.
for employee in employee_list:
    employeeid = employee.employee_id
    firstname = employee.firstname
    lastname = employee.lastname
    age = employee.age
    print("employeeid=", employeeid, "firstname=", firstname, "lastname=", lastname, "age=", age)


# Data + functionality
# logic entity
class Example:
    # attribute: these are used to store data/maintain the state of object
    a = 10

    # method:Functionality / change the state of an object
    # memory will be allocated only when object is created
    def add(self, b):
        return self.a + b


# Physical
# syntax: reference variable = <name of the class>(constructor:pass input arguments to class parameters)
# this variable stores the reference of the memory address of the attribute a.
object1 = Example()
print(hex(id(object1)))
print(object1.a)
# print(object1.add(20))

object2 = Example()
print(hex(id(object2)))
print(object2.a)
# print(object2.add(40))











