age = int(input("enter your age: "))
# if statement no 1:
if(age%2 == 0):
    print("Your age is a even no:")
# if statement no 2:
if(age == 0):
    print("You are not born yet")
elif(age < 0):
    print("Your are entering invalid age! verify age ")
elif(age >= 18):
    print("you are mature!")
else:
    print("You are not mature!. be mature first ")
print("just verified age")