from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

def distributionPlot(noRows,noCols,dataFrame,figName):
    fig = plt.figure(figsize=(15, 8))#Overall size of graph
    fig.canvas.manager.set_window_title(figName)
    i = 0
    warnings.filterwarnings('ignore')
    while (i < len(dataFrame.columns)):
        plt.subplot(noRows, noCols, i + 1) #Numer of rows and number of columns and index positions
        sns.distplot(dataFrame.iloc[:, i]) #plots the distribution of the data
        i += 1

def scaterPlot(xValue,yValue,xTitle,yTitle):
    plt.scatter(xValue,yValue, alpha=0.5)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)
    plt.title(xTitle+" - "+yTitle)
    plt.show()

#import data
data = pd.DataFrame(fetch_california_housing(as_frame=True).data)
print(data.head().to_string())

#Graphical Representation
distributionPlot(2,4,data,"Entire Data") #plotting distribution graph
plt.show()
data.plot(kind='box',subplots=True,layout=(2,4),figsize=(15,8),title="Entire Data")  #box plot
plt.show()
scaterPlot(data["AveRooms"],data["AveBedrms"],"AveRooms","AveBedrms")
scaterPlot(data["HouseAge"],data["MedInc"],"HouseAge","MedInc")
scaterPlot(data["Population"],data["AveOccup"],"Population","AveOccup")
scaterPlot(data["Population"],data["HouseAge"],"Population","HouseAge")

# calculate Q1 and Q3
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3-Q1
print("Q1\n",Q1,"\n")
print("Q3\n",Q3,"\n")
print("IQR\n",IQR,"\n")

#finding upper and lower limit
upper = Q3 + 1.5* IQR
lower = Q1 - 1.5* IQR

print("upper\n",upper,"\n")
print("lower\n",lower,"\n")

#Finding Outliers

Outliers = data[((data<lower) | (data > upper)).any(axis=1)] #Filtering only the Outliers
print(Outliers.head(),"\n")

print("\n Shape before removing Outliers",data.shape)
data1 = data[~((data<lower) | (data > upper)).any(axis=1)] #removing the Outliers
print("\n Shape after removing Outliers",data1.shape)

#Graphical representation after removing Outliers
distributionPlot(2,4,data,"Graph before removing Outliers") #Before
distributionPlot(2,4,data1,"Graph after removing Outliers") #After
plt.show()
data.plot(kind='box',subplots=True,layout=(2,4),figsize=(15,8),title="Graph before removing Outliers")  #box plot before
data1.plot(kind='box',subplots=True,layout=(2,4),figsize=(15,8),title="Graph after removing Outliers")  #box plot after
plt.show()
scaterPlot(data["AveRooms"],data["AveBedrms"],"AveRooms","AveBedrms Before removing Outliers")
scaterPlot(data1["AveRooms"],data1["AveBedrms"],"AveRooms","AveBedrms After removing Outliers")
scaterPlot(data["HouseAge"],data["MedInc"],"HouseAge","MedInc Before removing Outliers")
scaterPlot(data1["HouseAge"],data1["MedInc"],"HouseAge","MedInc After removing Outliers")
scaterPlot(data["Population"],data["AveOccup"],"Population","AveOccup Before removing Outliers")
scaterPlot(data1["Population"],data1["AveOccup"],"Population","AveOccup After removing Outliers")
scaterPlot(data["Population"],data["HouseAge"],"Population","HouseAge Before removing Outliers")
scaterPlot(data1["Population"],data1["HouseAge"],"Population","HouseAge After removing Outliers")