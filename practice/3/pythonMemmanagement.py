# heap memory is where the object gets created which is a data structure.
# whenever an object is created a table with references and count will get created once no object
# is using the reference then the count will be decremented, and it is deallocated

# for whole .py file the compiler will generate the .pyc file then each of the statement is executed by pvm.

# pvm contains the python memory manager which talks with os memory manager to create objects in private heap memory.
# few objects reference count will never be zero that is which has circular references and two objects reference each other.
# to reclaim memory in such cases we use garbage collector.

import gc
import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


numbers = [1, 2, 3]
numbers_id = id(numbers)

print(ref_count(numbers_id))

ranks = numbers
print(ref_count(numbers_id))

ranks = None
print(ref_count(numbers_id))

numbers = None
print(ref_count(numbers_id))

print("----------------")
print("understanding garbage collector")


def ref_count(address):
    return ctypes.c_long.from_address(address).value


# below function is used to check if object exists in the heap memory
def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True
    return False


class classA:
    def __init__(self):
        # we are creating an instance level variable b which is referring to B's object
        # at the time of object A creation we are also creating object B and storing the references
        # of object B into A's object.
        self.b_address = classB(self)
        # we are printing the id of A's object and id of B's object.
        print(f"A:{hex(id(self))},B:{hex(id(self.b_address))}")


class classB:
    def __init__(self, a):
        # we are having instance level variable a_address which we are passing address of A.
        self.a_address = a
        print(f'B:{hex(id(self))},A:{hex(id(self.a_address))}')


# we are disabling circular dependencies so that we can see the circular dependencies.
gc.disable()


a = classA()

a_id = id(a)
b_id = id(a.b_address)

# Instance of A has two references which is variable a and instance of B.
# and instance of B has one reference which is instance of A.
print(ref_count(a_id))
print(ref_count(b_id))

print(object_exists(a_id))
print(object_exists(b_id))

print("---------------")

a = None

print(ref_count(a_id))
print(ref_count(b_id))


print(object_exists(a_id))
print(object_exists(b_id))

# when a is set to none b is also set to none because we are accessing b_reference using a_reference
# the circular dependency exist that is both objects exists as none but direct connection to b is gone
# hence both are cleared from memory when gc.collect is run
gc.collect()

print(object_exists(a_id))
print(object_exists(b_id))

print(ref_count(a_id))
print(ref_count(b_id))
