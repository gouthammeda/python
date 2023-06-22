# opening a file in read mode
f = open("sample.txt", 'r')

# reading lines in a file
for line in f:
    # doing all your processing here
    print(line)

# close
f.close()

# we don't need to close the file connection once it is opened
with open("sample.txt", 'r') as file:
    for line in file:
        print(line)

with open("sample.txt",'r') as file:
    file_content = file.read()
    print(type(file_content))
    print(file_content)


with open("sample.txt", 'r') as file:
    # User can also pass optional argument to read method  offset
    # lets say want to read first 40 characters from a file
    first_40_chars = file.read(40)
    print(first_40_chars)
    print(len(first_40_chars))

    # tell method is used know the  current offset file handler is pointing to
    current_offset = file.tell()
    print(current_offset)

    print("-------- below logic is used to read the next set of 40 characters ----------")
    first_40_chars = file.read(40)
    print(first_40_chars)
    print(len(first_40_chars))
    # tell method is used know the  current offset file handler is pointing to
    current_offset = file.tell()
    print("current offset is",current_offset)

    # let's now reset the offset using seek
    file.seek(0)
    # tell method is used know the  current offset file handler is pointing to
    current_offset = file.tell()
    print("tell after offset reset", current_offset)
    print("--------Reading first 40 chars after seeking offset to 0 ----------")
    first_40_chars = file.read(40)
    print(first_40_chars)
    print(len(first_40_chars))

with open("sample.txt", 'r') as file:
    lines = file.readlines()
    # print(lines)
    for line in lines:
        print("first line is", line)


print("--writing data to file--")

file = open('sample_write.txt','w')

file.write("Hello World\n")
file.write("Be optimistic\n")
file.write("Everything will be alright\n")

file.close()







