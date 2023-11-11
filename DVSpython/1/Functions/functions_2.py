def sum_default_parameters(a, c, b=2):
    result = a + b + c
    return result


print(sum_default_parameters(1, 2))
# all the default parameters should be defined at the end after the non-default parameters and value given in
# arguments will overwrite the parameters.
print(sum_default_parameters(1, 4, 5))


def sum_default_parameters(a, c, f, b=2, d=5):
    result = a + b + c + d + f
    return result


# order is not mandatory
print(sum_default_parameters(a=1, d=3, f=4, c=5))
# always non-keyword args must be at beginning then the keyword arguments
print(sum_default_parameters(1, 2, d=6, f=4))


# variable number of arguments
def sum_variable_number_of_arguments(*args):
    print(args)
    a = 0
    total = 0
    finalstring = ""
    # print(type(args))
    while len(args) > a:
        value = args[a]
        # "int" in <class 'int'> --> True,"float" in <class 'float'> --> True
        if "int" in str(type(value)) or "float" in str(type(value)):
            total = total + args[a]
        # "str" in <class 'str'> --> True if str doesn't exist in <class 'str'> it will return False
        elif "str" in str(type(value)):
            finalString = finalString + args[a]
        else:
            print(value)
        a += 1
    return total, finalString


print(sum_variable_number_of_arguments(1, 4, 5, "Goutham", 6, 7, "Meda", 10.4, (1, 2, 3)))


# for *args parameter we can give different number of positional arguments and for **kwanything we can give different
# number of keyword arguments
def sum_keyword_variable_number_of_arguments(a, b, c, *args, **kwargs):
    print(a, b, c)
    print(type(args))
    print(type(kwargs))
    print(args)
    print(kwargs)


sum_keyword_variable_number_of_arguments(2, 3, 5, 6, 7, [1, 2, 3], d=5, f=0, e="Goutham Meda", m="Ravi")
