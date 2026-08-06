# read a whole file:
with open('/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.txt', 'r') as file:
    content = file.read()
    print(content)


# read the content of a file line by line:
with open('/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.txt','r') as file:
    for line in file:
        print(line.strip())


# writing a file(overwriting):
with open('/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.txt','w') as file:
    file.write("Hello world\n")
    file.write("i am here")

# write a file(without overwriting):
with open("/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.txt",'a') as file:
    file.write("\nhey my name is krishna \n")
    file.write("file operation executed")


# writing a list of lines to a file:
lines = ["krishna\n","Second line\n","third line"]
with open("/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.txt",'a') as file:
    file.writelines(lines)


# binary files: writing binary file:
data = b'\x00\x01\x02\x03\x04'
with open('/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.bin','wb') as file:
    file.write(data)


# reading binary file:
with open('/Users/a2251/Desktop/Python Programing/Chapter-12-File-Handeling/example.bin','rb') as file:
    contents = file.read()
    print(contents)


