import matplotlib.pyplot as plt
# x = [1,2,9,4,5]
# y = [2,7,5,9,10]

# # i want to create a line plot
# plt.plot(x,y)
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.title("Basic Line Plot")
# plt.show()


# create a customised line plot:
# x =[1,12,3,43,23,56]
# y =[4,9,4,6,23,56]
# plt.plot(x,y, color='red', linestyle='dashdot', marker='o', linewidth=3, markersize='9') 
# plt.grid(True)
# plt.show()


# sample data:
# x = [1,2,3,4,5]
# y1 = [1,4,9,16,25]
# y2 = [1,2,3,4,5]

# plt.figure(figsize=(9,6))

# plt.subplot(2,2,1)
# plt.plot(x,y1, color='green')
# plt.title('Plot1')

# plt.subplot(2,2,2)
# plt.plot(x,y2, color='green')
# plt.title('Plot2')

# plt.subplot(2,2,3)
# plt.plot(y1,x, color='green')
# plt.title('Plot3')

# plt.subplot(2,2,4)
# plt.plot(y2,y1, color='green')
# plt.title('Plot4')

# plt.show()





# bar plot: plotting by categories:<=========
# category = ['A', 'B', 'C', 'D', 'E']
# values = [7,8,3,5,9]

# # create a bar plot:
# plt.bar(category, values, color='red')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Plot')
# plt.show()





# ==================>Histogram<=====================
'''
histogram are used to represent the distribution of a dataset. 
they divide the data into bins and count the nos of data point in each bean
'''
# data = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
# # create a histogram:
# plt.hist(data, bins=5, color='red', edgecolor='black')
# plt.show()


# =================>Scatter plot<====================
# create a scatter plot:
# sample data:
# x = [1,2,3,4,5]
# y = [2,3,4,5,6]

# plt.scatter(x,y, color='red', marker='+')
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('scatter Plot')
# plt.show()




# ======================>pie chart<===================
category = ['A', 'B', 'C', 'D', 'E']
values = [17,38,53,25,39]
colors = ['red','green','blue','yellow','gray']
explode = (0.2,0,0,0,0)     #move out the first slice

plt.pie(values, labels=category, colors=colors, autopct='%1.1f%%', explode=explode)
plt.show()




# sales data visualisation: real example for all the things we have studied so far:
