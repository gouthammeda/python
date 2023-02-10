# if code block--always pass relational expression so that they return boolean values
# always the inner code is tab indented.
"""
Syntax:
if <condition>:
    <code block>
<code after if>
"""

if 30 < 20:
    print("Debug1")
    print("Debug2")
    print("Debug3")
print("Statement after if code block")

# if the relational expression returns false then else part is executed
# without the exit() program moves to next line in execution, so we have to use exit to stop it.
timeofday = int(input("Enter time of the day:"))
if timeofday > 0 and 23 < timeofday:
    print("Not a valid input")
    exit()

if timeofday > 12:
    print("PM")
else:
    print("AM")
print("-------------")

# if-elif-else->when we want to check multiple conditions instead of executing the else immediately then we use it.
score = int(input("Calculation of letter grade for score of:"))
if score > 90:
    print("A")
# chained condition(score > 80 and score < 90)
elif 80 < score < 90:
    print("B")
elif 70 < score < 80:
    print("C")
else:
    print("D")

print("After if-elif-else statement")

# nested if-> there will be outer layer and inner layer of conditional statements that is called as nested conditional statement
age = int(input("Please enter your age:"))
gender = input("Please enter your gender(M OR F):")
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif 18 <= age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')

# single line if statement
if 'f' in 'foo': print('1');print(2);print('3')

print("----------")
x = 2
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

# what is difference between conditional statement and expression?
age = int(input("Enter your age to check whether you are minor or adult:"))
print("-----statement-----")
# Conditional Statements
if age < 21:
    print("minor")
else:
    print("adult")
print("-----Expression-----")
# Conditional Expression

# '<value to be executed when if condition is true>' if <condition> else '<value to be returned when condition is false>'
s = 'minor' if age < 21 else 'adult'
print(s)
print("-----------")
#
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
     )
print(s)
print("----")
