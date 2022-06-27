import pandas as pd
from mlxtend.evaluate import bias_variance_decomp
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#read data
df = pd.read_csv("weight-height.csv")

#splitting data
y = df["Weight"].values
x = df["Height"].values
#x = df.drop(["Weight"],axis=1) #considering both Gender and Height
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3) # 70% training and 30% test

#plot training and testing data

ax = plt.axes()
ax.set_title("Data")
ax.scatter(X_train,y_train, label = "Train set")
ax.scatter(X_test,y_test, label = "Test set")
ax.legend()
plt.show()

#Models

#Linear Regression
model = LinearRegression()
mse,bias,var = bias_variance_decomp(model,X_train,y_train,X_test,y_test,loss='mse')
print(mse)
print(bias)
print(var)
