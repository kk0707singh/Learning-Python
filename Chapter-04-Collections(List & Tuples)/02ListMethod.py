data = ["krishna", "ontario", "tokyo", 8, 8.9]
data.append("Sidharth")
print(data)

anotherlist = [81, 14, 5, 3, 7, 2, 41, 9, 10]
anotherlist.reverse()
print(anotherlist)
anotherlist.sort()
print(anotherlist)
print(anotherlist.pop(7))
anotherlist.remove(9)

anotherlist.extend([99,88,44,45])
print(anotherlist)

'''

Method	                 What it does	                                       Example

append(x)	             Adds one item at the end	                           l.append("Krishna")
extend(iterable)	     Adds multiple items	                               l.extend([4, 5, 6])
insert(index, item)	     Inserts an item at a specific index	               l.insert(1, "Rahul")
remove(value)	         Removes the first matching value	                   l.remove("Rahul")
pop()	                 Removes and returns the last item	                   l.pop()
pop(index)	             Removes and returns the item at the given index	   l.pop(2)
clear()	                 Removes all items	                                   l.clear()
index(value)	         Returns the index of the first matching value	       l.index("Krishna")
count(value)	         Counts how many times a value appears	               l.count(10)
sort()	                 Sorts the list in ascending order	                   l.sort()
sort(reverse=True)	     Sorts the list in descending order	                   l.sort(reverse=True)
reverse()	             Reverses the order of the list	                       l.reverse()
copy()	                 Creates a shallow copy of the list	                   new_list = l.copy()

'''