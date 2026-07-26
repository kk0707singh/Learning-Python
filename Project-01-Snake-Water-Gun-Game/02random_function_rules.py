# ============================================================
#                 PYTHON RANDOM MODULE - NOTES
# ============================================================

"""
The random module is used when we want Python to make a random
choice instead of us deciding the value.

Example:
---------
Games
Lottery
OTP (Demo)
Quiz App
Password Generator
Card Games
Dice Games
"""

import random


# ============================================================
# 1. random.randint(start, end)
# ============================================================

"""
Returns a random INTEGER between start and end.
Both start and end are included.
"""

print(random.randint(1, 6))

# Example Uses:
# Dice Game
# Guess the Number
# OTP (Simple Demo)
# Random Marks


# ============================================================
# 2. random.choice(sequence)
# ============================================================

"""
Chooses ONE random element from a list, tuple or string.
"""

fruits = ["Apple", "Banana", "Mango"]

print(random.choice(fruits))

# Example Uses:
# Snake Water Gun
# Rock Paper Scissors
# Random Movie Suggestion
# Random Quote
# Random Team Selection


# ============================================================
# 3. random.random()
# ============================================================

"""
Returns a random decimal number between 0 and 1.

0 <= number < 1
"""

print(random.random())

# Example Uses:
# Probability
# Simulations
# Chance based games


# ============================================================
# 4. random.uniform(start, end)
# ============================================================

"""
Returns a random decimal number between two numbers.
"""

print(random.uniform(10, 20))

# Example Uses:
# Random Temperature
# Physics Simulations
# Random Heights


# ============================================================
# 5. random.shuffle(list)
# ============================================================

"""
Shuffles the ORIGINAL list.

NOTE:
shuffle() changes the original list.
It does NOT return a new list.
"""

cards = [1,2,3,4,5]

random.shuffle(cards)

print(cards)

# Example Uses:
# Card Games
# Quiz Questions
# Flash Cards
# Random Order of Students


# ============================================================
# 6. random.sample(sequence, k)
# ============================================================

"""
Returns k UNIQUE random values.

Original list remains unchanged.
"""

numbers = [1,2,3,4,5,6,7,8]

print(random.sample(numbers, 3))

# Example Uses:
# Lottery
# Lucky Draw
# Interview Question Selection


# ============================================================
# 7. random.choices(sequence, k)
# ============================================================

"""
Returns multiple random values.

Duplicates ARE allowed.
"""

colors = ["Red", "Blue", "Green"]

print(random.choices(colors, k=5))

# Example Output

# ['Blue', 'Blue', 'Green', 'Red', 'Blue']

# Example Uses:
# Coin Toss Simulation
# Repeated Random Events
# Game Simulations


# ============================================================
# RANDOM STRING
# ============================================================

letters = "abcdefghijklmnopqrstuvwxyz"

print(random.choice(letters))

# Output:
# q
# m
# a


# ============================================================
# RANDOM PASSWORD (Simple)
# ============================================================

letters = "abcdefghijklmnopqrstuvwxyz"

password = ""

for i in range(5):
    password += random.choice(letters)

print(password)

# Output:
# abcde
# pqrxy
# mnopq


# ============================================================
# SUMMARY
# ============================================================

"""
randint()  -> Random Integer

choice()   -> One Random Item

random()   -> Decimal between 0 and 1

uniform()  -> Decimal between any two numbers

shuffle()  -> Shuffle original list

sample()   -> Multiple unique values

choices()  -> Multiple values (duplicates allowed)
"""