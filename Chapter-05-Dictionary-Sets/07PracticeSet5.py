# Practice Set 5:
# QUESTION1: Program to create a dictionary of hindi words with values as their english translation. provide user with an option to look it up
translation = {
    "madad": "help",
    "mauj": "Enjoy",
    "hawa": "Air"
}

meaning = input("Enter the word you want the meaning of: ")
print(translation[meaning])
print(translation["madad"])

# other ways to do the same problem using user input
student = {}
student[input("enter First key in hindi: ")] = input("Enter Value in English: ")
student[input("enter second key in hindi: ")] = input("Enter Value in English: ")
student[input("enter third key in hindi: ")] = input("Enter Value in English: ")
student[input("enter fourth key in hindi: ")] = input("Enter Value in English: ")
print("Keys and Values are: ", student)
words = input("Enter words you want the meaning of: ")
print(student[words])

# QUESTION2: Program to input eight numbers from user to display all the unique numbers
s = set()
s.add(int(input("enter the number: ")))
s.add(int(input("enter the number: ")))
s.add(int(input("enter the number: ")))
s.add(int(input("enter the number: ")))
s.add(int(input("enter the number: ")))
s.add(int(input("enter the number: ")))
s.add(int(input("enter the number: ")))
print(s)

# QUESTION3: can we have a set with int 18 and str '18' as avalue in it
mixed = set()
mixed.add(int(input("enter the number: ")))
mixed.add(input("enter the number: "))
print(mixed)

# QUESTION4: What will be the length of the following set s:
'''
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
'''

s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print("set is: ", s)
print("length of the set is: ", len(s))

# QUESTION5: s = {}: what is the type of s:
s = {}
print("the type of s is: ", type(s))   #returns type dictionary

# QUESTION6: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d = {}
d[input("enter the name: ")] = input("Enter programming language: ")
d[input("enter the name: ")] = input("Enter programming language: ")
d[input("enter the name: ")] = input("Enter programming language: ")
d[input("enter the name: ")] = input("Enter programming language: ")
print(d)

# other ways to do the same problem
language = {}
name = input("Enter your name: ")
lang = input("enter programming language: ")
language.update({name:lang})

name = input("Enter your name: ")
lang = input("enter programming language: ")
language.update({name:lang})

name = input("Enter your name: ")
lang = input("enter programming language: ")
language.update({name:lang})

name = input("Enter your name: ")
lang = input("enter programming language: ")
language.update({name:lang})

print(language)

# QUESTION9: Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
# THIS WILL THROW ERROR BECAUSE WE CANT STORE LIST IN A SET