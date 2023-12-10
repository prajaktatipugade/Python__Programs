from matplotlib import pyplot as plt
names=['Rohan','Rohit','Ritrsh']
marks=[80,40,50]
plt.subplot(1,3,1)
plt.subplot(131)
plt.bar(names,marks)
plt.subplot(1,3,2)
plt.scatter(names,marks)
plt.subplot(133)
plt.plot(names,marks)
plt.suptitle("subplot graph")
plt.show()
