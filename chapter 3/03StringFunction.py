name = "Krishna Kant"

# len() - Returns the length of the string
print(len(name))                          # 13

# endswith() - Checks if the string ends with a substring
print(name.endswith("shna"))             # False
print(name.endswith("ant"))              # True

# upper() - Converts all characters to uppercase
print(name.upper())                      # KRISHNA KANT

# lower() - Converts all characters to lowercase
print(name.lower())                      # krishna kant

# startswith() - Checks if the string starts with a substring
print(name.startswith("Kri"))            # True

# capitalize() - Capitalizes only the first character
print(name.capitalize())                 # Krishna kant

# title() - Capitalizes the first letter of each word
print(name.title())                      # Krishna Kant

# find() - Returns the index of the first occurrence
print(name.find("ant"))                  # 10

# replace() - Replaces a substring with another
print(name.replace("Kant", "Singh"))     # Krishna Singh

# count() - Counts the occurrences of a substring
print(name.count("a"))                   # 2

# strip() - Removes spaces from both ends
name_with_spaces = "   Krishna Kant   "
print(name_with_spaces.strip())          # Krishna Kant

# split() - Splits the string into a list
print(name.split())                      # ['Krishna', 'Kant']

# join() - Joins list elements into a string
words = ["Krishna", "Kant"]
print("-".join(words))                   # Krishna-Kant

# isalpha() - Checks if all characters are alphabets
print(name.isalpha())                    # False (because of the space)

# isdigit() - Checks if all characters are digits
print("12345".isdigit())                 # True

# isalnum() - Checks if all characters are alphabets or digits
print("Krishna123".isalnum())            # True