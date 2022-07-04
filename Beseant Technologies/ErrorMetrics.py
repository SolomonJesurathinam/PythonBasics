import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data_csv = pd.read_csv("Files/gender_submission.csv")
print(data_csv.head())

x = data_csv.iloc[:,0:1]
y = data_csv.iloc[:,1:2]
print(x)
print(y)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3)
#plt.plot(x,y)
#plt.show()

model = LinearRegression()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(mae(y_test,y_predict))
print(mse(y_test,y_predict))
print(np.sqrt(mse(y_test,y_predict)))

