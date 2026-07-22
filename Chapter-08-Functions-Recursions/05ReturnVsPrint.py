"""
=========================================================
TOPIC : print() vs return()
Author : Krishna Kant
Purpose : Revision Notes
=========================================================
"""

# =========================================================
# Question 1
# Function is defined but never called.
# =========================================================

def hello():
    print("Hello")

print("Python")

# Output:
# Python


# =========================================================
# Question 2
# Function is called.
# =========================================================

def hello():
    print("Hello")

print("Python")
hello()
print("Bye")

# Output:
# Python
# Hello
# Bye


# =========================================================
# Question 3
# Parameter and Argument
# =========================================================

def country(city):
    print(city)

country("Delhi")
country("Mumbai")

# Output:
# Delhi
# Mumbai


# =========================================================
# Question 4
# print() inside function
# =========================================================

def add(a, b):
    print(a + b)

x = add(10, 20)

print(x)

# Output:
# 30
# None


# =========================================================
# Question 5
# return inside function
# =========================================================

def add(a, b):
    return a + b

print(add(10, 20))

# Output:
# 30


# =========================================================
# Question 6
# return stores value in variable
# =========================================================

def square(n):
    return n * n

x = square(5)

print(x)

# Output:
# 25


# =========================================================
# Question 7
# print() returns None
# =========================================================

def greet(name, ending):
    return print("Good Day", name, ending)

a = greet("Krishna", "Thank You!")

print(a)

# Output:
# Good Day Krishna Thank You!
# None


# =========================================================
# Question 8
# print() returns None
# =========================================================

def test():
    x = print("Python")
    return x

a = test()

print(a)

# Output:
# Python
# None


# =========================================================
# Question 9
# print() + return together
# =========================================================

def test():
    x = "Python"
    print(x)
    return x

a = test()

print(a)

# Output:
# Python
# Python


# =========================================================
# Question 10
# Code after return never executes
# =========================================================

def test():
    return "Python"
    print("Java")

print(test())

# Output:
# Python


# =========================================================
# Question 11
# print() before return
# =========================================================

def demo():
    print("A")
    return "B"
    print("C")

x = demo()

print(x)

# Output:
# A
# B


# =========================================================
# Question 12
# print() + return
# =========================================================

def square(x):
    print(x)
    return x * x

y = square(4)

print(y)

# Output:
# 4
# 16


# =========================================================
# Question 13
# Multiple Parameters
# =========================================================

def greet(name, ending):
    print("Good Day", name, ending)

greet("Krishna", "Thank You!")
greet("Divya", "Thank You!")
greet("Priyanka", "Thank You!")

# Output:
# Good Day Krishna Thank You!
# Good Day Divya Thank You!
# Good Day Priyanka Thank You!


# =========================================================
# Question 14
# return can be stored
# =========================================================

def multiply(a, b):
    return a * b

result = multiply(5, 6)

print(result)

# Output:
# 30


# =========================================================
# Question 15
# print() cannot be stored
# =========================================================

x = print("Python")

print(x)

# Output:
# Python
# None