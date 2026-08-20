import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('Chapter-20-Exploratory-Data-Analysis/flight_price.xlsx')
print(df.head())
print(df.tail())

# get the basic info about data
print(df.info())
print(df.describe())

# feature ingineering process:
df['Date'] = df['Date_of_Journey'].str.split('/').str[0]
print(df['Date'])

df['Month'] = df['Date_of_Journey'].str.split('/').str[1]
print(df['Month'])

df['Year'] = df['Date_of_Journey'].str.split('/').str[2]
print(df['Year'])

df['Date'] = df['Date'].astype(int)
df['Month'] = df['Month'].astype(int)
df['Year'] = df['Year'].astype(int)


# drop date of journey column:
df.drop('Date_of_Journey', axis=1, inplace=True)

df['Arrival_Time'] = df['Arrival_Time'].apply(lambda x:x.split(' ')[0])
df['Arrival_hour'] = df['Arrival_Time'].str.split(':').str[0]
df['Arrival_minute'] = df['Arrival_Time'].str.split(':').str[1]

df['Arrival_hour'] = df['Arrival_hour'].astype(int)
df['Arrival_minute'] = df['Arrival_minute'].astype(int)
df.drop('Arrival_Time', axis=1, inplace=True)
# print(df.head())


# handle departure time:
df['Dep_hour'] = df['Dep_Time'].str.split(':').str[0]
df['Dep_minute'] = df['Dep_Time'].str.split(':').str[1]

df['Dep_hour'] = df['Dep_hour'].astype(int)
df['Dep_minute'] = df['Dep_minute'].astype(int)
# print(df.head())
print(df.info())
df.drop('Dep_Time', axis=1, inplace=True)
print(df.head())



# handeling total stops from the dataset:
print(df['Total_Stops'].unique())

df['Total_Stops'] = df['Total_Stops'].map({'non-stop':0, '1 stop':1, '2 stop': 2, '3 stop': 3, '4 stop': 4, np.nan:1})
df.drop('Route', axis=1, inplace=True)