import pandas as pd
import numpy as np
# print(pd.__version__)

# Series: A Series is a one-dimensional labeled array in Pandas that stores data along with an index.
# it can also hold any data type. it is similar to column in a table
data = [1,2,3,4,5,6,7,8,9,10]
series = pd.Series(data)
print(series)

# create a series from a dictionary:
data = {'a':1, 'b':2, 'c':3, 'd':4}
dict_series = pd.Series(data)
print(dict_series)


# we can gove different index over here based on our requirement below is the example:
data = [10,20,30]
indx = ['a', 'b', 'c']
series = pd.Series(data, index=indx)
print(series)



# DATA FRAME =======>>
# create a Dataframe from a dictionary oof list:
data = {
    'Name': ['Sidharth', 'Priyanka', 'Garima', 'Raghav'],
    'age': [26, 24, 23, 25],
    'city': ['Banglore', 'Chennai', 'Madras', 'Uttarakhand']
}
df = pd.DataFrame(data)
print(df)
# using numpy see the magic: it will skip the column name and indices:
print(np.array(df))



# Create a Data frame From a List of Dictionaries:
data = [
    {'Name': 'Krishna', 'Age': 26, 'City': 'Bangluru'},
    {'Name': 'Khushi', 'Age': 25, 'City': 'Banarash'},
    {'Name': 'Khusboo', 'Age': 24, 'City': 'Kolkata'},
    {'Name': 'Kashinath', 'Age': 27, 'City': 'Nalanda'},
    {'Name': 'Kamalnath', 'Age': 23, 'City': 'Almora'},
    {'Name': 'Krishika', 'Age': 20, 'City': 'Nainital'},
    {'Name': 'Komal', 'Age': 33, 'City': 'Begusarai'},
    {'Name': 'Kanahaiya', 'Age': 45, 'City': 'Bhagalpur'},
    {'Name': 'Kundan', 'Age': 28, 'City': 'Ramnagar'}
]
df = pd.DataFrame(data)
print(df)




# QUESTION:
# Read data from a csv file:
df = pd.read_csv('Chapter-15-Data-Analysis-with-Python/data.csv')
print(df.head(10))
print(df.tail(10))

# accessing data from DataFrame:
print(df['Date'])
print(df['Category'])

# accessing data from row:
print(df.loc[0]) 

# to get some kinf of operation here:
print(df.iloc[0,2])

# Accessing a Specified Element:
print(df.at[1,'Sales'])
print(df.at[0,'Product'])

# Accessing a Specified element using iat[]:
print(df.iat[2,2])

# data manipulation with data frame: Adding a column here:
df['Rating'] = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
print(df)

# remove a column: for permanent removal use inplace=True
remvd_data = df.drop('Region', axis=1, inplace=True)
print(remvd_data)

# Add rating by 1 to the rating column:
df['Rating'] = df['Rating']+1
print(df)

# Remove element by row: permanently
df.drop(0, inplace=True)
print(df)

# display the data types of each column:
print("Data types:\n", df.dtypes)

# describe the Data frames:
print("Statistical Summary:\n", df.describe())
