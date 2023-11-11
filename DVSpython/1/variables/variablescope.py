def f():
    # local variable-> variable is not available outside the function, once the value is returned back the allocated
    # memory for function execution will be de-allocated.
    k = "I love Python"
    print(k)


f()


# local variable to function will have preference than the global variable when both are same.
def func():
    s = "Me too."
    print(s)


if __name__ == "__main__":
    # Global scope --> variable is accessible inside the function as well as outside in print.
    s = "I love Python"
    func()
    print(s)




