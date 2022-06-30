#Exercise on KNN Computer
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/horse-colic.csv'
data = pd.read_csv(url, header=None, na_values='?')

print(data.head())
print("Total Shape \n",data.shape) # total row n column
print("Columns with no data \n",data.isnull().sum()) # print column wise null values
print("Total cells with no data \n",data.isnull().sum().sum()) # print total null values

imputer = KNNImputer(n_neighbors=5,weights='uniform',metric="nan_euclidean")  #default values
imputerArray = imputer.fit_transform(data)
filledData = pd.DataFrame(imputerArray)
print(filledData.head())
print("Total Shape \n",filledData.shape) # total row n column
print("Columns with no data \n",filledData.isnull().sum()) # print column wise null values
print("Total cells with no data \n",filledData.isnull().sum().sum()) # print total null values