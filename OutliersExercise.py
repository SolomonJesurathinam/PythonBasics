from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

def distributionPlot(noRows,noCols,dataFrame):
    plt.figure(figsize=(15, 8)) #Overall size of graph
    i = 0
    warnings.filterwarnings('ignore')
    while (i < len(dataFrame.columns)):
        plt.subplot(noRows, noCols, i + 1) #Numer of rows and number of columns and index positions
        sns.distplot(dataFrame.iloc[:, i]) #plots the distribution of the data
        i += 1
    plt.show()

#import data
data = pd.DataFrame(fetch_california_housing(as_frame=True).data)
print(data.head().to_string())
print(data.shape)

#Distribution plot
distributionPlot(2,4,data)