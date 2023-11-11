class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        if not 'str' in str(type(name)):
            raise Exception("Invalid name")
        elif len(name) < 2:
            raise Exception("name should be more than 2 char")
        else:
            self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age <= 0:
            # here we are raising error if age of person is less than 0
            raise ValueError("The age must be positive")
        # we are making instance variable private so that it can't be accessed or modified by object reference
        # outside the class.
        self.__age = age

    def get_age(self):
        return self.__age


john = Person('John', 18)
#print(john.set_age(-1))
john.set_name("joh")
print(john.get_name())
