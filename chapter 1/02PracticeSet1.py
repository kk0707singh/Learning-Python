# QUESTION1: print twinckle twinckle little star poem

print("""Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle twinkle little star
How I wonder what you are
Twinkle twinkle little star
Shining brightly and afar
Twinkle star dust all around
From the sky right to the ground
Twinkle twinkle little star
Shining brightly and afar
      """)


# QUESTION2: print table of 5 using REPL
# open command line and type python3 and then after we can perform any task


# QUESTION3: install an external module and use it to perform any task

from pyfiglet import Figlet
f = Figlet(font="slant")
print(f.renderText("Krishna"))



import pyttsx3
engine = pyttsx3.init()
engine.say("Hello Krishna, welcome to Python programming.")
engine.runAndWait()


# QUESTION4: write a python program to print the contents of a directory using the OS module. search online for the function which does that

import os
# Specify the directory path
path = "/"
# Get all files and folders
contents = os.listdir(path)
# Print each item
for item in contents:
    print(item)