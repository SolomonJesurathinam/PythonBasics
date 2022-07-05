import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read data
data_csv = pd.read_csv("Files/country_population.csv")
data_csv = data_csv.drop(["Country Code","Indicator Name","Indicator Code"],axis=1)

#x value
x = data_csv.drop("Country Name",axis=1)
x = x.columns.tolist()

#Yvalue
country = input("Enter the country to plot graph: ").strip().capitalize()
index = data_csv[data_csv["Country Name"] == country].index[0]
print(index)
y = np.reshape(data_csv.loc[index:index].drop("Country Name", axis=1).values.tolist(),(-1, 1))

#plotting
plt.plot(x,y)
plt.xticks(x[::5], rotation=90)
plt.show()