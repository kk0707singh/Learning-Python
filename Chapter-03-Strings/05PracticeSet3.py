# PRACTICE SET 3
# QUESTION1: program to display a user entered name followed by Good Afternoon using input() function
a = input("Enter Your Name: ")
print("Good Afternood",a)

# QUESTION2: program to fill a letter template with name and date
# letter = ''' Dear <|Name|>,
#              You are selected!
#              <|Date|>'''
letter = ''' Dear <|Name|>,
             You are selected!
             <|Date|>'''
name = input("Enter Your Name: ")
date = input("Enter Date: ")
print(letter.replace("<|Name|>",name). replace("<|Date|>",date))

# QUESTION3: Program to detect double spacing
name1 = input("Enter name with double spacing: ")
print(name1.find("  "))

# QUESTION4: Rreplace double space into single spaces
MyName = "Krishna  Kant  Singh"
print(MyName.replace("  "," "))
# bonus for QUESTION4 if we print MyName again this will print the same string that has been declare 
# Earlier so it means strings are immutable