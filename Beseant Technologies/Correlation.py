#relation between 2 points
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

read_csv = pd.read_csv("../weight-height.csv")
print(read_csv.head())

x = read_csv['Height']
y = read_csv['Weight']
#Numpy
cor = np.corrcoef(x,y)
print(cor)

#Pearsons
corr1 = pearsonr(x,y)
print(corr1) #second value is probability value
print('CORR: %.3f' %corr1[0])



