# ==========================================================
# File Name : 06RevisionListTupleDictSets.py
# Python Revision Sheet: Lists, Tuples, Dictionaries & Sets
# ==========================================================

# ==========================================================
# 1. LIST
# ==========================================================

# List -> Ordered, Mutable, Allows Duplicates

l = [10, 20, 30]

# append() -> Adds one item at the end.
l.append(40)

# extend() -> Adds multiple items.
l.extend([50, 60])

# insert(index, value) -> Inserts at a specific position.
l.insert(1, 15)

# remove(value) -> Removes first matching value.
l.remove(20)

# pop() -> Removes and returns last element.
last = l.pop()

# pop(index) -> Removes and returns element at index.
removed = l.pop(1)

# count(value) -> Counts occurrences.
print(l.count(30))

# index(value) -> Returns first index.
print(l.index(30))

# sort() -> Sort ascending (modifies list).
nums = [81, 14, 5, 3, 7]
nums.sort()
print(nums)

# sort(reverse=True) -> Descending.
nums.sort(reverse=True)
print(nums)

# reverse() -> Reverse list.
nums.reverse()

# copy() -> Creates a shallow copy.
nums_copy = nums.copy()

# clear() -> Removes all elements.
temp = [1,2,3]
temp.clear()

# ---------- List Input ----------

marks = []
marks.append(int(input("Enter mark1: ")))
marks.append(int(input("Enter mark2: ")))
marks.append(int(input("Enter mark3: ")))
print(marks)

marks2 = list(map(int, input("Enter marks separated by commas: ").split(",")))
print(marks2)

# ---------- List Functions ----------

print(len(marks2))
print(sum(marks2))
print(max(marks2))
print(min(marks2))
print(sorted(marks2))
print(any(marks2))
print(all(marks2))
print(type(marks2))

# ==========================================================
# 2. TUPLE
# ==========================================================

# Tuple -> Ordered, Immutable, Allows Duplicates

t = (10,20,30,20)

# count() -> Counts occurrences.
print(t.count(20))

# index() -> Returns first index.
print(t.index(30))

# Tuple Input
t2 = tuple(input("Enter names separated by commas: ").split(","))

# Tuple Functions
print(len(t))
print(sum((10,20,30)))
print(max((10,20,30)))
print(min((10,20,30)))
print(sorted((30,10,20)))
print(any((0,0,5)))
print(all((1,2,3)))
print(type(t))

# ==========================================================
# 3. DICTIONARY
# ==========================================================

student = {
    "name":"Krishna",
    "age":26,
    "city":"Delhi"
}

# Access value
print(student["name"])

# get() -> Safe access.
print(student.get("salary"))
print(student.get("salary","Not Found"))

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# Loop through dictionary
for key, value in student.items():
    print(key, value)

# update()
student.update({"age":27, "country":"India"})
print(student)

# pop(key)
print(student.pop("city"))
print(student)

# popitem()
print(student.popitem())
print(student)

# setdefault()
student.setdefault("salary",25000)
student.setdefault("age",30)
print(student)

# copy()
student_copy = student.copy()

# clear()
temp_dict = {"a":1}
temp_dict.clear()

# Find key from value
for key, value in student.items():
    if value == 27:
        print("Key:", key)

# Delete specific key
del student["age"]
print(student)

# ==========================================================
# 4. SET
# ==========================================================

# Set -> Unordered, Mutable, No Duplicates

s = {10,20,30,20}
print(s)

# Empty set
empty_set = set()

# add()
s.add(40)

# update()
s.update([50,60])

# remove()
s.remove(20)

# discard()
s.discard(100)

# pop()
removed = s.pop()

# copy()
copy_set = s.copy()

# clear()
temp_set = {1,2}
temp_set.clear()

# Set Operations
a = {1,2,3}
b = {3,4,5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))

# Useful Functions for Sets
print(len(s))
print(max(s))
print(min(s))
print(sum(s))
print(sorted(s))
print(any(s))
print(all(s))
print(type(s))

# ==========================================================
# DIFFERENCE BETWEEN DATA TYPES
# ==========================================================

"""
Feature              List            Tuple            Dictionary            Set
--------------------------------------------------------------------------------
Syntax               []              ()               {key:value}           {}
Ordered              Yes             Yes              Yes (Python 3.7+)     No
Mutable              Yes             No               Yes                   Yes
Duplicates           Yes             Yes              Keys No               No
Indexed              Yes             Yes              By Key                No
"""

# ==========================================================
# IMPORTANT BUILT-IN FUNCTIONS
# ==========================================================

"""
len()
sum()
max()
min()
sorted()
any()
all()
type()
"""

# ==========================================================
# GOLDEN RULES
# ==========================================================

"""
1. input() always returns a string.

2. split() always returns a list.

3. append() modifies a list and returns None.

4. sort() modifies a list and returns None.

5. pop() removes and returns an element.

6. remove() removes by value.

7. pop(index) removes by index.

8. Tuples are immutable.
   They only have:
      - count()
      - index()

9. Dictionaries are accessed by KEYS, not VALUES.

10. dict.get(key) returns None if the key doesn't exist.

11. Sets automatically remove duplicate values.

12. set() creates an empty set.
    {} creates an empty dictionary.
"""

print("\nRevision Completed Successfully!")
