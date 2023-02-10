a = int(input("Enter a number to calculate the factorial:"))

# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
fact = 1
while a > 1:
    fact *= a
    a -= 1
print(fact)

print("---------")


# Recursive function and Tail Recursion
# function call is keep happening until an exit condition is met.
# whenever a function call happens stack frame will be created and has to exist in memory, and it will be de-allocated once value has been given back.
# all the execution happens within the stackframe.Traditional recursion uses multiple stackframes but tail recursion uses only one stackframe.
def fact(a):
    if a == 1:
        return a
    return a * fact(a - 1)


print(fact(5))
print(fact(998))

# tail recursion-> Here there is no dependency that expression needs to be evaluated in the return statement, instead
# everything is done in the fact call itself using accumulator variable, so it uses only one stackframe.
"""
n = 3, acc = 1
fact(3,1)
fact(2,3)
fact(1,6)
return 6
"""


def fact(n, acc):
    if n == 1:
        return acc
    else:
        return fact(n - 1, n * acc)


print(fact(3, 1))


