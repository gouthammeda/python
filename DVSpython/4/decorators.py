#TODO revisit decorators again.
# # here we are having higher order function which takes function as input and returns wrapper function as output.
# # whatever the function we are passing as the input for closure we are calling that function inside wrapper.
# def uppercase_decorator(function):
#    # here wrapper is a closure
#     def uppercase_wrapper():
#         # here we are making the function executable and making result accessible.
#         func_output = function()
#         make_uppercase = func_output.upper()
#         return make_uppercase
#    # returning closure
#     return uppercase_wrapper()
#
# def say_hi():
#     return 'hello there'
#
# # we are passing reference of say_hi to the uppercase_decorator function.
# # main_wrapper = uppercase_decorator(say_hi)
# # output = main_wrapper()
# # print(output)
#
#
# def split_string(function):
#     def splitstring_wrapper():
#         func_output = function()
#
#         if 'str' in str(type(func_output)):
#             return func_output.split()
#         else:
#             return func_output
#
#     return splitstring_wrapper()
#
# # main_wrapper1 = split_string(say_hi)
# # output = main_wrapper1()
# # print(output)
#
# uppercase_decorator_wrapper_ref = uppercase_decorator(say_hi)
# split_string_wrapper = split_string(uppercase_decorator_wrapper_ref)
# split_string_output = split_string_wrapper()
# print(split_string_output)
#
#
# @split_string
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi())
#
# print("-------------------------------------------------------")

# Passing's Arguments to Decorator
def decorator_with_arguments(function):
    print("decorator_with_arguments executed")

    def wrapper_accepting_arguments(arg1, arg2):
        print("decorator_with_arguments.wrapper_accepting_arguments executed")
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("cities executed")
    print("Cities I love are {0} and {1}".format(city_one, city_two))


cities("Nairobi", "Accra")

print("-------------------------------------------------------")


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")


function_with_no_argument()
print("---------------------------------------------------------")


@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)


function_with_arguments(1, 2, 3)
print("---------------------------------------------------------")


@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")


function_with_keyword_arguments(first_name="Prudhvi", last_name="Akella")

print("---------------------------------------------------------")


def currency(fn):
    def wrapper(*args, **kwargs):
        print(fn)
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        # Here which ever either *args or **kwargs argument list match's with the net_price function's arguments list
        # those will be passed as an input
        # say in case of net_price(100, 0.05) values of *args will be passed as an input
        # in case net_price(price=100, tax=0.05) values of **kwargs will be passed as an input
        result = fn(*args, **kwargs)
        return f'${result}'

    return wrapper


@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    print(price, tax)
    return price * (1 + tax)


print(net_price(100, 0.05))
print("---------------------------------------------------------")
print(net_price(price=100, tax=0.05))
# if you check the name of the new function, Python will return the name of the inner function returned by the decorator
help(net_price)
print(net_price.__name__)
print("---------------------------------------------------------")

"""
Passing both keyword argument and Positional Argument togather 
"""


@currency
def net_price(a, b, price="", tax=0.0):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    print(a, b)
    print(price, tax)
    return price * (1 + tax)


print(net_price(100, 0.05, price=101, tax=0.06))

from functools import wraps
def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'

    return wrapper


@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


help(net_price)
print(net_price.__name__)


