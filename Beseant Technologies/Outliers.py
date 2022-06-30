#Outliers - group of data which is odd man out from the common group
#https://www.analyticsvidhya.com/blog/2021/05/why-you-shouldnt-just-delete-outliers/
#

from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset as a data frame
california_housing = fetch_california_housing(as_frame=True)
df = california_housing.data
print(df.shape)
print(df.head().to_string())

df_graph = df.plot(kind="box", subplots=True, layout=(3,3), figsize=(10,10))
plt.show()

plt.scatter(df.AveRooms, df.AveBedrms, alpha=0.5)
plt.xlabel('AveRooms')
plt.ylabel('AveBedrms')
plt.title('AveBedrms - AveRooms')
plt.show()

plt.scatter(df.HouseAge, df.Population, alpha=0.5)
plt.xlabel('HouseAge')
plt.ylabel('Population')
plt.title('Population - HouseAge')
plt.show()

# calculate Q1 and Q3
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)

# calculate the IQR
IQR = Q3 - Q1
print(Q1,"\n")
print(Q3,"\n")
print(IQR,'\n')

# filter the dataset with the IQR
IQR_outliers = df[((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(IQR_outliers)

# Remove
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df.shape)

df_graph = df.plot(kind="box", subplots=True, layout=(3,3), figsize=(10,10))
plt.show()

plt.scatter(df.AveRooms, df.AveBedrms, alpha=0.5)
plt.xlabel('AveRooms')
plt.ylabel('AveBedrms')
plt.title('AveBedrms - AveRooms')
plt.show()

plt.scatter(df.HouseAge, df.Population, alpha=0.5)
plt.xlabel('HouseAge')
plt.ylabel('Population')
plt.title('Population - HouseAge')
plt.show()