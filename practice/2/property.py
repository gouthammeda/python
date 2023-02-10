class Person:
    def __init__(self, name, age):
        self.name = name
        # Just Hover on the age to see the type of age
        self.age = age

    def set_age(self, age):
        print("Inside set age")
        if age <= 0:
            raise ValueError('The age must be positive')
        self.__age = age

    def get_age(self):
        print("Inside get age")
        return self.__age

    """
        when you try to assign the new value to age  using assignment operator set_age will be called
        when you try to get the new value of age  using reference operator get_age will be called
    """
    # Using property we are creating alias to private members
    # alias of __age is age
    age = property(fget=get_age, fset=set_age)


john = Person('John', 18)
print(john.age)
john.age = 10
print(john.age)


class Person:
    def __init__(self, name, age):
        # self.__name = name
        # self.__age = age
        self.name = name
        self.age = age

    @property  # This is getter method for age private variable
    def age(self):
        print("age_prop got executed")
        return self.__age

    @property  # This is getter method for name private variable.
    def name(self):
        print("name_prop got executed")
        return self.__name

    # below name method with @name.setter decorator will act like a setter for name instance attribute
    @name.setter
    def name(self, value):
        print("Inside setter name")
        if value.strip() == "":
            raise ValueError('The name cannot be empty')
        self.__name = value

    @age.setter
    def age(self, value):
        print("Inside setter age")
        if value <= 0:
            raise ValueError('The age must be positive')
        self.__age = value


person = Person("Goutham", 30)
print(person.age)
print(person.name)
person.age = 10
person.name = "Ravi"
print(person.age)
print(person.name)


