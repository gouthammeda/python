aIntList = [1, 2, 3, 4]
aStrList = ["Goutham", "Meda", "XYZ"]
aFloatList = [1.01, 2.011, 202.1]
aBoolList = [True, False, True, False]
aMixList = ["Goutham", 1, 2, 9.0, False, [1, 2, 3]]

# print(aIntList[9])
print(aMixList[2])
print(len(aIntList))

aString = "Hello World"
print(aString[-4])

# .--> reference operator used to access method of a class
ret_value = aIntList.pop()
print(ret_value)
print(aIntList)
ret_value = aIntList.pop()
print(ret_value)
print(aIntList)
ret_value = aIntList.pop()
print(ret_value)
print(aIntList)
ret_value = aIntList.pop()
print(ret_value)
print(aIntList)
# ret_value = aIntList.pop()
# print(ret_value)
# print(aIntList)

# popping element of list using its index
aList = ["foo", "bar", 1, False, 2.3]
print(aList.pop(2))
print(aList)

# using while to print elements of list in reverse order.
aList = ["foo", "bar", 1, False, 2.3]
length_of_list = len(aList) - 1
while length_of_list >= 0:
    print("--------------")
    print("Index:", length_of_list)
    print("Value:", aList[length_of_list])
    length_of_list -= 1  # length_of_list = length_of_list - 1
print("----outside while---")

# printing elements of list
aList = ["foo", "bar", 1, False, 2.3]
itr = 0
length_of_list = len(aList)
while length_of_list > itr:
    print("-------")
    print("Index:", itr)
    print("Value:", aList[itr])
    itr += 1
print("----------")

# iterating over list using pop method
# aList will become empty only when all elements get popped from list
aList = ["foo", "bar", 1, False, 2.3]
print(aList)
while aList:
    print("--------")
    return_val = aList.pop(0)
    print("Value", return_val)
    print("Type", type(return_val))
print('---------')
print(aList)

# traversing forward and backward of list
aList = ["foo", "bar", 1, False, 2.3]
aList_forward = ["foo", "bar", 1, False, 2.3]
while aList:
    print("-----")
    print("Reverse:", aList.pop(-1))
    print("Forward:", aList_forward.pop(0))
print("------break output----")


