# yield is used to generate an iterator object which is iterable and lazy meaning it will produce new value only when next()
# keyword is given.

# difference between yield and return --> when we say the function yield the state of the function is hold in-memory
# when return is called the function stack-frame is completely removed from memory.
# yield helps to return value at multiple places within a function, with return we can use only one time to get back output.
# we can iterate over the yield object, but we can't iterate over return object as it returns an integer.
def greeting():
    print("Hi!")
    yield 1
    print("How are you?")
    yield 2
    print("Are you there?")
    yield 3


messenger = greeting()
print(type(messenger))
print(next(messenger))
print(next(messenger))
print(next(messenger))

print("----")


# class that is iterable using by overriding __next__ method
class Squares:
    def __init__(self, length):
        self.length = length
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.current ** 2

        self.current += 1

        if self.current > self.length:
            raise StopIteration

        return result


length = 4
square = Squares(length)


# for s in square:
#     print(s)


# above class can be replaceable with below generator function.
def squares(length):
    for n in range(length):
        print("-------")
        print(n)
        yield n ** 2
        # return n ** 2


length = 5
square = squares(length)
print(square)
for s in square:
    print(s)

print("-------")


def even_squares(length):
    for n in range(length):
        if n % 2 == 0:
            yield n


number = 100
even_number_generator = even_squares(number)
# print(list(even_number_generator))
for number in even_number_generator:
    print(number)

print("-------")
# genexpr = (expression for item in collection if condition)

squares = (n ** 2 for n in range(5))
print(squares)
for square in squares:
    print(square)

print("-------")

# generate square of even numbers from 1 to 10.
# generator expressions are lazy in nature i.e, they will not get called until action is set on them.
# whereas list comprehensions will get executed as soon as they are written
even_squares = (x * x for x in range(10) if x % 2 == 0)
# for x in even_squares:
#     print(x)

# print(next(even_squares))
# print(next(even_squares))

even_squares_list = [x*x for x in range(10) if x % 2 == 0]
print(even_squares_list)
















