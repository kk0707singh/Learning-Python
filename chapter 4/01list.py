data = ["krishna", "sidharth", 98, 7, True, "Archit", "Raghav"]
print(data)
data[4] = False
print(data)

# list slicing 
print(data[0:4])

# how to add items in a empty list using append and insert function
l = []
l.insert(1, "rahaul")
l.insert(0, "sidharth")
l.append("drishti")
print(l)


# taking user input to add items in a empty list
userInputList = []
item1 = input("Enter First item: ")
userInputList.append(item1)

item2 = input("Enter secon item: ")
userInputList.append(item2)

item3 = input("Enter third input: ")
userInputList.append(item3)

print(userInputList)


# shorter way to solve this problem
shorterinput = []
shorterinput.append(input("enter first choice: "))
shorterinput.append(input("enter second choice: "))
shorterinput.append(input("enter third choice: "))
shorterinput.append(input("enter fourth choice: "))
shorterinput.append(input("enter fifth choice: "))
shorterinput.append(input("enter sixth choice: "))
print(shorterinput)

# more shorter way to solve the same problem
emptylist = input("Enter the items seperated by commas: ")
print(emptylist.split(","))