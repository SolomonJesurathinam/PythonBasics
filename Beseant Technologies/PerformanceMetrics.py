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

'''
[8:27 am, 01/07/2022] Beseant Trainer: # Confusion Matrix
con_matrix = confusion_matrix(y_test,y_predict)
print(con_matrix)

# Print Report

print(classification_report(y_test,y_predict))
[8:34 am, 01/07/2022] Beseant Trainer: import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report


df = pd.read_csv("data.csv")
print(df.shape)
print(df.head(5).to_string())

x = df.iloc[:,2:6]
print(x.head().to_string())
y = df.iloc[:,1]
print(y.head().to_string())

# Train data

x_train = x[:200]
y_train = y[:200]

# Test data

x_test = x[200:500]
y_test = y[200:500]

# Create model

logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)
y_predict = logmodel.predict(x_test)

# Confusion Matrix
con_matrix = confusion_matrix(y_test,y_predict)
print(con_matrix)

# Print Report

print(classification_report(y_test,y_predict))
'''