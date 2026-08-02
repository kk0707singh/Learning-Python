def goodDay(name, ending = "Thank You"):
    print(f"Good Day, {name}")
    print(ending)
goodDay("Archit")
goodDay("Krishna", "how are you: ")


# variable length argument
# positional argument
def print_nos(*krish):
    # generally we use *args but we are free to use any name for positional keyword arguments
    for number in krish:
        print(number)
print_nos(1, 2, 3, 4, 5, 6, "kk", "kks")

# keyword argument
def print_datails(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_datails(name="Krishna", age=26, country="india")


# combine bothpositional and keyword arguments we get:
def print_datails(*args, **kwargs):
    for val in args:
        print(f"positional args: {val}")

    for key, value in kwargs.items():
        print(f"keyword arguments: {key}:{value}")

print_datails(1, 2, 3, 4, 5, 6, "kk", "kks", name="Krishna", age=26, country="india")

# return statement
