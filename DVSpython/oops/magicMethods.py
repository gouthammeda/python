class Example(object):
    def __init__(self):
        print("Inside init", id(self))

    def __str__(self):
        return "Example"

    def __len__(self):
        return 1

    def __del__(self):
        print("Deleting an example's object with ref:" + str(self))


object = Example()
# the below str method internally calls the __str__ method and returns the output present in it.
string_object = str(object)
print(string_object)
# anything we try to print is by default calls str method which is returning the memory location of object reference
# currently. print(object)

a: int = 10
a_str = str(a)
a_str1 = a.__str__()
# by default int class calls the __str__ method and value returned is given as output.
print(a)
print(a_str)
print(a_str1)
# to use len we have to override in the class we are using
print(len(object))

object1 = Example()
# print(object1.a) the given memory is deallocated for that particular object and to perform any actions before
# deleting we can override del method. del object1 print(object1.a)

print("---------")


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Author:{},Title:{},Pages:{}".format(self.author, self.title, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("An book object has been deleted")


book = Book("Here,There and Everywhere", "Sudha Murthy", 120)
print(str(book))

print(len(book))
del book

# __itr__ and __next__
# for expects to override __itr__ and __next__ method to access and iterate over it
aList = ['foo', 'bar', 1, False, 2.3]
# by default alist overwrites itr and next method, so we are able to access it.
for item in aList:
    print(item)

# when we pass aList as a reference to for it gets an iterator object by using iter() method
anitr = iter(aList)
print(anitr)

# when next() is being applied on anitr it returns current element and stores next elements memory location or
# reference in it.
print(next(anitr))
print(next(anitr))
print(next(anitr))
print(next(anitr))
print(next(anitr))


# print(next(anitr))

# Itr and Next methods are overwritten for classes like list and string methods but not for int.
class Reverse:
    """Iterator for looping over a sequence backwards"""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        # if we return self then it will call next method of this class but if we return string then it will call
        # string class next method.
        return self

    def __next__(self):
        print("index is:", self.index)
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse('spam')
# This is how we make object iterable without using list or set in the class. Try implementing linked list in python.
iter_reverse = iter(rev)
print(next(iter_reverse))
print(next(iter_reverse))
print(next(iter_reverse))
print(next(iter_reverse))
# print(next(iter_reverse))

# for char in rev:
#     print(char)

# using item as a reference of values stored in the list we are able to access and iterate over elements using iter
# and next methods
aList = [1, 2, 3, 4, 5, 6]
for item in aList:
    print(id(item))
    # item it contains all methods of object class
    print(item)


# using iter and next methods with in operator
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        print("_iter_ called")
        return self

    def __next__(self):
        print("_Next_ called")
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev_str = Reverse('123456789')
# iter_reverse = iter(rev_str)
# print(next(iter_reverse))
print('------- find 8 in rev way--------')
if '8' in rev_str:
    print('Found: 8')

print('------- find 3 in rev way--------')
if '3' in rev_str:
    print('Found: 3')

rev = Reverse('spam')
for char in rev:
    print(char)
