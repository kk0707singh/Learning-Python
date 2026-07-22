# # PRACTICE SET 6:
# # QUESTION1: program to find the greatest of four number entered by user
a1 = int(input("Enter the no: "))
a2 = int(input("Enter the no: "))
a3 = int(input("Enter the no: "))
a4 = int(input("Enter the no: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("A1 is greatest ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("A2 is greatest ",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("A3 is freatest ",a3)
else:
    print("A4 is greatest ",a4)


# another shortest way to solve this
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))

print("Greatest number is:", max(a, b, c, d))

# QUESTION2: Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.
m1 = int(input("Enter marks of each subject: "))
m2 = int(input("Enter marks of each subject: "))
m3 = int(input("Enter marks of each subject: "))
total_percentage = (((m1+m2+m3)/300)*100)
print("Yeah I got! : ", total_percentage)
if(m1>=33 and m2>=33 and m3>=33 and total_percentage >= 40):
    print("Your are Promoted: ",total_percentage)
else:
    print("fail! try Again: ",total_percentage)

# QUESTION3: A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
word = input("enter your comment: ").lower()
s1 = "Make a lot of Money".lower()
s2 = "Buy now".lower()
s3 = "Subscribe this".lower()
s4 = "Click this".lower()

if((s1 in word) or (s2 in word) or (s3 in word) or (s4 in word)):
    print(" this is spam comment: ")
else:
    print(" this is not a spam! ")


# QUESTION4: Write a program to find whether a given username contains less than 10
# characters or not.
user_name = input("Enter your User name: ")
if(len(user_name) <= 10):
    print("username is less than or equal to 10 characters ")
else:
    print("username contains more than 10 characters ")


# QUESTION5: Write a program which finds out whether a given name is present in a list or not.
list_of_students = ["rohan", "Mohan", "Ram", "Shyam", "Krishna"]
name = input("Enter your name to check in the list: ")
if(name in list_of_students):
    print("You are in the list")
else:
    print("You are not in the list")


# QUESTION6: 
'''
Write a program to calculate the grade of a student from his marks from the
following scheme:
90 - 100 => Ex
80 - 90 => A
70 - 80 => B
60 - 70 =>C
50 - 60 => D
<50 => F
'''
total_marks = int(input("Enter your marks to check the grade: "))
if(total_marks >= 90 and total_marks <= 100):
    print("your garde is Excellent!: ",total_marks)

elif(total_marks >= 80 and total_marks < 90):
    print("Your Grade is A: ",total_marks)

elif(total_marks >= 70 and total_marks < 80):
    print("your Grade is B: ",total_marks)

elif(total_marks >= 60 and total_marks < 70):
    print("your Grade is C: ",total_marks)

elif(total_marks >= 50 and total_marks < 60):
    print("your Grade is D: ",total_marks)

elif(total_marks <= 50):
    print("your Grade is F! Work hard: ",total_marks)
print("all good",total_marks)

# QUESTION7: Write a program to find out whether a given post is talking about “Harry” or not.
post = input("Enter your thaughts here! ")
if("Harry".lower() in post.lower()):
    print("This post is talking about you: ")
else:
    print("This post is not about you: ")
