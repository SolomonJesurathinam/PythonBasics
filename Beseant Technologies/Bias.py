import pandas as pd
from mlxtend.evaluate import bias_variance_decomp
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso

def plotting(Title,xTrain,YTrain,XTest,YTest,TrainLabel,TestLabel):
    ax = plt.axes()
    ax.set_title(Title)
    ax.scatter(xTrain, YTrain, label=TrainLabel)
    ax.scatter(XTest, YTest, label=TestLabel)
    ax.legend()
    plt.show()

def plotting1(Title,totalX,totalY,xvalue,yvalue,FullValueLabel,Predictedlabel):
    ax = plt.axes()
    ax.set_title(Title)
    ax.scatter(totalX, totalY, label=FullValueLabel)
    ax.plot(xvalue,yvalue, label=Predictedlabel,color = 'red')
    ax.legend()
    plt.show()

#read data
df = pd.read_csv("../weight-height.csv")
gender = input("Enter Male/Female/both to calculate:").strip().lower()
if(gender=="male"):
    df = df[df['Gender']=='Male']
elif(gender=="female"):
    df = df[df['Gender'] == 'Female']

#splitting data
x = df.iloc[:, 1:2].values
y = df.iloc[:, 2].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3) # 70% training and 30% test

#plot training and testing data

plotting("Data",X_train,y_train,X_test,y_test,"Train set","Test set")

#Models

#Linear Regression
model = LinearRegression()
mse,bias,var = bias_variance_decomp(model,X_train,y_train,X_test,y_test,loss='mse')
#append values to list
modelList = ['Linear Regression']
biasList = [bias]
mseList = [mse]
varList = [var]
#plot Linear Regression
plotting1("Linear Regression - Train data",X_train,y_train,X_train,model.predict(X_train),"Training Value","Predicted Value")
plotting1("Linear Regression - Test data",X_test,y_test,X_test,model.predict(X_test),"Training Value","Predicted Value")

#Decision Tree Regressor
tree = DecisionTreeRegressor(random_state=123)
mse,bias,var = bias_variance_decomp(tree,X_train,y_train,X_test,y_test,loss='mse',random_seed=123)
modelList.append("Decision Tree Regressor")
mseList.append(mse)
biasList.append(bias)
varList.append(var)
#plot Tree Regressor
plotting1("Decision Tree Regressor - Train data",X_train,y_train,X_train,tree.predict(X_train),"Training Value","Predicted Value")
plotting1("Decision Tree Regressor - Test data",X_test,y_test,X_test,tree.predict(X_test),"Training Value","Predicted Value")

#Lasso Model
lasso = Lasso(alpha=0.5)
mse,bias,var = bias_variance_decomp(lasso,X_train,y_train,X_test,y_test,loss='mse',random_seed=123)
modelList.append("Lasso Model")
mseList.append(mse)
biasList.append(bias)
varList.append(var)
#plot Lasso Model
plotting1("Lasso Model - Train data",X_train,y_train,X_train,lasso.predict(X_train),"Training Value","Predicted Value")
plotting1("Lasso Model - Test data",X_test,y_test,X_test,lasso.predict(X_test),"Training Value","Predicted Value")

#Validating different models results
outputdf = pd.DataFrame({"Model List":modelList,"Mse":mseList,"Bias":biasList,"Variance":varList})
print(outputdf)