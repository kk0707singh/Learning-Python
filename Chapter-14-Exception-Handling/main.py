# a = b
# output:- NameError: name 'b' is not defined
# how to handle the exception for the above using try, block:
try:
    a = b
except:
    print("the variable has not been assigned yet!")


# other ways to handle the exception:
try: 
    a = b
except NameError as ne:
    print(ne)


# other example to handle the exception:
try:
    result = 1/0
except ZeroDivisionError as zde:
    print(zde)
    print('Please enter the denominator greator than ZERO!')


# how to handle any exception when we dont know the error class:
try:
    result = 1/2
    a = b
except ZeroDivisionError as zde:
    print(zde)
except Exception as ex:
    print(ex)


# example:
try:
    num = int(input("Enter the no: "))
    result = 100/num
    print(result)
except NameError as ne1:
    print(ne1)
    print("Enter a valid no! ")
except ValueError as ve:
    print(ve)
    print('not a valid no! ')
except ZeroDivisionError as zde1:
    print(zde1)
    print('enter the no greater than ZERO! ')
except Exception as ex1:
    print(ex1)


# try, except, else and finally:
try:
    num = int(input("Enter the no: "))
    result = 100/num
except ValueError as ve:
    print(ve)
    print('not a valid no! ')
except ZeroDivisionError as zde1:
    print(zde1)
    print('enter the no greater than ZERO! ')
except Exception as ex1:
    print(ex1)
else:
    print(f'result is {result}')
finally:
    print("Execution completed")
