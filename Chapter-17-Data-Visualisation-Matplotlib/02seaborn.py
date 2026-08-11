import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# basic plotting with seaborn:
data_set = sns.load_dataset('tips')
print(data_set)

# # create a scatter plot:
# sns.scatterplot(x='total_bill', y='tip', data=data_set)
# plt.title("seaborn scatterplot")
# plt.show()

# # line plot:
# sns.lineplot(x='size', y='total_bill', data=data_set)
# plt.title("lineplot of total bill size")
# plt.show()


# # categorical plot:
# # 1.barplot:
# sns.barplot(x='day', y='total_bill', data=data_set)
# plt.title("bar plot of total_bill with respect to day")
# plt.show()

# # box plot:
# sns.boxplot(x='day', y='total_bill', data=data_set)
# plt.title("box plot of total_bill with respect to day")
# plt.show()


# # violin plot:
# sns.violinplot(x='day', y='total_bill', data=data_set)
# plt.title("violin plot of total_bill with respect to day")
# plt.show()


# # histogram:
# sns.histplot(data_set['total_bill'], bins=10, kde=True)
# plt.show()

# # kde plot:
# sns.kdeplot(data_set['total_bill'], fill=True)
# plt.show()

# # pairplot:
# sns.pairplot(data_set)
# plt.show()


# # Heatmap:
# corr = data_set[['total_bill', 'tip', 'size']].corr()
# print(corr)
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.show()


# sales_df = pd.read_csv('Chapter-17-Data-Visualisation-Matplotlib/seaborn_dataset.csv')
# print(sales_df.head(5))
# # plot total sales by product
# plt.figure(figsize=(10,6))
# sns.barplot(x='Product_Category', y='Total_Revenue', data=sales_df, estimator=sum)
# plt.title("TOtal Sales by Product")
# plt.xlabel('Product')
# plt.ylabel('total sales')
# plt.show()


sales_df = pd.read_csv('Chapter-17-Data-Visualisation-Matplotlib/seaborn_dataset.csv')
print(sales_df.head(5))
# plot total sales by Region
plt.figure(figsize=(10,6))
sns.barplot(x='Region', y='Total_Revenue', data=sales_df, estimator=sum)
plt.title("TOtal Sales by Product")
plt.xlabel('Region')
plt.ylabel('total sales')
plt.show()