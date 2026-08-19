'''
Five-Number Summary and Box-plot
minimun, maximum, median, q1, q3, iqr
'''
import numpy as np
lst_marks = [45,32,56,75,89,54,32,89,90,87,67,54,45,98,99,67,74]
minimum,Q1,median,Q3,maximum = np.quantile(lst_marks,[0, 0.25, 0.50,0.75,1.0])
print(minimum)
print(Q1)
print(median)
print(Q3)
print(maximum)

IQR = Q3-Q1
print(IQR)

lower_fence = Q1-1.5*(IQR)
higher_fence = Q3+1.5*(IQR)
print(lower_fence)
print(higher_fence)

import seaborn as sns
import matplotlib.pyplot as plt
# sns.boxplot(lst_marks)
# plt.show()

lst_marks = [-100,-200,45,32,56,75,89,54,32,89,90,87,67,54,45,98,99,67,74,150,170,180]
sns.boxplot(lst_marks)
plt.show()

