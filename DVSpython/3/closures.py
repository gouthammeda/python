# when non-local variable which is accessed inside the inner function, then combination of variable and
# inner function is called as closure.

def say1():
    greeting = 'Hello'

    # inner function/Auxiliary function
    def display():
        # as non-local variable is used inside display() makes a closure
        print(greeting)

    display()


say1()

print("-------")


# here say is a higher function as it is returning the display() as output when we call it.
def say():
    greeting = 'Hello'
    aInt = 10

    # Inner Function/ Auxiliary Function
    def display():
        # as nonlocal variable is used inside display() makes it Closure
        print(greeting)
        print(aInt)

    # returning Inner function (display) instead of executing it
    return display


display1 = say()
print(display1)  # prints the address of this function object
display1()  # Here inner function will happen and executes the function
print("----------------------------------------")

print(display1.__closure__)

print("----------------------------------------")


# here multiplier is a higher order function as it returns functions reference as an output for function call.
def multiplier(x):
    def multiply(y):
        return x * y

    return multiply

# these function calls create three closures.Each function multiplies a number with 1,3 and 3.


m1 = multiplier(1)
m2 = multiplier(2)
m3 = multiplier(3)

# execute functions of closures.
print(m1(10))
print(m2(10))
print(m3(10))

# print(multiplier(3)(10))


def outer_func(x):
    y = 4

    def inner_func(z):
        print(f"x={x},y={y},z={z}")
        return x + y + z

    return inner_func


for i in range(3):
    closure = outer_func(i)
    print(closure.__closure__)
    # print("closure({})={}".format(i+5, closure(i+5)))
    print(f"closure({i+5})={closure(i+5)}")










