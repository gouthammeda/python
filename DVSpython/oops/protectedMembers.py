class Base:

    def __init__(self):
        # Protected Member
        self._a = 2


class Derived(Base):

    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class: ", self._a)

        # Modify the protected variable:
        self._a = 3
        print("address of _a inside derived class", hex(id(self._a)))

        print("Calling modified protected member outside class: ", self._a)


obj1 = Derived()
obj2 = Base()

# protected member should not be accesses outside the class due to convention
print("Accessing protected member of obj1: ", obj1._a)

print("address of _a outside derived class", hex(id(obj1._a)))

print("Accessing protected member of obj2: ", obj2._a)


# Example 2
class Student:
    _name = None
    _roll = None
    _branch = None

    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    def _displayRollAndBranch(self):
        # accessing protected data members
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)


# derived class

class Sparkler(Student):
    # constructor
    def __init__(self, name, roll, branch):
        Student.__init__(self, name, roll, branch)

    # public member function
    def displayDetails(self):
        # accessing protected data members of super class
        print("Name: ", self._name)
        # accessing protected member functions of super class
        self._displayRollAndBranch()


# creating objects of derived class
obj = Sparkler("R2J", 17347, "Information Technology")
# calling public member
obj.displayDetails()
