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




