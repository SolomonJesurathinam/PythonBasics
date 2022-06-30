import pandas as pd
import numpy as np

'''Write a Pandas program to create and display a one-dimensional 
array-like object containing an array of data using Pandas module'''

list = [1,2,3,4,5]
array = pd.Series(list)
print(array)

'''Write a Pandas program to convert a Panda module Series to Python list and it's type.'''
list1 = array.to_list()
print(list1)

'''Write a Pandas program to add, subtract, multiple and divide two Pandas Series'''
series1 = pd.Series([1,2,3,4,5])
series2 = pd.Series([6,7,8,9,10])

#add
print("Addition")
print(series1 + series2)

print("Subtraction")
print(series2 - series1)

print("multiplication")
print(series1 * series2)
print("\n")

print("Division")
print(series1 / series2)
print("\n")

'''Write a Pandas program to compare the elements of the two Pandas Series.'''
print(series1 == series2)
print(series1 > series2)
print(series2 > series1)
print("\n")

'''Write a Pandas program to convert a dictionary to a Pandas series'''
dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
pandadict = pd.Series(dict)
print(pandadict)
print("\n")

'''Write a Pandas program to convert a NumPy array to a Pandas series'''
numpyArray = np.array([1,2,3,4,5])
print(numpyArray)
pandaNumpy = pd.Series(numpyArray)
print(pandaNumpy)

nummpy2Array = np.array(([[1,2,3,4,5],
                          [6,7,8,9,0]]))
print(nummpy2Array)
pandaDF = pd.DataFrame(nummpy2Array)
print(pandaDF)
print("\n")

'''Write a Pandas program to change the data type of given a column or a Series'''
pandaDF[0] = pandaDF[0].astype(np.float16)
print(pandaDF[0])
print("\n")

'''Write a Pandas program to convert the first column of a DataFrame as a Series'''
array2d = np.array([[1,2,3],
                    [6,7,8],
                    [11,12,13]])
pandaDF1 = pd.DataFrame(array2d,columns=["Col1","Col2","col3"])
print(pandaDF1)
print("\n")

series3 = pd.Series(pandaDF1["Col1"])
print(series3)
print(type(series3))
print("\n")

'''Write a Pandas program to convert a given Series to an array'''
array1 = np.array(series3)
print(array1)
print(type(array1))
print("\n")


