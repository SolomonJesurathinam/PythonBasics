import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import numpy as np

#model function or method
def model(modelName,xtrain,ytrain,xtest):
    model = modelName
    model.fit(xtrain, ytrain)
    y_predict = model.predict(xtest)
    return y_predict

#confusion matrix function
def confusionMatrix(ytest,ypredict):
    confusionMatrix = confusion_matrix(y_test, y_predict)
    print("Confusion Matrix is: \n",confusionMatrix,"\n")
    TP = confusionMatrix[0, 0]
    FP = confusionMatrix[0, 1]
    FN = confusionMatrix[1, 0]
    TN = confusionMatrix[1, 1]
    print("Accuracy is: ",round((metrics.accuracy_score(ytest,ypredict)),2))
    print("Positive Precision is: ", round((metrics.precision_score(ytest, ypredict,pos_label='M')),2))
    print("Negative Precision is: ", round((metrics.precision_score(ytest, ypredict,pos_label='B')),2))
    print("Positive Recall is: ", round((metrics.recall_score(ytest, ypredict, pos_label='M')),2))
    print("Negative Recall is: ", round((metrics.recall_score(ytest, ypredict, pos_label='B')),2))
    print("Positive F1score is: ", round((metrics.f1_score(ytest, ypredict, pos_label='M')),2))
    print("Negative F1score is: ", round((metrics.f1_score(ytest, ypredict, pos_label='B')),2))
    print("Hamming loss is: ",round(metrics.hamming_loss(ytest, ypredict),2)) #Fraction of targets misclassified (0 best - 1 worst)
    print("\nClassification report:\n",classification_report(ytest, ypredict))

#import data
data_csv = pd.read_csv("Files/data.csv")
#print(data_csv.to_string())
print("Shape of data is: \n",data_csv.shape)

#split data
x = data_csv.iloc[:,2:6]
y = data_csv.iloc[:,1]
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)

#Create model

#Model 1 - LogisticRegression
y_predict = model(LogisticRegression(),x_train,y_train,x_test)
print("Logistic Regression")
# Confusion Matrix
confusionMatrix(y_test,y_predict)

#Model 2 - Support Vector Machine
y_predict = model(SVC(),x_train,y_train,x_test)
print("Support Vector Machine")
# Confusion Matrix
confusionMatrix(y_test,y_predict)

#Model 3 - Decision Tree Classifier
y_predict = model(DecisionTreeClassifier(),x_train,y_train,x_test)
print("Decision Tree Classifier")
# Confusion Matrix
confusionMatrix(y_test,y_predict)

#Model 4 - Random Forest Classifier
y_predict = model(RandomForestClassifier(),x_train,y_train,x_test)
print("Random Forest Classifier")
# Confusion Matrix
confusionMatrix(y_test,y_predict)

#Model 5 - XGB Classifier
#only accepts values as 0 and 1 so replacing the values
y_train[y_train == 'B']=0
y_train[y_train == 'M']=1
y_predict = model(XGBClassifier(),x_train,y_train,x_test)

#y_test in conversion matrix is 'B' and 'M', so again replacing the predicted values with 'B' and 'M'
#print(type(y_predict[1]))
y_predict = y_predict.astype(str)
#print(type(y_predict[1]))
y_predict[y_predict == '0'] = 'B'
y_predict[y_predict == '1'] = 'M'

#confusion matrix
confusionMatrix(y_test,y_predict)