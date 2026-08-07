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
# the first[0]: indicates rows and second[3]: indicates columns index element

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

