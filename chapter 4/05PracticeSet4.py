# practice set: 4
# QUESTION1: Program to store seven values in a empty SET rollno entered by user
l = []
l.append(input("enter your first choice: "))
l.append(input("Enter your second choice: "))
l.append(input("Enter your third choice: "))
l.append(input("enter your fourth choice: "))
l.append(input("enter your fifth choice: "))
l.append(input("enter your sixth chice: "))

print(l)

# shorter way to do this
fruits = input("enter fruits items seperated by commas: ")
# print(tuple(fruits.split(",")))      this will return a tuple
print(fruits.split(","))               #this will return a rollno

# QUESTION2: program to accept marks of six student and sort them
rollno = []
m1 = int(input("enter your marks here: "))
rollno.append(m1)

m2 = int(input("enter your marks here: "))
rollno.append(m2)

m3 = int(input("enter your marks here: "))
rollno.append(m3)

m4 = int(input("enter your marks here: "))
rollno.append(m4)

m5 = int(input("enter your marks here: "))
rollno.append(m5)

m6 = int(input("enter your marks here: "))
rollno.append(m6)

m7 = int(input("enter your marks here: "))
rollno.append(m7)

rollno.sort()

print(rollno)


# Same as above example
list = []
list.append(int(input("Enter mark1: ")))
list.append(int(input("Enter mark2: "))) 
list.append(int(input("Enter mark3: "))) 
list.append(int(input("Enter mark4: "))) 
list.sort() 
print(list)


# QUESTION3: check that tuple type canot be changed
a = ("Sidharth", 34, 45, "rohan")
# a[2] = "krishna" this is not accepted in tuple does not support item assignment

# QUESTION4: A program to sum all the no present in a string
newlist = []
newlist.append(int(input("Enter mark1: ")))
newlist.append(int(input("Enter mark2: "))) 
newlist.append(int(input("Enter mark3: "))) 
newlist.append(int(input("Enter mark4: "))) 
print(sum(newlist))

# QUESTION5: Program to count no. of "0" in a tuple
a = (3, 0, 0, 8, 9, 0, 7, 1, 0, 3, 0)
print(a.count(0))

'''
Function     List     Tuple
 sum()        ✅        ✅ 
 len()        ✅        ✅ 
 max()        ✅        ✅ 
 min()        ✅        ✅ 
 sorted()     ✅        ✅ 
 any()        ✅        ✅ 
 all()        ✅        ✅ 

Example:
l = [5, 2, 8]
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
print(sorted(l))


t = (5, 2, 8)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))

Easy rule to remember:
Functions like sum(), len(), max(), min() 
usually work on both lists and tuples.

Methods that modify data (append(), sort(), remove(), pop(), etc.) 
exist only for lists because tuples cannot be changed.


A useful way to think about it:
Is this function just reading the data? (e.g., sum, len, max)
→ It will often work on both lists and tuples.

Is this method trying to change the data? (e.g., append, sort, remove) 
→ It works on lists, but not on tuples.

'''