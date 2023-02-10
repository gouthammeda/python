def capture_inputs():
    firstname = input("Enter first name:")
    lastname = input("Enter last name:")
    age = input("Enter age")
    return firstname, lastname, age


# TODO make this function print first and last name as invalid when int is passed instead of string
def validate_inputs(firstname, lastname, age):
    are_checks_passed = True
    # check whether firstname and last name are strings
    print(firstname)
    print(type(firstname))
    print(str(type(firstname)))
    print(str(type(lastname)))
    check = 'str' in str(type(firstname)) and 'str' in str(type(lastname))
    print(check)
    if not check:
        print("inside if")
        are_checks_passed = False
        print("Firstname and last name are not valid")
    age = int(age)
    if not 'int' in str(type(age)):
        are_checks_passed = False
        print("age should be number")
    return are_checks_passed


def business_logic(firstname, lastname, age):
    return firstname + " " + lastname + " " + str(age)


def main():
    # inputs
    firstname, lastname, age = capture_inputs()
    print("type of lastname is", type(lastname))
    # validation
    are_checks_passed = validate_inputs(firstname, lastname, age)
    if not are_checks_passed:
        exit()
    # business logic
    print(business_logic(firstname, lastname, age))


if __name__ == '__main__':
    main()
