import sys
# we want something outside of program as input to our program.
# firstname = input("Please enter your firstname:")
# lastname = input("Please enter your lastname:")
# age = input("Please enter your age:")

# print("Hi "+firstname+" "+lastname+",\n"+"You are aged around:"+age)
# or
print('----------')
# print("Hi " + input("Please enter your firstname: ")+" "+input("Please enter your lastname: ")+",\n"+"You are aged
# around:"+input("Please enter your age: "))

# command line args--0th args is always the absolute path of the program.
# argv we need to import sys module and use agrv func.
cmd_line_args = sys.argv
# arg0 = cmd_line_args[0]
arg1 = cmd_line_args[1]
arg2 = int(cmd_line_args[2])
arg3 = int(cmd_line_args[3])

# print(arg0+" :"+arg1+" :"+str(arg2)+" :"+arg3)
print(arg1 + " :" + str(arg2) + " :" + str(arg3))
