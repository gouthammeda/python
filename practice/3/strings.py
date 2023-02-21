print("-----slicing------")
# a[start:end]
a = "Be Optimistic"

print(a[0:4])  # prints from start till before the 4th Index.
print(a[1:7])
print(a[7:len(a)])  # starts from 7 until length of a
print(a[:8])  # starts from 0 till before 8th Index.
print(a[8:])  # starts from 8th index till end of the string.
print(a[:])
print(a[-8:-1])  # starts from 8th index in reverse order to index before -1
print(a[:-10])  # from end of the string to -10 index
print(a[-10:])  # from -10 to end of string.

print("-----step--------")
# Take two steps/index forward including current index.
print(a[0:7:2])
print(a[0:7:5])

# Note: when using a reverse step the lower boundary should be higher index and upper boundary should be lower index.
print(a[13:2:-1])
print(a[13:2:-2])

print(a[::-1])

# TODO print the elements of the string in reverse order using tail recursion

print(a[:6] + 'U' + a[7:])

colors = ['red', 'green', 'blue', 'orange']
# create a slice object whose start is 0, stop is 4, and step is 2.
s = slice(0, 4, 2)
# print(s)

# return a tuple of indices of slice of sequence whose length is length of colors list.
t = s.indices(len(colors))
print(t)

for index in range(*t):
    print("Index:", index)
    print("Value:", colors[index])

# for i in range(0, 4, 2):
#     print(i)

# we have to give you start, end and step value
print(colors[0:4:2])

# converts integer 65 to ASCII character('A')
y = chr(65)
print(type(y), y)

for i in range(65, 65+26):
    print(chr(i), end=",")

# printing ASCII characters until its range.
start = 0
end = 1114111

# try:
#     for i in range(start, end+2):
#         a = chr(i)
#         print(a, end=",")
# except ValueError:
#     print("ValueError for i =", i)

# ord() does the reverse of chr()
# convert ascII unicode character 'A' to 65
y = ord('A')
print(type(y),y)

alphabet_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in alphabet_list:
    print(ord(i), end=",")
print(end="\n")
# this raises a type error if length of input string is not equal to one.
try:
    y = ord('Hi')
except Exception as ex:
    print(ex)

# String interpolation
age = 26
salary = 10000
name = "Goutham Meda"

# Approach 1: concat here we have to use str() to concatenate with integer with string
aString = "Name:" + name + ";Age:" + str(age) + ";Salary:" + str(salary)
print(aString)

# Format Method
print("Name:{};Age:{};Salary:{}".format(name, age, salary))
print("Name:{2};Age:{1};Salary:{0}".format(name, age, salary))
print("Name:{n};Age:{a};Salary:{sal}".format(n=name, a=age, sal=salary))

result = 100/777
print(result)

# don't add spaces before decimal string and consider 5 precision value out of 16
print("The result was {r:0.5f}".format(r=result))
# add 10-4 = 6 spaces before decimal string while printing, consider 3 precision values out of 16 while printing.
print("The result was {f:10.2f}".format(f=result))

# String case conversion methods
aString = 'egG BacOn SauSAGE loBSter'
print(aString.lower())
print(aString.upper())
print(aString.capitalize())
print(aString.title())
print(aString.swapcase())

print("---seek and find methods-----")
aString = 'spam ham clam jam'
# count takes a string pattern as input and count number of times it is observed in the input
result = aString.count('am')
print(result)

print(aString[0:10].count("am"))

# endswith checks for the pattern present if exists then print with return true.

print('spam ham clam jam'.endswith('jam'))
print('spam ham clam jam'.endswith('jam', 0, 9))

# vice versa of ends with is startswith
print('spam ham clam jam'.startswith('spam'))
print('spam ham clam jam'.startswith('spam', 0, 9))

s = 'spam ham clam jam'
print(s.startswith('spam',0,9))


s = 'spam bacon egg sausage'
print(s.find('egg'))

print(aString.find('am'))

# output = -1 if pattern doesn't exist.
print(aString.find("amiam"))

# rfind -> returns last occurrence of patterns find starting index from right to left

print(aString.rfind('am'))

# index works similar to find the but if pattern is not it throws exception.
print(aString.index('am'))
print(aString.rindex('am'))

#print(aString.index('amiam'))






























