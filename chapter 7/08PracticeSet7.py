# QUESTION1: Write a program to print multiplication table of a given number using for loop.
# number = int(input("Enter any no of your choice: "))
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")



# QUWSTION2: Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     if(i.startswith("S")):
#         print("Hello, good morning", i)


# QUESTION3: Attempt problem 1 using while loop.
# n = int(input("Enter any no: "))
# i = 1
# while(i<11):
#     print(f"{n} x {i} = {n*i}")
#     i = i+1


# QUESTION4: Write a program to find whether a given number is prime or not.
# num = int(input("Enter the no: "))
# for i in range(2, num):
#     if(num%i == 0):
#         print("not a prime no: ")
#         break
# else:
#     print("no is prime")



# QUESTION5: Write a program to find the sum of first n natural numbers using while loop.
# num = int(input("Enter the no: "))
# result = 0
# for i in range(1, num+1):
#     result = result+i
# print(result)


# another way to solve the following question
# num = int(input("Enter the no: "))
# i = 1
# result = 0
# while(i<=num):
#     result = result+i
#     i = i+1
# print("total is", result)



# QUESTION6: Write a program to calculate the factorial of a given number using for loop.
# num = int(input("Enter the no: "))
# result = 1
# for i in range(1, num+1):
#     result = result*i
# print("factorial is: ", result)


'''
Write a program to print the following star pattern.
  *
 ***
***** for n = 3
'''
# sidha pyramid
# num = int(input("Enter the no of rows: "))
# for i in range(1, num+1):
#     print(" "*(num-i), end="")
#     print("*"*(2*i-1))


'''
*****
 ***
  *
'''
# # ulta pyramid
# num = int(input("Enter the no of rows: "))
# for i in range(0, num):
#     print(" "*i, end="")
#     print("*"*((2*num-1)-2*i))



'''
DIAMOND PYRAMID: Enter the no of rows: 5
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
# num = int(input("Enter the no of rows: "))
# for j in range(1, num+1):
#     print(" "*(num-j), end="")
#     print("*"*(2*j-1))
# for i in range(1, num):
#     print(" "*i, end="")
#     print("*"*((2*num-1)-2*i))




'''
pyramid using nested loop:
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''
# num = int(input("Enter the no of rows:"))
# for i in range(1, num+1):
#     for j in range(0, num-i):
#         print(" ", end=" ")
#     for k in range(0, 2*i-1):
#         print("*", end=" ")
#     print()



'''
QUESTION: ulta pyramid using nested loop:
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''
# num = int(input("Enter the no of rows:"))
# for i in range(1, num+1):
#     for j in range(1, i):
#         print(" ", end=" ") 
#     for k in range(0, num*2-(2*i-1)):
#         print("*", end=" ")
#     print()



'''
QUESTION: printing patterns using nested loop
* 
* * 
* * * 
* * * * 
* * * * * 
'''
# num = int(input("Enter the no of rows: "))
# for i in range(1, num+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



'''
QUESTION: printing patterns using nested loop:
        *
      * *
    * * *
  * * * *
* * * * *
'''
# num = int(input("Enter the no. of rows: "))
# for i in range(1, num+1):
#     for j in range(0, num-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()



'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''
# num = int(input("Enter the no of rows: "))
# for i in range(1, num+1):
#     for j in range(0, num-i):
#         print(" ", end=" ")
#     for k in range(2*i-1):
#         print("*", end=" ")
#     print()
# for i in range(1, num):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(0, (num*2-(2*i-1))-2):
#         print("*", end=" ")
#     print()



'''
QUESTION: For printing these pattern question
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
# num = int(input("Enter the no of rows: "))
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()



'''
QUESTION: For printing these pattern question:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
# num = int(input("Enter the no of rows: "))
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()
