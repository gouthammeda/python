from math import pi

# same operator can be used in many ways say "+" operator can be
print(1 + 2)
print("Goutham" + "" + "Meda")
print(2 * 3)
print("Goutham" * 3)

# function:same function can be used to perform multiple different actions based on arguments passed is operator
# overloading
print(len("Goutham Meda"))
print(len(["Hello", "Optimist", 12, 3, True]))


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape"


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length ** 2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


a = Square(4)
b = Circle(7)
# In run time when the object is created based on the type of reference used to call the function that particular
# classes' method(here area) is called and output is returned which is called as run time polymorphism.
print(a.area())
print(a.fact())

print(b.area())
print(b.fact())
