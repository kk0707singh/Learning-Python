#          NUMPY IMPORTANT ATTRIBUTES & METHODS
#                (Data Analyst Notes)

import numpy as np

# ==========================================================
# ATTRIBUTES
# ==========================================================

# 1. .shape
"""
Purpose:
Returns the shape (structure) of an array.

Syntax:
array.shape

Return Type:
Tuple

Meaning:
(rows, columns)

Note:
.shape is an ATTRIBUTE.
Do NOT use parentheses.
"""

arr = np.array([[10,20,30],
                [40,50,60]])

print(arr.shape)

# Output
# (2, 3)

# ----------------------------------------------------------
# 2. .ndim
"""
Purpose:
Returns the number of dimensions.

Syntax:
array.ndim

Return Type:
Integer

Meaning:
1 -> One Dimensional Array
2 -> Two Dimensional Array
3 -> Three Dimensional Array
"""

arr = np.array([[10,20],
                [30,40]])

print(arr.ndim)

# Output
# 2

# ----------------------------------------------------------
# 3. .size
"""
Purpose:
Returns total number of elements.

Syntax:
array.size

Return Type:
Integer

Formula:
Rows × Columns
"""

arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.size)

# Output
# 6

# ----------------------------------------------------------
# 4. .dtype
"""
Purpose:
Returns data type of array elements.

Syntax:
array.dtype

Return Type:
dtype object

Possible Types:
int64
float64
bool
str
"""

arr = np.array([10,20,30])

print(arr.dtype)

# Output
# int64

# ----------------------------------------------------------
# 5. .itemsize
"""
Purpose:
Returns memory occupied by ONE element.

Syntax:
array.itemsize

Return Type:
Integer

Unit:
Bytes
"""

arr = np.array([10,20,30])

print(arr.itemsize)

# Output
# 8

# ----------------------------------------------------------
# 6. .nbytes

"""
Purpose:
Returns total memory occupied by the array.

Syntax:
array.nbytes

Return Type:
Integer

Formula:
size × itemsize
"""

arr = np.array([10,20,30])

print(arr.nbytes)

# Output
# 24

# ==========================================================
# METHODS
# ==========================================================

# ----------------------------------------------------------
# 1. reshape()
"""
Purpose:
Changes the shape (layout) of an array.

Syntax:
array.reshape(rows, columns)

Return Type:
ndarray

Rule:
Rows × Columns = Total Elements

Data remains SAME.
Only arrangement changes.
"""

arr = np.array([1,2,3,4,5,6])

print(arr.reshape(2,3))

# Output
# [[1 2 3]
#  [4 5 6]]

# ----------------------------------------------------------
# 2. reshape(-1)
"""
Purpose:
NumPy automatically calculates ONE missing dimension.

Syntax:
array.reshape(2,-1)

OR

array.reshape(-1,2)

Rules:

✔ Only ONE -1 is allowed.

✔ Total elements must remain the same.

❌ reshape(-1,-1)

Raises ValueError.
"""

arr = np.array([1,2,3,4,5,6])

print(arr.reshape(2,-1))

# Output
# [[1 2 3]
#  [4 5 6]]

print(arr.reshape(-1,2))

# Output
# [[1 2]
#  [3 4]
#  [5 6]]

# ----------------------------------------------------------
# 3. sum()
"""
Purpose:
Returns sum of all elements.

Syntax:
array.sum()

Return Type:
Scalar
"""

arr = np.array([10,20,30])

print(arr.sum())

# Output
# 60

# ----------------------------------------------------------
# 4. mean()
"""
Purpose:
Returns average of all elements.

Syntax:
array.mean()

Return Type:
Scalar
"""

arr = np.array([10,20,30])

print(arr.mean())

# Output
# 20.0

# ----------------------------------------------------------
# 5. max()
"""
Purpose:
Returns largest element.

Syntax:
array.max()

Return Type:
Scalar
"""

arr = np.array([10,20,30])

print(arr.max())

# Output
# 30

# ----------------------------------------------------------
# 6. min()
"""
Purpose:
Returns smallest element.

Syntax:
array.min()

Return Type:
Scalar
"""

arr = np.array([10,20,30])

print(arr.min())

# Output
# 10

