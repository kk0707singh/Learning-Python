import numpy as np
# create array usinh numpy
# create a 1D array

arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))
print(arr.shape)

try:
    arr = np.array([1,2,3,4,5,6])
    print(arr.reshape(2,2))
except Exception as ex:
    print(ex)



arr = np.array([10,20,30,40,50,60,70,80,90,100,110,120])

new_arr = arr.reshape(3,4)

print(new_arr)
print(new_arr.shape)



# other ways np.arange:
print(np.arange(0,10,2).reshape(5,1))

# np.ones: 
print(np.ones((3,4)))

# identity matrix:
'''
Purpose:
Creates an Identity Matrix.

Syntax:
np.eye(rows)

OR

np.eye(rows, columns)

Return Type:
ndarray

Definition:
An Identity Matrix is a square matrix in which

✔ Main diagonal elements = 1
✔ All other elements = 0
'''
print(np.eye(3))


# questions attributes of NumPy
arr = np.array([[1,2,3], [4,5,6]])
print('array:\n', arr)                          #simply prints the array 2D
print('shape:', arr.shape)                      #output: (2, 3)
print('no. of Dimensions:', arr.ndim)           #output: 2
print('Size(no. of elements):', arr.size)        #output: 6
print('Data type:', arr.dtype)                  #output: int64 (may vary based on platform)
print('itemsize in bytes:', arr.itemsize)       #output: 8 (may vary based on platform)



# NumPy vectorize operations: return type will be an array
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])
# Element wise addition:
print('Addition is:', arr1+arr2)
# element wise substraction:
print('substraction is:', arr1-arr2)
# element wise multiplication:
print('multiplication is:', arr1*arr2)
# element wise division:
print('divion is:', arr1/arr2, type(arr1/arr2))


# NumPy universal function:
arr = np.array([2,3,4,5,6])
# Square Root:
print(np.sqrt(arr))
# Exponential:
print(np.exp(arr))
# sin:
print(np.sin(arr))
# natural log:
print(np.log(arr))



# array slicing and indexing:
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print('Array is: \n', arr)
print(arr[1][3])
print(arr[1,3])
# arr[0][0] means: we can write both print(arr[1][3]) and print(arr[1,3])
# the first[1]: indicates rows and second[3]: indicates columns index element

# lets say i want [7,8] and [11,12] only:
print(arr[1:,2:])
# lets say i want [2,3,4] and [6,7,8]
# print(arr[0:2, 1:])



# some more practice questions:
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr[:,1])
print(arr[:2,1:])
print(arr[:2][1:])

# modify array elements:
arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
arr[0,0] = 100
print(arr)


# stastical concepts--normalisation:
# to have a mean of 0 and standard deviation of 1:
data = np.array([1,2,3,4,5])
# calculate mean and std deviation:
mean = np.mean(data)
print(f'mean is: {mean}')
std_dev = np.std(data)
print(f'Standard dev. is: {std_dev}')
# normalisation of data:
normalise_data = (data-mean)/std_dev
print(normalise_data)



# how to calculate mean, median, standard deviation and variance:
data = np.array([1,2,3,4,5,6,7,8,9,10])
# mean:
mean = np.mean(data)
print(f'mean is: {mean}')

# median:
median = np.median(data)
print(f'median is: {median}')

# standard deviation:
st_dev = np.std(data)
print(f'Standard deviation is: {st_dev}')

# variance:
variance = np.var(data)
print(f'variance is: {variance}')



# logical operation:
data = np.array([1,2,3,4,5,6,7,8,9,10])
print(data>5)            # Output==> [False False False False False  True  True  True  True  True]
print(data[data>5])      # Output==> [ 6  7  8  9 10]
new_data = data[(data>=5) & (data<=10)]
print(new_data)



# question that includes all the function modules and attributes
# Students ke marks ka 2D NumPy array bana rahe hain
marks = np.array([[78,85,72,80],[45,55,60,50],[90,88,95,92],[65,70,68,75],[82,78,85,88]])

# Array ko print kar rahe hain
print("Marks:\n", marks)

# Array ki rows aur columns ki shape check kar rahe hain
print("Shape:", marks.shape)

# Array ke dimensions check kar rahe hain
print("Dimensions:", marks.ndim)

# Array me total elements check kar rahe hain
print("Total elements:", marks.size)

# Array ke elements ka data type check kar rahe hain
print("Data type:", marks.dtype)

# First student ke Python marks access kar rahe hain
print("First student's Python marks:", marks[0,0])

# Sabhi students ke Python marks select kar rahe hain
python_marks = marks[:,0]

# Python ke marks print kar rahe hain
print("Python marks:", python_marks)

# Har student's Python marks me 5 add kar rahe hain using vectorized operation
updated_marks = python_marks + 5

# Updated marks print kar rahe hain
print("Updated Python marks:", updated_marks)

# Python marks ka average calculate kar rahe hain
average = np.mean(python_marks)

# Average print kar rahe hain
print("Average:", average)

# Python marks ka median calculate kar rahe hain
median = np.median(python_marks)

# Median print kar rahe hain
print("Median:", median)

# Python marks ka standard deviation calculate kar rahe hain
std = np.std(python_marks)

# Standard deviation print kar rahe hain
print("Standard deviation:", std)

# Python marks ka variance calculate kar rahe hain
variance = np.var(python_marks)

# Variance print kar rahe hain
print("Variance:", variance)

# 70 se greater marks ko filter karne ke liye Boolean condition bana rahe hain
high_marks = python_marks > 70

# Boolean condition print kar rahe hain
print("Condition:", high_marks)

# Boolean indexing se 70 se greater marks select kar rahe hain
filtered_marks = python_marks[python_marks > 70]

# Filtered marks print kar rahe hain
print("Marks greater than 70:", filtered_marks)

# 70 se greater/equal AND 90 se less/equal marks filter kar rahe hain
selected_marks = python_marks[(python_marks >= 70) & (python_marks <= 90)]

# Selected marks print kar rahe hain
print("Marks between 70 and 90:", selected_marks)

# Python marks ko 5 rows aur 1 column me reshape kar rahe hain
reshaped_marks = python_marks.reshape(5,1)

# Reshaped array print kar rahe hain
print("Reshaped marks:\n", reshaped_marks)

# Marks ka mean calculate karke normalization ke liye use kar rahe hain
mean = np.mean(python_marks)

# Marks ka standard deviation calculate karke normalization ke liye use kar rahe hain
std = np.std(python_marks)

# Formula use karke marks ko normalize kar rahe hain
normalized_marks = (python_marks - mean) / std

# Normalized marks print kar rahe hain
print("Normalized marks:", normalized_marks)

# Har Python mark ka square root calculate kar rahe hain using NumPy universal function
sqrt_marks = np.sqrt(python_marks)

# Square root values print kar rahe hain
print("Square root:", sqrt_marks)

# 1 se 5 tak student numbers ka NumPy array bana rahe hain
student_numbers = np.arange(1,6)

# Student numbers print kar rahe hain
print("Student numbers:", student_numbers)

# Sabhi students ke marks me 5 add karke vectorized operation perform kar rahe hain
bonus_marks = marks + 5

# Bonus marks wala complete array print kar rahe hain
print("Marks after bonus:\n", bonus_marks)