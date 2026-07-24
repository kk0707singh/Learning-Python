# Practice Set: 8
# QUESTION1: program using functions to find greatest of 4 nos:
def maximum(a, b, c, d):
    greatest = max(a, b, c, d)
    return greatest

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
d = int(input("Enter number d: "))
print(f"greatest among a, b, c, d is: {maximum(a, b, c, d)}")


# another way to solve the above problem
w = int(input("Enter number w: "))
x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
z = int(input("Enter number z: "))

def greatest(w, x, y, z):
    if(w>x and w>y and w>z):
        print("W is greatest among all:")
        return w
    elif(x>w and x>y and x>z):
        print("X is greatest among all:")
        return x
    elif(y>w and y>x and y>z):
        print("Y is greatest among all:")
        return y
    elif(z>w and z>x and z>y):
        print("Z is greatest among all:")
        return z
print("greatest among all is: ", greatest(w, x, y, z))


# QUESTION2: program using function to convert Celsius to Fahrenheit.
def conversion(celsius):
    fahrenheit = (celsius*1.8)+32
    return fahrenheit
celsius = float(input("Enter the temperature to convert in fahrenheit: "))
print("conversion is:", conversion(celsius))


# # QUESTION3: How do you prevent a python print() function to print a new line at the end:
print("a")
print("b")
print("C", end=" ")         #we can use end = "" to prevent the new line in python
print("D")



# QUESTION4: Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_first_natural_no(n):
    count = 0
    for i in range(1, n+1):
        count = count+i
    return count

n = int(input("Enter the no: "))
print(f"the sum of n natural no is: {sum_of_first_natural_no(n)}")



# another way to solve the same question:
def sum(n):
    if(n == 1):
        return 1
    return sum(n-1)+n
print(sum(4)) 



'''
QUESTION5: Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*
'''
def patterns(n):
    if n == 0:
        return
    print("*"*n)
    patterns(n-1)
patterns(5)


# QUESTION: find the average using function
def cal_avg(a, b, c):
    avg = (a+b+c)/3
    return avg
a = float(input("Enter no A: "))
b = float(input("Enter no B: "))
c = float(input("Enter no C: "))
print("Average of 3 nos are: ",cal_avg(a, b, c))



# QUESTION: function to find the length of a list using user input:
def len_func(item):
    return len(item)
    # print(len(item))

cities = []
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))
cities.append(input("Enter the cities of your choices:"))

super_heros = []
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))
super_heros.append(input("Enter the super heros of your choices:"))

# a = len_func(cities)
# print(a)
# b = len_func(super_heros)
# print(b)
print(f"length of the city list is: {len_func(cities)}")
print(f"length of the super hero list is: {len_func(super_heros)}")




#  program to print the list using function
def len_func(item):
    for i in item:
        print(i, end=" ")

cities = []
for city in range(8):
    cities.append(input("Enter the city you belong: "))

super_heros = []
for super_hero in range(8):
    super_heros.append(input("enter your Fav Super hero: "))

len_func(cities)
print()
len_func(super_heros)
print()
print("length is: ", len(cities))
print("length is: ", len(super_heros))




# program to convert usd to INR using function and user input
def usd_to_inr_convertor(usd_value):
    inr_value = usd_value*89
    print(f"{usd_value}USD = {inr_value}INR" )
usd_value = float(input("Enter USDT to covert into INR: "))
usd_to_inr_convertor(usd_value)




# program which takes input from user and check for odd and even and returns value as a string odd for odd and even for even
def odd_even_checker(num):
    if(num%2==0):
        return "Even"
    else:
        return "Odd"
num = int(input("Enter the no to check ODD or EVEN: "))
print(odd_even_checker(num))




# QUESTION: a program to convert inches into cms
def inches_cms_converter(inches):
    cms = inches*2.54
    return cms
inches = float(input("Enter the meseurment in inches only: "))
print(inches_cms_converter(inches))



# QUESTION: Write a python function to remove a given word from a list ad strip it at the sametime.
def rem(lst, word):
    n = []
    for i in lst:
        if i != word:
            n.append(i.strip(word))
    return n
l = ["harry", "rohan", "mohan", "an", "sohan"]
print(rem(l, "an"))


# QUESTION: Write a python function to print multiplication table of a given number.
def mult_table(num):
    for item in range(1, 11):
        print(f"multiplication table of num is: {num} x {item} = {num*item}")
num = int(input("Enter the num you want the multiplication of: "))
print(mult_table(num))