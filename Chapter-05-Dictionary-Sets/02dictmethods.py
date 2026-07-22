# marks = {
#     "Sidharth": 100,
#     "Archit": 54,
#     "Raghav": 78
# }

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Archit": 73})
# print(marks)
# marks.update({"Pinki": 92})
# print(marks)
# # print(marks["Sidharth1"])        returns key error 
# print(marks.get("Sidharth1"))      #returns none 
# print(marks.get("city", "delhi"))

# print(marks.pop("Archit"))


# ========================= DICTIONARY METHODS =========================

student = {
    "name": "Krishna",
    "age": 26,
    "city": "Delhi",
    "course": "MCA"
}

# get(key) -> Returns the value of the key. If the key doesn't exist, it returns None (or a default value if provided).
print(student.get("name"))            # Krishna
print(student.get("salary"))          # None
print(student.get("salary", 25000))   # 25000

# keys() -> Returns all the keys in the dictionary.
print(student.keys())                 # dict_keys(['name', 'age', 'city', 'course'])

# values() -> Returns all the values in the dictionary.
print(student.values())               # dict_values(['Krishna', 26, 'Delhi', 'MCA'])

# items() -> Returns all key-value pairs as tuples.
print(student.items())                # dict_items([('name', 'Krishna'), ('age', 26), ...])

# update() -> Adds a new key-value pair or updates an existing key.
student.update({"age": 27, "salary": 25000})
print(student)

# pop(key) -> Removes the specified key and returns its value.
print(student.pop("city"))            # Delhi
print(student)

# popitem() -> Removes and returns the last inserted key-value pair.
print(student.popitem())              # ('salary', 25000)
print(student)

# copy() -> Creates a shallow copy of the dictionary.
new_student = student.copy()
print(new_student)

# setdefault(key, default) -> Returns the value if the key exists; otherwise adds the key with the default value.
student.setdefault("country", "India")
student.setdefault("age", 30)         # Won't change because 'age' already exists
print(student)

# clear() -> Removes all key-value pairs from the dictionary.
student.clear()
print(student)                        # {}

'''
get() → Safely get a value.
keys() → Get all keys.
values() → Get all values.
items() → Get all (key, value) pairs.
update() → Add or update key-value pairs.
pop() → Remove a specific key and return its value.
popitem() → Remove the last inserted key-value pair.
copy() → Create a copy of the dictionary.
setdefault() → Add a key only if it doesn't already exist.
clear() → Remove everything from the dictionary.
'''