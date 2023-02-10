# while we are defining the functions the inside ones are called as parameters but when we are
# calling the inner ones are called as arguments.
def function_name(par1, par2):
    print("statement1")
    print("statement2")
    return "value"


# function definition
def add(a, b):
    print(a, b)
    # return is always Optional
    return a + b


# function call
ret = add(1, 2)
ret_str = add("Hello", "World")
print(ret)
print(ret_str)


# specifying data types to parameters, even though we give string data types python understands the datatype of the args
# passed and uses it to perform the operation

def add_with_datatypes(a: int, b: int) -> int:
    return a + b


ret = add_with_datatypes(1, 2)
print(ret)

ret = add_with_datatypes("Hello", "World")
print(ret)


def function_without_return_type(a, b):
    print(a)
    print(b)


# it returns None of NoneType which means nothing or no value
ret = function_without_return_type(1, 2)
print(ret)
print(type(ret))


def add(a, b):
    return a + b


def multiply_2(a):
    print(a)
    return a * 2


# function will be evaluated to a value when it is passed as an argument result is then passed as argument to next function which returns the
# final result which is known as function evaluation.
print(multiply_2(add(1, 2)))
print(multiply_2(3))

"""
a-> add 
a(1,2) -> add(1,2) --> 3 * 2 = 6
"""


# closure -> function that takes other function as an argument is called as higher order function
def multiply_2_higher_order_fun(a):
    return a(1, 2) * 2


# we passed function reference as an argument or address of add to function which means parameter 'a' acts like alias to that function, but it is not a function call as it is not called with arguments.
print(multiply_2_higher_order_fun(add))


def plus(a, b):
    result = a + b
    return result, a


# call 'plus()' and unpack variables
sum, a = plus(3, 4)

print(sum, a)
