# If the integer object exists in memory then python instead of creating different object it will use existing object
# means they share same memory location .
a = 10
b = 10
print("--------")
print(id(a))
print(id(b))

