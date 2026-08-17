import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = sns.load_dataset('titanic')
# print(data)
# print(data.head(10))


# check missing values:
print(data.isnull().sum())
print(data.shape)

# delete the missing value from column:
print(data.dropna(axis=1).shape)


# imputation missing values:
# 1. mean value imputation:
# sns.displot(data['age'])
# plt.show()

# sns.histplot(data['age'], kde=True)
# plt.show()

data['age_mean'] = data['age'].fillna(data['age'].mean())
print(data[['age_mean', 'age']])
# mean imputation works well when we have normally distributed data



# 2. median value imputation:
# if we have outliers in data set
data['age_median'] = data['age'].fillna(data['age'].median())
print(data[['age_median', 'age']])


# 3. mode imputation: categorical value


