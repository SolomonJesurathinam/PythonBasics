#Treating Nan or missing value
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
#Dummification, Central Imputation, KNN Imputation - fillna(0) is the dummification

read_csv = pd.read_csv("MissingValue.csv")
#print(read_csv)

mean = read_csv['Test2'].mean()
median =read_csv['Test2'].median()
mode = read_csv['Test2'].mode()

#print(mean)
#print(median)
#print(mode)

read_csv['Test2'] = read_csv['Test2'].fillna(mean)
#print(read_csv)

#KNN K-Nearest neighbour
read_csv1 = pd.read_csv("MissingValue.csv")
x = [[1,2,np.NaN,3,4,5]]
imputer = KNNImputer(n_neighbors= 1)
#impute_with_1 = imputer.fit_transform(X)
print(read_csv1['Test2'])
impute1 = KNNImputer(n_neighbors=2)
imputer1 = imputer.fit_transform(read_csv1['Test2'].array.reshape(-1,1))
print(imputer1)

impute1 = KNNImputer(n_neighbors=2)
imputer1 = imputer.fit_transform(x)
print(imputer1)
