class Employee:
    # any variables defined outside the init method is class level attributes, and it will have same value for all the objects
    department = "cse"

    # Remember the first argument of __init__ will always be self to hold the address of current
    # object that is accessing attribute or method using reference operator "."
    def __init__(self, employee_id, firstname, lastname, age, department):
        # Instance level attributes--> these values change with each of the object created.
        self.employee_id = employee_id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        # when we have both class level and object level attributes then priority will be given to object/instance level attributes.
        self.department = department

    # when we call a method with reference of object then self will be same memory location of that particular object
    # whichever reference we are using to call this method the reference of that object will be stored in self to access
    # attributes of that object either at class level or instance level
    def print_employee_details(self):
        print("self memory location", id(self))
        print("department=", self.department, "employeeid=", self.employee_id, "firstname=", self.firstname,
              "lastname=", self.lastname, "age=", self.age)


# # Now lets see whether this __init__ method will be called when user creates an objects for employee class
# employee = Employee(1, "Goutham", "Meda", 30)
# employee2 = Employee(2, "kiran", "p", 30)
#
# # Now lets print address of employee1 and employee2 using id
# print(id(employee))
# print(id(employee2))
employee1 = Employee(1, "Goutham", "Meda", 30, "mech")
print("employee1 memory location:", id(employee1))
employee1.print_employee_details()
print("----------")
employee2 = Employee(2, "Ravi", "M", 30, "ece")
print("employee2 memory location:", id(employee2))
employee2.print_employee_details()
print("----------")
employee3 = Employee(3, "kasi", "k", 23, "eee")
print("employee3 memory location:", id(employee3))
employee3.print_employee_details()
print("----------")

# Re-assign value to class level attribute, we shouldn't do this

# Employee.department = "ece"
# employee1 = Employee(1, "goutham", "meda", 30)
# print(Employee.department)
# print(employee1.department)

# Re-assign the value to instance level attribute
# employee1.employee_id = 2
# print(employee1.employee_id)
