"""
Tuple: Immutable in nature and are heterogeneous
"""

# creating a tuple

# Empty tuple
my_tuple = ()
print(my_tuple.__sizeof__())

my_tuple = (1, 2, 3)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)
print(my_tuple.__sizeof__())

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

# tuple can also be created without using parenthesis
my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)
print(b)
print(c)

my_tuple = "hello"
print(type(my_tuple))

# creating tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))

# parenthesis is optional
my_tuple = "hello",
print(type(my_tuple))

# Access tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])
print(my_tuple[5])

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])  # 's'
print(n_tuple[1][1])  # 4

# Negative Indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

# Output: 't'
print(my_tuple[-1])
print(my_tuple[-6])

my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple[1:4])

# print elements from -7 to end towards right.
print(my_tuple[:-7])
# print elements from 8th to end
print(my_tuple[7:])

print(my_tuple[:])

# changing a Tuple
my_tuple = (4, 2, 3, [6, 5])

# However, item of mutable element can be changed
my_tuple[3][0] = 9
print(my_tuple)

# concatenation.
print((1, 2, 3) + (4, 5, 6))

# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
print(("Repeat",) * 3)

# deleting a List
# Deleting tuples-- we shouldn't do it gc takes care of it.
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

del my_tuple

my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3

my_tuple = ('a', 'p', 'p', 'l', 'e',)

print(my_tuple.count('p'))  # Output: 2
print(my_tuple.index('l'))  # Output: 3

# Usage of Membership operator in Tuple
# Membership test in tuple
my_tuple = ('a', 'p', 'p', 'l', 'e',)

# In operation
print('a' in my_tuple)
print('b' in my_tuple)

# Not in operation
print('g' not in my_tuple)

# Iterating Through a Tuple
# Using a for loop to iterate through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)

# Size of Tuple--> empty tuple takes 24 bytes and elements are remaining 40 bytes.
print(my_tuple.__sizeof__())


# we are accessing cat's method and dog method with their respective references being passed as tuple and using
# common animal variable to iterate because of polymorphism.
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


# Poly example
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
