age = int(input("enter your age: "))
if(age == 0):
    print("You are not born yet")
elif(age < 0):
    print("Your are entering invalid age! verify age ")
elif(age >= 18):
    print("you are mature!")
else:
    print("You are not mature!. be mature first ")
print("just verified age")


# Quick Quiz: Write a program to print yes when the age entered by the user is greater than or equal to 18.
number = int(input("Enter your age: "))
if(number >= 18):
    print("YES! the no. is greater than 18 or equal to 18: ")
else:
    print("NO! the no. is not greater than 18: ")