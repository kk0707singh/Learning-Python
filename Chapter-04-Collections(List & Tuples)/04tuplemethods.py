# ========================= TUPLE METHODS =========================

a = (1, 45, 342, False, 45, "Rohan")

# count(value) -> Counts how many times a value appears in the tuple.
print(a.count(45))        # Output: 2

# index(value) -> Returns the index of the first occurrence of the value.
print(a.index(False))     # Output: 3
print(a.index(45))        # Output: 1


# ========================= TUPLE FUNCTIONS =========================

numbers = (10, 20, 30, 40)

# len(tuple) -> Returns the total number of elements.
print(len(numbers))       # Output: 4

# max(tuple) -> Returns the largest element.
print(max(numbers))       # Output: 40

# min(tuple) -> Returns the smallest element.
print(min(numbers))       # Output: 10

# sum(tuple) -> Returns the sum of all numeric elements.
print(sum(numbers))       # Output: 100

# sorted(tuple) -> Returns a NEW sorted list (not a tuple).
print(sorted((30, 10, 20)))   # Output: [10, 20, 30]

# tuple(iterable) -> Converts an iterable (like a list) into a tuple.
my_list = [1, 2, 3]
print(tuple(my_list))     # Output: (1, 2, 3)

# any(tuple) -> Returns True if at least one element is True (truthy).
print(any((0, False, "", 10)))   # Output: True

# all(tuple) -> Returns True only if all elements are True (truthy).
print(all((1, True, 5)))         # Output: True
print(all((1, 0, True)))         # Output: False