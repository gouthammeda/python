"""
Dictionary: Mutable objects.
"""

aDict = {
    "name": "Goutham",
    "age": 30,
    "is_married": True,
    "departments": ["IT", "Finance"],
    "address": {
        "add1": "106 Apartment",
        "add2": "Begur",
        "lat-lon": [-1.0234, 0.9876],
        "previous_address": {
            "add1": "106,Apartment1",
            "add2": "Begur1",
            "lat-lon": [-1.0235, 0.9870]
        }
    }
}
adepartment_list = aDict["departments"]
print(adepartment_list)
address = aDict["address"]
# address2 = address["add2"]
# print(address2)

pre_add = address["previous_address"]
add2 = pre_add["add2"]
print(add2)

print("hi",((aDict["address"])["previous_address"])["add2"])

print("------create dictionary-------")
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# by calling constructor of dict class
my_dict1 = dict({1: 'apple', 2: 'ball'})
print(my_dict1)

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])
print("------Accessing elements from a dictionary-----")
# Accessing elements from dictionary.

aDict = {
    "firstname": "Prudhvi",
    "lastname": "Akella",
    "age": 28,
    "height": 5.6,
    "is_married": True,
    "lat_long": [1.146, 4.096],
    "addresses": [
        {
            "address1": "dno:8-13-11",
            "address2": "",
            "pincode": 533101
        },
        {
            "address1": "dno:8-14-16",
            "address2": "",
            "pincode": 533102,
            "address3": {
                "city": "hyd",
                "state": "AP"
            }
        }
    ]
}

print("-------Approach 1-------")
firstname = aDict.get("firstname", None)

print("-------Approach 2------")
firstname = aDict["firstname"]

print("-----updating the value of a key------")
aDict["firstname"] = "Ravi"
aDict["lastname"] = "K"
print(aDict)

print("-----Accessing the remaining elements------")

print(aDict['height'])
print(aDict['addresses'][1]['pincode'])  # 533102
print(aDict['addresses'][1]['address3']['state'])  # AP
print(aDict['addresses'][1].get('address3', 'NA'))  # {
#     "city": "hyd",
#     "state": "AP"
# }
print(aDict['addresses'][0].get('address3', 'NA'))  # NA

output_dict = aDict
state = output_dict['addresses'][1]['address3']['state']  # AP

city = output_dict['addresses'][1]['address3'][
    'city']  # HYD # get the value of city(KEY)  from addresses.1.address3 and storing the value into city variable
output_dict['addresses'][1][
    'state'] = state  # create key state under the addresses 1st element and assign value stored in state variable to it
output_dict['addresses'][1][
    'city'] = city  # create key city under the addresses 1st element and assign value stored in state variable to it
output_dict['addresses'][1]['address3'] = {}

print(output_dict)

print("---popping elements from a dictionary---")

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item and returns value
print(squares.pop(4))
print(squares)

print(squares.popitem())

print(squares)

squares.clear()

# remove all items
squares.clear()
print(squares)

# delete the dictionary itself
del squares

print("---getting keys and values as a list---")
print(output_dict.keys())
print(output_dict.values())

print("-----Dictionary Methods----")
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)

for item in marks.items():
    print(item)

print("---Dictionary Comprehension----")

squares = {x: x * x for x in range(6)}
print(squares)

squares = {}
for x in range(6):
    squares[x] = x * x
print(squares)

odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
print(odd_squares)

print("----Dictionary Membership Test----")
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

print(1 in squares)

print(2 not in squares)

print(49 in squares)
print("--------------")

aDict = {
    "firstname": "Prudhvi",
    "lastname": "Akella",
    "age": 28,
    "height": 5.6,
    "is_married": True,
    "lat_long": [1.146, 4.096],
    "addresses": [
        {
            "address1": "dno:8-13-11",
            "address2": "",
            "pincode": 533101
        },
        {
            "address1": "dno:8-14-16",
            "address2": "",
            "pincode": 533102,
            "address3": {
                "city": "hyd",
                "state": "AP"
            }
        }
    ]
}

# updating a key in a dictionary which contains list of json's or dictionaries as a value.
new_elements = []

for element in aDict['addresses']:
    keys = element.keys()
    print(keys)
    if 'address3' in keys:
        element.pop('address3')
        new_elements.append(element)
    else:
        new_elements.append(element)

print(new_elements)
output_dict['addresses'] = new_elements
print("output dictionary is", output_dict)
print(aDict.keys())



