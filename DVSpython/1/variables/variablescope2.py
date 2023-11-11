def f(k):
    k += 'GFG'
    return k


# Global scope
s = "I love Python"
# this approach is better to change the value inside the local scope of function as the copy of s is passed to
# function memory and the result obtained is assigned a new value rather than changing the state/value in global scope.
s_concat = f(s)
print(s_concat)


def f():
    global i  # if we don't define global it will be read only inside that particular local function,
    # once we assign it with global keyword we can overwrite it with any of the other functions here we are trying to
    # change value of variable from module stack-frame in function stack-frame hence global need to be used.
    i += 'GFG'
    print(i)


# global scope
i = "I love Python"
i_concat = f()
print(i_concat)


def calculation():
    global place
    place = "Cape Town"
    name = "John"

    print(globals())
    # we should always use locals inside the function only.
    print(locals())
    print("place in global:", 'place' in globals())
    print("place in local:", 'place' in locals())
    print("name in global:", 'name' in globals())
    print("name in local:", 'name' in locals())
    return


place = "Berlin"
print(place)
calculation()
