# closure is when non-local variable is accessed inside the inner function, inner function is called as closure.

def say1():
    greeting = 'Hello'

    # inner function/Auxiliary function
    def display():
        # as non-local variable is used inside display() makes a closure
        print(greeting)

    display()

say1()

print("-------")


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


display = say()
print(display)  # prints the address of this function object
display()  # Here inner function will happen and executes the function
print("----------------------------------------")

print(display.__closure__)

print("----------------------------------------")
