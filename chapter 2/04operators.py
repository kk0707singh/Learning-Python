# ARITHMATIC OPERATOR

a = 7
b = 4
c = a + b
print (c)

# ASSIGNMENT OPERATOR

a = 4-2  #assign 4-2 in variable a
b = 6
b +=3    #Increment the value of b by 3 and then assign it to b
print("the value of b while incresing: ", b)

b -=3    #Decrement the value of b by 3 and then assign it to b
print("the value of b while decreasing: ", b)

b *=3    #Multiply the value of b by 3 and then assign it to b
print("the value of b while Multiplying: ", b)

b /=3    #devide the value of b by 3 and then assign it to b
print("the value of b while Deviding: ", b)

print("total value of b after applying operator: ", a+b)


# COMPARISON OPERATOR 
#Always returns Bollean value either True or False

d = 5>6
print(d)    # Returns False

e = 5==5
print(e)


# truth table of OR. Atleast one condition is true it return true
print("Truth Table of OR: ")
print("True or False is: ", True or False)
print("True or True is: ", True or True)
print("False or True is: ", False or True)
print("False or false is: ", False or False)

# truth table of AND. both the condition should be True then only it returns True othervise it will Return False
print("Truth Table of AND: ")
print("True and False is: ", True and False)
print("True and True is: ", True and True)
print("False and True is: ", False and True)
print("False and false is: ", False and False)

# NOT it return False for True and returns True true for false 
print(not(True))
print(not(False))