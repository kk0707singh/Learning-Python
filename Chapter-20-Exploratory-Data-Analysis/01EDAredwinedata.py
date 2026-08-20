import pandas as pd
df = pd.read_csv('Chapter-20-Exploratory-Data-Analysis/winequality-red.csv', sep=';')
print(df.head())
print(df.info())      #summary of the dataset

print(df.describe())    #description of dataset

print(df.shape)
print(df.columns)

# want to see the unique values in column:
print(df['quality'].unique())

# check for missing values:
print(df.isnull().sum())

# duplicate record:

print(df[df.duplicated()])

# removing the duplicates:
df.drop_duplicates(inplace=True)
print(df.shape)

# correlation
print(df.corr())

import seaborn as sns
import matplotlib.pyplot as plt
# sns.heatmap(df.corr())
# plt.show()

# visualisation:
df.quality.value_counts().plot(kind='bar')
# plt.show()


# for column in df.columns:
#     sns.histplot(df[column], kde=True)
# plt.show()

# sns.histplot(df['alcohol'])
# plt.show()

# sns.pairplot(df)
# plt.show()

sns.catplot(x='quality', y='alcohol', data=df, kind='box')
plt.show()