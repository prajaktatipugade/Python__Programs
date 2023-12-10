from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[1,4,9,16,25]
plt.bar(x,y)
plt.show()
plt.hist(x)
plt.show()
plt.scatter(x,y)
plt.show()
#pi chart
p=['a','b','c','d','e']
q=[1,4,9,26,25]
plt.pie(q,labels=p)
plt.show()
