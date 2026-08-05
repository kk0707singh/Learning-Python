# why fuction needed
# a = int(input("enter the no: "))
# b = int(input("enter the no: "))
# c = int(input("enter the no: "))
# d = int(input("enter the no: "))

# average = (a+b+c+d)/4

# print(average)

# a = int(input("enter the no: "))
# b = int(input("enter the no: "))
# c = int(input("enter the no: "))
# d = int(input("enter the no: "))

# average = (a+b+c+d)/4

# print(average)

# a = int(input("enter the no: "))
# b = int(input("enter the no: "))
# c = int(input("enter the no: "))
# d = int(input("enter the no: "))

# average = (a+b+c+d)/4

# print(average)

# to avoid this we use function:
# function defenition
def avg():
    a = int(input("enter the no: "))
    b = int(input("enter the no: "))
    c = int(input("enter the no: "))
    d = int(input("enter the no: "))

    average = (a+b+c+d)/4

    print(average)
avg()       #function call
print("I have just started function ")  
avg()
avg()

# lambda function
# syntax to write lambda function
# lambda arguments: expression
addition = lambda a, b: a+b
type(addition)
print(addition(2, 5))

# basic functions:
def addition1(a, b):
    return a+b
print(addition1(2, 5))


# lambda function for even odd:
even = lambda num:num%2==0