from functools import reduce

lam1 = lambda x:x+1
print(lam1)
print("-----")
lam2 = lambda x,y: x+y
print(lam2(2, 4))
print("------")
full_name = lambda first, last: f'full name:{first.title()}{last.title()}'
print(full_name("Goutham", "Meda"))
print("------")


# implementing x and func(x)
high_ord_func = lambda x, func: x + func(x)

print(high_ord_func(2, lambda x: x*x))
print(high_ord_func(2, lambda x: x+3))

# parameters x,y,func
high_ord_func = lambda x,y,func:func(x,y)
print(high_ord_func(2,3,lambda x,y:x*x))
print("--------")


# python closures and for loop:
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply


multipliers = []
for x in range(1,4):
    multipliers.append(multiplier(x))

m1, m2, m3 = multipliers

print(m1(10))
print(m2(10))
print(m3(10))
print("----------")


def outer_func(x):
    y = 4
    return lambda z: x+y+z


for i in range(3):
    closure = outer_func(i)
    print(f"closure({i +5})={closure(i+5)}")

print("----------")

# map(function, containers)
# one to one mapping there will always be one output for a given input, and no of inputs will be equal to no of outputs


def multiply_with_2(x):
    return x * 2


aList = [1,2,3,4,5,6]
x_map = map(lambda x: x*2, aList)
print(list(x_map))

# map with udf as an argument

x_map = map(multiply_with_2,aList)
print(list(x_map))

x_map = map(lambda x:x.upper(), ['cat','dog','cow'])
print(list(x_map))
print("-----")

v_filter = filter(lambda x:'o' in x,['cat','dog','cow'])
print(list(v_filter))

# filter(function, containers)
# 1 -> 1 mapping => each item in the iterable that is passed an input to the filter will be send as an input to either lamdba or UDF and apply the relation epres
# and number of inputs will always be equal to number of outputs
v_filter = filter(lambda x: x > 5, aList)
print(list(v_filter))

even = lambda x: x % 2 == 0
print(list(filter(even, range(11))))
print("--------------------------------------")

# aList = [1, 2, 3, 4, 5, 6]


def reduce_int(x, y):
    return x + y

reduced_value = reduce(lambda x, y: x + y, aList)
print(reduced_value)

reduced_value = reduce(reduce_int, aList)
print(reduced_value)

reduced_value = reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow'])
print(reduced_value)

def reduce_to_value(acc,pair):
    print(acc)
    print(pair[0])
    print("----------")
    return acc + pair[0]


pairs = [(1,'a'),(2,'b'),(3,'c')]
reduced_value = reduce(reduce_to_value, pairs,0)
print(reduced_value)

print("---------------------------------------")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

value = sum(x[0] for x in pairs)
print(value)
















