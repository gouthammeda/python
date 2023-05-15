import traceback

# by handling the exceptions we are making sure to keep program executing.
try:
    colors = ['red', 'green', 'blue']
    print(colors[0])
    print(colors[3])
except IndexError as error:
    print("Index error occurred")
finally:
    print("finally executed")

print("Its executed")

try:
    colors = ['red', 'green', 'blue']
    print(colors[0])
    print(colors[3])
except IndexError as error:
    print("Index error occurred")
    # when use raise keyword then program execution is stopped after executing finally.
    # raise error
finally:
    print("finally executed")

print("Its executed")

# using traceback module to convert exception to string.
try:
    colors = ['red', 'green', 'blue']
    print(colors[0])
    print(colors[3])
except IndexError as error:
    print(error)
    # exception_str = traceback.format_exc()
    # print(exception_str)

finally:
    print("finally executed")

print("Its executed")

# we could use the parent class to handle the exception instead of child reference this is same as mentioned in liskov substitution
# principle.
colors = ['red', 'green', 'blue']
try:
    print(colors[3])
except Exception as e:
    print(e.__class__, '-', e)

a = ['red', 'green', 'blue']


# try:
#     print(a[5])
# except Exception as e:
#     if isinstance(e, IndexError):
#         print("Its IndexError Object")
#     else:
#         print("Its exception object")
#     print(e.__class__, e)

# handling division by zero error.
def division(a, b):
    try:
        return {
            'success': True,
            'message': 'OK',
            'result': a / b
        }
    except Exception as e:
        return {
            'success': False,
            'message': 'b cannot be zero',
            'result': None
        }


result = division(10, 2)
if result["success"]:
    print(result)
else:
    exit(-1)


# if possibility of multiple errors within the same program.


def division(a, b):
    try:
        return {
            'success': True,
            'message': 'OK',
            'result': a / b
        }

    # always the child should be defined first then the parent must be defined.
    except TypeError as e:
        return {
            'success': False,
            'message': 'Both a & b must be numbers',
            'result': None
        }
    except ZeroDivisionError as e:
        return {
            'success': False,
            'message': 'b cannot be zero',
            'result': None

        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
            'result': None
        }


result = division(10, '2')
print(result)


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        raise ValueError('b must not be zero') from ex


# result = divide(10, 0)
# print(result)

# using sys to print the error.
import sys

try:
    '20' / 2
except:
    exc_info = sys.exc_info()
    print(exc_info)

import traceback
def division(a, b):
    try:
        return {
            'success': True,
            'message': 'OK',
            'result': a / b
        }
    except(TypeError, ZeroDivisionError, Exception) as e:
        return {
            'success': False,
            'message': str(e),
            'traceback': traceback.format_exc(),
            'result': None
        }


result = division(10, 0)
print(result)

# Here we are creating a custom exception class to raise value error if input doesn't fall in the valid range

class FahrenheitError(Exception):
    min_f = 32
    max_f = 212

    def __init__(self, f):
        self.f = f

    def __str__(self):
        return f'The {self.f} is not in a valid range {self.min_f, self.max_f}'


# The following defines the fahrenheit_to_celsius function that accepts a temperature in Fahrenheit and returns a
# temperature in Celsius:
def fahrenheit_to_celsius(f: float) -> float:
    # The fahrenheit_to_celsius function raises the FahrenheitError exception if the input temperature is not in the
    # valid range. Otherwise, it converts the temperature from Fahrenheit to Celsius.
    if f < FahrenheitError.min_f or f > FahrenheitError.max_f:
        # if we raise the exception next immediate except block will catch the exception and print will call the magic method __str__.
        raise FahrenheitError(f)

    return (f - 32) * 5 / 9


f = input('Enter a temperature in Fahrenheit:')
try:
    # below code tries to convert the input passed from console to float if it fails to do that it will raise ValueError
    # if float conversion is successful then else will be executed
    f = float(f)
except ValueError as ex:
    print(ex)
else:
    try:
        # fahrenheit_to_celsius conversion is successful  then else will be executed
        c = fahrenheit_to_celsius(float(f))
    except FahrenheitError as ex:
        print(ex)
    else:
        print(f'{f} Fahrenheit = {c:.4f} Celsius')
