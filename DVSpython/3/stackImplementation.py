from queue import LifoQueue

stack = LifoQueue(maxsize=4)
print(stack.qsize())

# put is used to push elements into the stack.
stack.put('a')
stack.put('b')
stack.put('c')
stack.put(21)

# checks if stack size is full and returns true if it is.
print("Full:", stack.full())
# returns the size of the stack.
print("Size:", stack.qsize())


print("Elements popped from the stack")
# get is used to pop elements from the stack in last in first out order.
print(stack.get())
print(stack.get())
print(stack.get())
print(stack.get())

# check if stack size is empty and returns true if it is empty.
print("\nEmpty:", stack.empty())

