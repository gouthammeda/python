import copy

a_list = [1, 2, 3, 4, 5, 6]
print(id(a_list))

bList = a_list
print(id(bList))

# 10 is added to a list and blist
bList.append(10)
print(a_list)
print(bList)

# c_list and b_list have same references but are created in different memory locations.
c_list = copy.copy(bList)
print(id(c_list))

# but 3 is not added into blist and present only in c_list as they are pointing to two different memory locations.
c_list.append(3)
print(bList)
print(c_list)
