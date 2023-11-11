print('----------')
# arithmatic exp produces value(Int,Float) based on type of operator used.
a = 3
b = 4
print(a + b)
print(b - a)
print(a * b)
# type(a/b) is always float.
print(a / b)
print(a % b)
print(a ** b)
# Floor Division-- eliminates precision portion returns int
print(a / b)
print(a // b)
print(1.2)
# floating point error we can use round to avoid them from happening
print(1.2 - 1.0)
print(10 / 3)

# rel expressions are constructed with relational operators and logical operators and always result in boolean value
# true or false exp with rel operators
a, b, c = 10, 20, 30
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# expression with logical operators
# AND(multiplication) IF one of the rel exp is false then output is false.
print('-------AND------')
print((a > b) and (b < c))

# OR(Addition) If one of rel exp is true then output is true.
print('----OR----')
print((a > b) or (b < c))

# NOT(negate operator) it will inverse the boolean input and provide the output.
print('----NOT---')
print(not ((a > b) or (b < c)))
print('------')

# string based operators and expressions
aString1 = "Hello"
aString2 = " World"

# same operator behaves differently based on the type of operands provided is called as operator polymorphism.
# concat(+)
print('----concat----')
print(aString1 + aString2)
# reflection(*)
print('---REFLECTION----')
print(aString1 * 2)
# Membership operator(return true or false)
print('----MEMBERSHIP---')
"""
step 1:
(aString1 + aString2) -> Hello World
step 2:
'Hello' in "Hello World"--> True 
"""
print('Hello' in (aString1 + aString2))
print('Hello' not in (aString1 + aString2))

# can I concat number with string? no
# print("You are No:" + 1)
# YES BY USING int to string using str() in-built function
print('---------')
print("You are No:" + str(1))
# converting number string value to int
a = "1"
print(int(a) + 10)
# invalid usage--we have to use float
a = "1.34"
# print(int(a)+0.234)
# converting floating point number string value to float
print('----------')
a = "1.34"
print(float(a) + 2.34)
# anything other than 0 is passed to bool returns true it could be a number, floating point number, string etc.
print('--------')
print(bool(1))
print(bool(1))
print(bool("Hello"))
print(bool(0))
print('---------')
