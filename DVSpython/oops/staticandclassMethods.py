class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    # if a method is declared with static then we don't need to pass self which stores object reference or address,
    # and they can be accessed using class name, or we can access it by creating the object. They are mainly used for
    # creation of utility methods. These are class methods.
    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")

dateFromDB = "15/12/2016"
# date.toDashDate(dateFromDB)

dateWithDash = Dates.toDashDate(dateFromDB)

if date.getDate() == dateWithDash:
    print("Equal")
else:
    print("Unequal")

# class methods or factory methods will act like factory to create the objects of that particular class.

from datetime import date


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthyear):
        return cls(name, date.today().year - birthyear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John', 1985)
person1.display()


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))


class Man(Person):
    sex = 'Male'


man = Man.fromBirthYear('John', 1985)
# is instance checks if man is object of Man and returns true if it is.
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))


