#coding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

list1 = [1,2,3,4,5]
series = pd.Series(list1)
print(series)

series1 = pd.Series(list1,index=["A","b","C","D","E"])
print(series1)
print(series1["A"])

#dataFrame

dataDictionary = {'name':["Solo", "Rajiv", "Ram"],
           'age' :[30,12,15]
           }
dataframe = pd.DataFrame(dataDictionary)
print(dataframe)
print(dataframe['name'])

#Loading File

readCsv = pd.read_csv("C:/Users/solom/Downloads/DummyData.csv",encoding_errors='ignore')

with pd.option_context('display.max_rows', None, 'display.max_columns',None):
    print(readCsv)
#print(readCsv.to_string())

readJson = pd.read_json("C:/Users/solom/Downloads/example_2.json")
print(readJson.to_string())
print(readJson.info())

#Operations

readcsV1 = pd.read_csv("C:/Users/solom/Downloads/Dummycsv.csv",encoding_errors='ignore')
#print(readcsV1.to_string())

#drop naN
newdf = readcsV1.dropna()
#print(newdf.to_string())

#replace
#readcsV1["Value1"] = readcsV1["Value1"].replace(np.nan,0)
#print(readcsV1.to_string())

readcsV1 = readcsV1.fillna(0)
#print(readcsV1.to_string())

#duplicates
readcsV1 = readcsV1.drop_duplicates();   #remove only entire row is duplicate
#print(readcsV1.to_string())

#Aggregate
entireDf = readcsV1.aggregate(['sum','min','max'])
#print(entireDf.to_string())

#singleDf = readcsV1.aggregate({'S.No':['sum','min'], 'Value1':['min','max']})
#print(singleDf)
#singleDf.to_csv("test.csv")

#Data Manipulattions

readnew = pd.read_csv("test.csv")
#print(readnew.to_string())

readnew['Gender'] = readnew['Gender'].map({"Male":'m', "Female":'f'}).astype("str")
#print(readnew)

#Merge
read1 = pd.read_csv("Dummycsv.csv",encoding_errors='ignore')
read2 = pd.read_csv("Dummycsv1.csv",encoding_errors='ignore')

mergeCsv = pd.merge(read2,read1,on='S.No')
#print(mergeCsv.to_string())

#GroupBy
print(mergeCsv.groupby("Year").get_group(2003))

#remove duplicates in a column
print(mergeCsv[~mergeCsv.duplicated("Year")])

#Statitics Mean median mode
stats = pd.read_csv("Statistics.csv",usecols=['Sub1','Sub2'])
print(stats.to_string())

mean = stats.mean(axis=1)
#print(mean)

median = stats.median(axis=1)
#print(median)

mode = stats["Sub1"].mode()
print("Mode")
print(mode)

#skewness

loadcs = pd.read_csv("nba.csv",encoding_errors='ignore')
print(loadcs.skew(axis=0,skipna=True))

#Normal Distribution

xaxis = np.arange(-3,3,000.1)

mean1 = xaxis.mean()
print(mean1)
std = xaxis.std()
print(std)
normalDist = norm.pdf(xaxis,mean1,std)   #mean, SD
plt.plot(xaxis,normalDist)
plt.show()


