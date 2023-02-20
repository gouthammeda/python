import traceback

print("--------")
# mutability
print("Lists are mutable in nature")

aList = [1,2,3,4]
aList[3] = 0
print(aList)

# immutability

print("how ever strings are immutable in  nature")

try:
    aString = "Hello, How do you do?"
    aString[4] = 'd'

except Exception as ex:
    print("Exception occured while trying to change internal state of string object")
    print(traceback.format_exc())



