"""
Lists: Mutable objects, Heterogeneous in nature.
"""

Int_List = [1, 2, 3, 4, 5]
float_list = [0.4, 0.5, 0.6, 0.7]
String_list = ["Goutham", "Meda", "Kavi"]
Mix_List = [1, 2, 3, 4, "Goutham Meda", 10.5, True]

# change the value of an index.
String_list[0] = "Ruppu"
print(String_list)

# using slicing to get elements from 0 until 1.
print(String_list[0:2])
# printing the length of list.
print(len(String_list))
# converting string to a list.
aString = "I am converting into list"
aList = list(aString)

print(aString)
print(aList)

# concat multiple lists
newList = String_list + Mix_List + [0, 8, 10]
print(newList)

# adding element to list
String_list.append("New element")
print(String_list)

# pop by default removes n-1 element if nothing is specified to it.
poped_element = String_list.pop()
print(poped_element)

# add elements at the head of list
head_List = [2]
head_element_list = head_List + String_list
print(head_element_list)

# adding new elements at 3 index.
print(head_element_list[0:3] + [1, 2, 3] + head_element_list[3:])

# sort a list
aList = [5, 2, 9, 8, 4, 5]
# sorting in ascending order.
aList.sort(reverse=False)
print(aList)
# sort in descending order.
aList.sort(reverse=True)
print(aList)

# :: consider all elements and then reverse elements in the list.
aList = [-1, 2, 3, 4, 5]
print(aList[::-1])
aList.reverse()
print(aList)

# getting String from list
aList = ['I', ' ', 'k', 'n', 'o', 'w', ' ', 't', 'h', 'i', 's']
aString_from_List = "".join(aList)
print(aString_from_List)

aString_from_List = "::".join(aList)
print(aString_from_List)

aString_from_List = "abc abc abc".join(aList)
print(aString_from_List)

# split is used to divide a string into list based on pattern.
aString = "Hello,how,are,you,doing?"
print(aString.split(','))

aString = "Hello how are you doing?"
print(aString.split())

moby = 'Call me Ishmael.\nSome years ago- never mind how long precisely-\nhaving little or no money in my purse,' \
       '\nand nothing particular to interest me on shore,\nI thought I would sail about a little and see the watery ' \
       'part of the world.\n '

print(moby.split('\n'))
print(moby.splitlines())











