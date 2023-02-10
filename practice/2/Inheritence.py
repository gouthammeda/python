import re


class BaseParentClass(object):
    pass


class DerivedChildClass(BaseParentClass):
    pass


child = DerivedChildClass()


class Polygon:
    def __init__(self, no_of_sides):
        print("Polygon object")
        print(self)
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        print(self.sides)

    def inputSides(self):
        self.sides = [float(input("Enter side" + str(i + 1) + ":")) for i in range(self.n)]
        print(self.sides)

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        print("triangle object")
        print(self)
        # object for polygon has to be created inside triangle, to access init and remaining methods.
        # come back for run time polymorphism
        Polygon.__init__(self, 3)
        # super().__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of triangle is %0.2f' % area)


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()


# Multiple inheritance
class B1(object):
    def __init__(self):
        self.str1 = "Python1"
        print("B1")


class B2(object):
    def __init__(self):
        self.str2 = "Python2"
        print("B2")


class derived(B1, B2):
    def __init__(self):
        # pass
        # you should instantiate parent class in child init method
        # else you cannot be able to access methods and variables from parent
        super().__init__()  # it will always refer to immediate parent.
        B2.__init__(self)


der = derived()
print(der.str2)
print(der.str1)


# multilevel inheritance

# The base class
class grandma:
    def __init__(self, grandmaname):
        self.grandmaname = grandmaname


# Middle class
class mother(grandma):
    def __init__(self, mothername, grandmaname):
        self.mothername = mothername

        # invoke a constructor of grandma class
        grandma.__init__(self, grandmaname)


# last class
class son(mother):
    def __init__(self, sonname, mothername, grandmaname):
        self.sonname = sonname

        # invoke a constructor of mother class
        mother.__init__(self, mothername, grandmaname)

    def print_name(self):
        print('Grandma name:', self.grandmaname)
        print("Mother name:", self.mothername)
        print("Son name:", self.sonname)


s = son("Goutham", "vinuja", "sulochanamma")
# using son's reference we are getting grandma's details
s.print_name()


# hierarchical Inheritance
# base class
class parent:
    def funA(self):
        print("This function is in the parent class.")


# derived class one
class child_one(parent):
    def funB(self):
        print("This function is in class child_one.")


# derived class two
class child_two(parent):
    def funC(self):
        print("This function is in class child_two.")


c = child_one()
c.funA()


# Method Overriding
class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    # method signature is same but implementation is different which is method overriding
    def get_pay(self):
        return self.base_pay + self.sales_incentive


# based on the reference it is able to identify which method to call this way is called as run-time polymorphism
john = SalesEmployee('John', 5000, 1500)
print(john.get_pay())

jane = Employee('Jane', 5000)
print(jane.get_pay())


# Method Overriding Example2
class Parser:
    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(r'\d{3}-\d{3}-\d{4}', self.text)
        if match:
            return match.group(0)
        return None

    def parse(self):
        # it is returning back a json as output.
        # when parse method is called with Ukparser's reference child's class phone method will get executed.
        return {
            'email': self.email(),
            'phone': self.phone()
        }


class UkParser(Parser):
    # this method is overriden in child class for changed functionality.
    def phone(self):
        match = re.search(r'(\+\d{1}-\d{3}-\d{3}-\d{4})', self.text)
        if match:
            return match.group(0)
        return None


s = 'Contact us via 408-205-5663 or email@test.com'
parser = Parser(s)
print(parser.parse())

s2 = 'Contact me via +1-650-453-3456 or email@test.co.uk'
parser = UkParser(s2)
print(parser.parse())


# attribute overriding
class Parser:
    phone_pattern = r'\d{3}-\d{3}-\d{4}'

    def __init__(self, text):
        self.text = text

    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', self.text)
        if match:
            return match.group(0)
        return None

    def phone(self):
        match = re.search(self.phone_pattern, self.text)
        if match:
            return match.group(0)
        return None

    # based on the reference used to call parse method that particular phone method is called using the same parent or child's pattern.
    def parse(self):
        return {
            'email': self.email(),
            'phone': self.phone()
        }


class UkParser(Parser):
    phone_pattern = r'\+\d{1}-d{3}-\d{3}-\d{4}'


s = 'Contact us via 408-205-5663 or email@test.com'
parser = Parser(s)
print(parser.parse())

s2 = 'Contact me via +1-650-453-3456 or email@test.co.uk'
parser = UkParser(s2)
print(parser.parse())
