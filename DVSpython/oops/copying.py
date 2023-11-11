import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]

# when we create new_list as reference variable then old list reference is copied into new_list so any changes done
# to new list will affect old_list. reference copy
new_list = old_list
new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of new List:', id(new_list))
print("---------")
new_list.append([10, 20])
print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
# this is called as shallow(little-depth) copy the value of old_list is being copied into new_list but with
# different memory location
new_list = copy.copy(old_list)

print(id(old_list))
print(id(new_list))

# when we try to change the new_list automatically old_list is also updated as reflection.
new_list[2][2] = 9

print(old_list)
print(new_list)

# when append change is only happening to new_list but not to the old one but assignment operator apply changes to
# both of lists.
new_list.append([10, 20])
print(old_list)
print(new_list)

# if we perform any change to the existing element state in list then it is affecting both the lists then it is doing
# shallow copy but if we are not touching the existing element but adding new element then change is happening to
# only that list but not both the lists. memory locations are different.
print(id(old_list))
print(id(new_list))

# it is creating a new object, new memory location will be created and that address will be stored in old_list
old_list = copy.copy(new_list)
print("here id is:", id(old_list))
print(old_list)

import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]

# each object has its own memory location, so if we perform any of the reassignment operation reflection will not
# happen on them.
new_list = copy.deepcopy(old_list)

new_list[2][2] = 9
print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of new List:', id(new_list))

print("----Deep copy append----")
new_list.append([10, 20])
print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of new List:', id(new_list))