# ----------------------------------------------------------
# 7. std()
"""
Purpose:
Returns Standard Deviation.

Syntax:
array.std()

Return Type:
Scalar

Used in Statistics and Data Analysis.
"""

arr = np.array([10,20,30])

print(arr.std())



# ----------------------------------------------------------
# 8. var()
"""
Purpose:
Returns Variance.

Syntax:
array.var()

Return Type:
Scalar
"""

arr = np.array([10,20,30])

print(arr.var())

# ----------------------------------------------------------
# 9. flatten()
"""
Purpose:
Converts a multi-dimensional array into a 1D array.

Syntax:
array.flatten()

Return Type:
ndarray
"""

arr = np.array([[1,2],
                [3,4]])

print(arr.flatten())

# Output
# [1 2 3 4]

# ----------------------------------------------------------
# 10. astype()
"""
Purpose:
Changes the data type of an array.

Syntax:
array.astype(datatype)

Return Type:
ndarray

Original array remains unchanged.
"""

arr = np.array([1,2,3])

print(arr.astype(float))

# Output
# [1. 2. 3.]

# ----------------------------------------------------------
# 11. copy()
"""
Purpose:
Creates an independent copy of an array.

Syntax:
array.copy()

Return Type:
ndarray

Changing copied array DOES NOT affect original array.
"""

arr = np.array([1,2,3])

copy_arr = arr.copy()

print(copy_arr)

# Output
# [1 2 3]

# ==========================================================
# ATTRIBUTES SUMMARY
# ==========================================================
"""
+------------+-----------------------------------------+----------------+
| Attribute  | Purpose                                 | Return Type    |
+------------+-----------------------------------------+----------------+
| .shape     | Returns array shape                     | tuple          |
| .ndim      | Returns number of dimensions            | int            |
| .size      | Returns total elements                  | int            |
| .dtype     | Returns data type                       | dtype object   |
| .itemsize  | Returns bytes used by one element       | int            |
| .nbytes    | Returns total memory occupied           | int            |
+------------+-----------------------------------------+----------------+
"""

# ==========================================================
# METHODS SUMMARY
# ==========================================================
"""
+-------------+------------------------------------------+----------------+
| Method      | Purpose                                  | Return Type    |
+-------------+------------------------------------------+----------------+
| reshape()   | Changes array shape                      | ndarray        |
| reshape(-1) | Auto calculates one dimension            | ndarray        |
| sum()       | Returns sum                              | Scalar         |
| mean()      | Returns average                          | Scalar         |
| max()       | Returns largest element                  | Scalar         |
| min()       | Returns smallest element                 | Scalar         |
| std()       | Returns standard deviation               | Scalar         |
| var()       | Returns variance                         | Scalar         |
| flatten()   | Converts array into 1D                   | ndarray        |
| astype()    | Changes data type                        | ndarray        |
| copy()      | Creates independent copy                 | ndarray        |
+-------------+------------------------------------------+----------------+
"""
# ==========================================================
# COMMON MISTAKES
# ==========================================================

"""
❌ Wrong

arr.shape()

✔ Correct

arr.shape

------------------------------------

❌ Wrong

arr.reshape(2,2)

when total elements = 6

✔ Correct

arr.reshape(2,3)

------------------------------------

❌ Wrong

arr.reshape(-1,-1)

✔ Correct

arr.reshape(2,-1)
"""

# ==========================================================
# MEMORY TRICKS
# ==========================================================
"""
shape
→ Structure

ndim
→ Number of Dimensions

size
→ Total Elements

dtype
→ Data Type

itemsize
→ Memory per Element

nbytes
→ Total Memory

reshape()
→ Changes Layout

reshape(-1)
→ NumPy Calculates Missing Dimension

flatten()
→ 2D → 1D

astype()
→ Change Data Type

sum()
→ Total

mean()
→ Average

max()
→ Largest

min()
→ Smallest
"""



# ==========================================================
#                NUMPY ARRAY CREATION METHODS
#                   (Data Analyst Notes)
# ==========================================================

import numpy as np

# ==========================================================
# 1. arange()
# ==========================================================

"""
Purpose:
Creates an array with evenly spaced values.

Syntax:
np.arange(start, stop, step)

Parameters:

start -> Starting value (included)

stop -> Ending value (excluded)

step -> Gap between consecutive values

Return Type:
ndarray

Note:
Works exactly like Python's range().
Difference is that it returns a NumPy array.
"""

