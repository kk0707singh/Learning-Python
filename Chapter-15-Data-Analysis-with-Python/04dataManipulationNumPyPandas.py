import pandas as pd
df = pd.read_csv('Chapter-15-Data-Analysis-with-Python/data.csv')
# printing first five rows:
print(df.head(5))
# printing the last rows:
print(df.tail(5))
# print stqatistical things:
print(df.describe())
# printing data types:
print(df.dtypes)
# handeling misssing values:
print(df.isnull().any(axis=1))
print(df.isnull().sum())             # this will tell the total no of missing value
# to fill the missing values with default value:
# print(df.fillna(0)) 
# filling missing values with the mean of the column:
df['Sales_fillNA'] = df['Sales'].fillna(df['Sales'].mean())
print(df)
# Renaming columns:
df = df.rename(columns={'Date': 'Deadline'})      #we have to give in key and value pairs
print(df.head(5))
# change data types:
df['New_Value'] = df['Value'].fillna(df['Value'].mean()).astype(int)
print(df.head(5))
# apply function to a column:
df['incrsd_val'] = df['New_Value'].apply(lambda x: x*2)
print(df.head(5))


# merging and joining: on the key columns
df1 = pd.DataFrame({'Key': ['a', 'b', 'c'], 'Value1':[1,2,3]})
df2 = pd.DataFrame({'Key': ['a', 'b', 'd'], 'Value2':[4,5,6]}) 

# Keep only common keys from df1 and df2
df3 = pd.merge(df1, df2, on='Key', how='inner')
print(df3)

# Keep all keys from both df1 and df2
df4 = pd.merge(df1, df2, on='Key', how='outer')
print(df4)

# Keep all keys from df1 and matching keys from df2
df5 = pd.merge(df1, df2, on='Key', how='left')
print(df5)

# Keep all keys from df2 and matching keys from df1
df6 = pd.merge(df1, df2, on='Key', how='right')
print(df6)