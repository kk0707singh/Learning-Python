# notes = "hey how are you"
# f = open("Chapter-09-File-Input-output/file.txt", "w")
# data = f.write(notes)
# print(data)
# f.close()


f = open("Chapter-09-File-Input-output/file.txt","r")
# # lines = f.readlines()
# # print(lines, type(lines))

# l1 = f.readline()
# print(l1, type(l1))

# l2 = f.readline()
# print(l2, type(l2))

# l3 = f.readline()
# print(l3, type(l3))

# l4 = f.readline()
# print(l4, type(l4))

# l5 = f.readline()
# print(l5, type(l5))
# f.close() 


count = 1
for line in f:
    print(f"line {count}: {line}", end="")
    count = count+1
    print(count)