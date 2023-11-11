"""
Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent accidental modification of data
"""


class Computer:

    def __init__(self):
        # private variable i.e., scope of it is maintained only within the class they can't be changed outside class
        # and can be accessed only using the getter and setter methods mentioned in the class these symbols are used
        # to denote access modifiers like private, public here it is private.
        self.__maxprice = 900

    # sell: Getter method to get the value of __maxprice
    def sell(self):
        return self.__maxprice

    # setMaxPrice: Setter method used to set new price for __maxprice
    def setMaxPrice(self, price):
        self.__maxprice = price

    # private method: this is accessible only within the class
    def __updateSoftware(self):
        print("updating software")


c = Computer()
max_value = c.sell()
print("Value of computer today is:" + str(max_value))

# Another instance level called __maxprice
c.__maxprice = 1000
print(c.__maxprice)

max_value = c.sell()
# private maxprice | public __maxPrice
print("Value of computer today is:" + str(max_value))
