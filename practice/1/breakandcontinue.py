# break statement-> control exits from the loop to outside statement once break is hit.
n = int(input("Enter your number:"))
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
print('Loop ended.')

aList = ['foo', 'bar', 'baz']
while True:  # infinite loop -> we use this when we don't know the exit condition.
    # once list becomes empty it returns none to while(come back) or
    # not(False) True that means we are breaking the continues loop using break statement.
    if not aList:
        break
    print(aList.pop(-1))
print("Statements after the while")

# continue will not exit the loop, but instead it will go to next immediate iteration by skipping the remaining steps for present iteration in the loop.
# print(2) will not be executed.
print('-----continue output-----')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print("Loop ended.")

# when while loop is made forcefully exited then else is not executed but when it is made to run all runs successfully then else is executed.
# else block is used to know the statements to execute if while got exited by itself or by the user. if while success then we will do certain things
# if it is exited by user then we will do another set of things.
print('-----else success case-----')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
else:
    print('Loop done.')
print('--Out side while--')

# for every iteration of first loop all the iterations of second loop are executed.
# when we pass 0 the condition fails and while will not execute no need to convert to boolean.
a = ['foo', 'bar']
while len(a):  # Outer --> bool(0) --> False, bool(anything) --> True
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):  # Inner --> bool(0) --> False, bool(anything) --> True
        print('>', b.pop(0))

# another way
a = ['foo', 'bar']
while a:  # Outer --> bool(0) --> False, bool(anything) --> True
    print(a.pop(0))
    b = ['baz', 'qux']
    while b:  # Inner --> bool(0) --> False, bool(anything) --> True
        print('>', b.pop(0))
