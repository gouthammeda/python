# sets always contain unique number of elements also they are unordered elements within it.
my_set = {1, 2, 3}
print(my_set)

# they also contain heterogeneous elements with in it.
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

# we can generate set from a list.
my_set = set([1, 2, 3, 2])
print(my_set)

my_set = {1, 3}
# it will flatten all the elements and pass it as input to my_set.
my_set.update([4, 5], {1, 6, 8}, (1, 2, 9))
print(my_set)

my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard will remove if element present or else do nothing
my_set.discard(4)
print(my_set)

# remove will element and raise error of element is not present.
my_set.remove(6)
print(my_set)

my_set = set("HelloWorld")
print(my_set)

# pop an element
print(my_set.pop())
print(my_set.pop())

print(my_set)

# clear my_set
my_set.clear()
print(my_set)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# perform union of A and B sets
print(A | B)

A.union(B)
B.union(A)

# perform intersection of a and b sets.
print(A & B)
A.intersection(B)
B.intersection(A)

# difference operation gets only the elements of A that are not present in B
print(A - B)
print(A.difference(B))

# gets only the elements of B that are not present in A
print(B - A)
print(B.difference(A))

# It will not give the common elements between both the sets.
print(A ^ B)

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

x1 = {1, 3, 5}
x2 = {2, 4, 6}

# check if the both sets have no elements in common
print(x1.isdisjoint(x2))
print(x1 & x2)

# all the elements of x1 are present in x2 then issubset returns true
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz', 'qux', 'quux'}
print(x1.issubset(x2))
print(x1 <= x2)

# x2 should contain all the elements of x1 and the size of x1 should be less than x2 then it is proper subset.
x1 = {'foo', 'bar'}
x2 = {'foo', 'bar', 'baz'}
print(x1 < x2)

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
print(x1 < x2)

# all the elements of x2 are present in x1 then it is superset returns true.
x1 = {'foo', 'bar', 'baz'}
print(x1.issuperset({'foo', 'bar'}))  # True

x2 = {'baz', 'qux', 'quux'}
print(x1 >= x2)  # False
# x1 should contain all the elements of x2 also they can't be identical.
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar'}
print(x1 > x2)  # True

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'bar', 'baz'}
print(x1 > x2)  # False

# Python Frozenset(Immutable sets) : Frozenset is a new class that has the characteristics of a set, but its elements
# cannot be changed once assigned.
x = frozenset(['foo', 'bar', 'baz'])
# provides intersection of both the sets.
print(x & {'baz', 'qux', 'quux'})
