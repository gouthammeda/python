# class Dog:
#     def __init__(self, name: str):
#         self.name = name
#
#     def bark(self):
#         print(f"{self.name} barks")
#
#
# dog1 = Dog("snoppy")
# dog1.bark()
# dog2 = Dog("Bet")
# dog2.bark()

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + "is" + str(self.age) + "year(s) old.")

    def increment_age_of_dog(self):
        self.age += 1

    # we are passing object reference of one object to another object
    def setbuddy(self, buddy_ref):
        print("self:", hex(id(snoopy)))
        print("buddy:", hex(id(buddy_ref)))
        # we are creating one-to-one relationship between two object as by creating self.buddy instance variable in snoopy object with buddys reference variable
        # and buddy.buddy instance level variable with filou as a reference.
        self.buddy = buddy_ref
        buddy_ref.buddy = self


snoopy = Dog("snoopy", 2)
print(hex(id(snoopy)))
filou = Dog("Filou", 8)
print(hex(id(filou)))

snoopy.setbuddy(filou)

print(snoopy.buddy.name)
print(snoopy.buddy.age)

print(filou.buddy.name)
print(filou.buddy.age)


