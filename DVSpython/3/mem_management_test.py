# class A:
#     def add_object_to_me(self, other_object_reference):
#         self.another_object_address = other_object_reference
#
#
# class B:
#     def add_object_to_me(self, other_object_reference):
#         self.another_object_address = other_object_reference
#
#
# x = A()
# y = B()
#
# x.add_object_to_me(y)
# y.add_object_to_me(x)
#
# print(id(x))
# print(id(x.another_object_address))
# print("------------")
# print(id(y))
# print(id(y.another_object_address))

class A:
    def __init__(self):
        self.b = B(self)


class B:
    def __init__(self, another_object_ref):
        self.a = another_object_ref


x = A()

print(x)
print(x.b)
print(x.b.a)
