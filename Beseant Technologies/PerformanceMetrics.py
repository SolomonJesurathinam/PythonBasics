#Confusion Matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
Accuraccy = TP+TN/(TP+FP+FN+TN)
Precesion = TP/(TP+FP)
Recall/actual positive - TP/(TP+FN)
F1 sccore = 2/((1/Precesion)+(1/Recall))      --> (2*Recall*Precesion)/(Recall + Precesion)
Specificity (True Negative) = TN/(TN+FP)
'''

data_csv = pd.read_csv("Files/data.csv")
print(data_csv.shape)

x = data_csv.iloc[:,2:6]
y = data_csv.iloc[:,1]

x_train = x[200:400]
y_train = y[200:400]

fig = plt.figure(figsize=(15, 8))#Overall size of graph
plt.subplot(1, 1, 1) #Numer of rows and number of columns and index positions\
sns.distplot(y_train) #plots the distribution of the data
#plt.plot(x_train,y_train)
plt.show()