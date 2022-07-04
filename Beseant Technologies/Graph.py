import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x = np.array([1,2,3,4,5,6,7,8,9,10])
y = np.array([1,2,3,5,8,13,21,34,55,89])
x2 = np.array([2,4,6,8,9,10])
y2 = np.array([4,6,8,10,12,14])
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
#plot
plt.plot(x,y)
#plt.show()
plt.plot(x,y,marker='o')
#plt.show()
plt.plot(x,y,marker='h')
#plt.show()
plt.plot(x,y,linestyle='--',color = 'r')
#plt.show()
plt.plot(x,y,linewidth='10')
#plt.show()
plt.plot(x,y,x2,y2)
#plt.show()

plt.plot(x,y,color='r')
plt.plot(x2,y2,color='b')
#plt.show()

#labels, Title
plt.plot(x2,y2,color='b')
plt.xlabel("Average Pulse",fontdict=font1)
plt.ylabel("Calorie Burnage",fontdict=font2)
plt.title("Testing",loc='left')
plt.show()

#sns.distplot(x)
#plt.show()