arr = np.arange(1, 11)

print(arr)

# Output
# [ 1  2  3  4  5  6  7  8  9 10]


# ----------------------------------------------------------
# Example 2
# ----------------------------------------------------------

arr = np.arange(5)

print(arr)

# Output
# [0 1 2 3 4]


# ----------------------------------------------------------
# Example 3
# ----------------------------------------------------------

arr = np.arange(2, 20, 2)

print(arr)

# Output
# [ 2  4  6  8 10 12 14 16 18]


# ----------------------------------------------------------
# Example 4
# ----------------------------------------------------------

arr = np.arange(10, 0, -2)

print(arr)

# Output
# [10  8  6  4  2]


# ==========================================================
# 2. ones()
# ==========================================================

"""
Purpose:
Creates an array filled with 1s.

Syntax:
np.ones(shape)

Return Type:
ndarray

Default Data Type:
float64
"""

arr = np.ones(5)

print(arr)

# Output
# [1. 1. 1. 1. 1.]


# ----------------------------------------------------------
# Example 2
# ----------------------------------------------------------

arr = np.ones((2,3))

print(arr)

# Output
# [[1. 1. 1.]
#  [1. 1. 1.]]


# ----------------------------------------------------------
# Example 3
# ----------------------------------------------------------

arr = np.ones((3,4), dtype=int)

print(arr)

# Output
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]


# ==========================================================
# arange() vs range()
# ==========================================================

"""
+-----------+----------------------+----------------------+
| Feature   | range()              | np.arange()          |
+-----------+----------------------+----------------------+
| Returns   | range object         | ndarray              |
| Library   | Python               | NumPy                |
| Used For  | Loops                | Numerical Computing  |
+-----------+----------------------+----------------------+
"""


# ==========================================================
# SUMMARY TABLE
# ==========================================================

"""
+-----------+-----------------------------------------+-------------+
| Method    | Purpose                                 | Return Type |
+-----------+-----------------------------------------+-------------+
| arange()  | Creates evenly spaced values            | ndarray     |
| ones()    | Creates an array filled with 1s         | ndarray     |
+-----------+-----------------------------------------+-------------+
"""


# ==========================================================
# DATA ANALYST NOTE
# ==========================================================

"""
np.arange()

✔ Creating index values

✔ Creating sequences

✔ Feature Engineering

✔ Data Simulation


np.ones()

✔ Initializing arrays

✔ Matrix creation

✔ Machine Learning

✔ Placeholder arrays
"""


# ==========================================================
# COMMON MISTAKES
# ==========================================================

"""
❌ Wrong

np.arange(1,10,0)

Reason:
Step cannot be zero.

-----------------------------------

❌ Wrong

np.ones(2,3)

✔ Correct

np.ones((2,3))

Reason:
2D shape must be written as a tuple.

-----------------------------------

❌ Wrong

np.arange(1,5)

Expected

1 2 3 4 5

✔ Actual

[1 2 3 4]

Reason:
Stop value is NOT included.
"""


# ==========================================================
# MEMORY TRICKS
# ==========================================================

"""
arange()

↓

Array + Range

↓

Works like Python range()

↓

Stop value NOT included


----------------------------


ones()

↓

Creates array filled with 1s

↓

Default Data Type = float
"""

# ==========================================================
#                    np.eye() FUNCTION
#                 (Data Analyst Notes)
# ==========================================================

import numpy as np

# ==========================================================
# 1. np.eye()
# ==========================================================

"""
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
"""

arr = np.eye(3)

print(arr)

# Output
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# ==========================================================
# Example 2
# ==========================================================

arr = np.eye(4)

print(arr)

# Output
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]


# ==========================================================
# Example 3
# ==========================================================

arr = np.eye(3,5)

print(arr)

# Output
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]


# ==========================================================
# Example 4
# ==========================================================

arr = np.eye(3, dtype=int)

print(arr)

# Output
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]


# ==========================================================
# SUMMARY TABLE
# ==========================================================

"""
+-----------+-----------------------------------------+-------------+
| Function  | Purpose                                 | Return Type |
+-----------+-----------------------------------------+-------------+
| np.eye()  | Creates an Identity Matrix              | ndarray     |
+-----------+-----------------------------------------+-------------+
"""