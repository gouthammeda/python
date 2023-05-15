# 5,4,3,2,1
n = int(input("Enter a number:"))
"""
while <condition>:
    <while code block>
the while code block continues to execute until the condition becomes false.
"""
while n > 0:
    n -= 1
    if n == 0:
        print(n, end="\n")
    else:
        print(n, end=",")
print("statement after the while")

# str1 = "hi how are you"
# output = "you are how hi"
str1 = "how are you"
a = str1.split(" ")
length = len(a)
print(length)
i = 0
b = []
while length > 0:
    i = i - 1
    b.append(a[i])
    length = length - 1

for ele in b:
    print(ele, end=" ")
