# Range-> It will create a sequence of integers from start 0 to end '9' values.
a = range(0, 10)
print(type(a))

aList = list(a)
print(aList)

# range with reverse order, here -1 is called as reverse step.
b = range(1001, 100, -1)
print(type(b))

bList = list(b)
print(bList)

# range with reverse order.
c = range(100, 1001)
print(type(c))

cList = list(c)
print(cList[::-1])

"""
for <variable to store intermediate value> in <iterator> -> this can be list,tuple,set,dictionary or any object that has an ability to iterate over and it returns iterator :
    <statement>
"""

for i in a:
    print(i)

b = 0
for i in a:
    b += i
    print("i:", i, "|", "b:", b)
print(b)

# in is a membership operator
for element in ["foo", "bar", 1, False, range(0, 9)]:
    if "str" in str(type(element)):
        print("Its a string")
    elif "int" in str(type(element)):
        print("Its an integer")
    elif 'bool' in str(type(element)):
        print("Its an boolean")
    else:
        print("type of value is not in ['str','int','bool']", type(element))

# List comprehension

aSquares = []
aRange = range(1, 10)
for number in aRange:
    aSquares.append(number * number)
    print(aSquares)
# print(aSquares)

# Python Syntactic Sugar

# syntax: [<expression to generate a new value into output list for each iteration> <iterator><conditional expression>(optional)]
# list comprehension without condition exp or statement
squares = [i * i for i in range(1, 10)]
print(squares)

double_number = [i * 2 for i in range(1, 10)]
print(double_number)

# list comp using conditional statement as it doesn't contain else part
sentence = 'the rocket came back from mars'
vowels = [char for char in sentence if char not in 'aeiou']
print(vowels)

# list comp using conditional expressions
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
print(prices)
