import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import pi
from math import exp
from scipy import stats

#Probability


#Theoritical - based on outcome - occurance/total posibility
#Relative(Experimental) - predicting by existing data
#Subjective -

df=pd.DataFrame({"Gender":["male", "male", "female", "male"],
                "Survived":[0,0,1,1]})

prob = df.loc[df['Gender'] == 'male', 'Survived'].mean()
prob_percent = df.groupby('Gender')['Survived'].mean()
#print(prob)
#print(prob_percent)

load = pd.read_csv("tested.csv")
prob_percent = load.groupby('Age')['Survived'].mean()
#print(prob_percent)


df1= pd.DataFrame(columns=['No','quantity'], data=[[1,100.0],[2,145.3],[3,301.3],[4,101.3],[5,101.3],[6,120.3]])
print(df1.to_string())
#Probability on invalid data

mean = df1['quantity'].mean()
print(mean)

sd = df1['quantity'].std()
print(sd)

#normalDist = norm.pdf(df1['quantity'],mean,sd)   #mean, SD
#plt.plot(df1['quantity'],normalDist)
#plt.show()

''' z-sccore = (x-mean)/sd'''
zscore = (df1['quantity'] - mean)/sd
#print(zscore) #positive value is above SD, negative denoted below SD
df1['z_score']=stats.mstats.zscore(df1.quantity)
#print(df1['z_score'])

df1['prob']=df1['quantity'].apply(lambda x: stats.norm(mean,sd).pdf(x) if x > mean else 1 - stats.norm(mean,sd).pdf(x))
print(df1['prob'])
df1['prob_percent'] = df1['prob'].apply(lambda x: x*100)
print(df1)

def normal_pdf(x, mu, sigma):
    return 1.0 / (sigma * (2.0 * pi)**(1/2)) * exp(-1.0 * (x - mu)**2 / (2.0 * (sigma**2)))
print((1-normal_pdf(100.0,mean,sd))*100)

yaxis = norm.pdf(df1['quantity'],mean,sd)
print(yaxis)
plt.plot(df1['quantity'],yaxis)
#plt.show()


'''for idx,row in df1.iterrows():
    # print(stats.norm.pdf((row.quantity),mu,sig))
    if row.quantity < mean:
        df1.at[idx,'prob'] = 1- (stats.norm(mean,sd).pdf(row.quantity))
    else:
        df1.at[idx,'prob'] = stats.norm(mean, sd).pdf(row.quantity)
'''

#odds Ratio
oddsRatio = pd.read_csv("oddsRatio.csv")
print(oddsRatio)

group = oddsRatio.groupby(["AboveBMI","Health Problem"]).size().reset_index(name="count")
print(group)

ExtYesOutcomeYes = group['count'][3]
print(ExtYesOutcomeYes)

ExtNoOutcomeYes = group['count'][1]
print(ExtNoOutcomeYes)

ExtYesOutcomeNo = group['count'][2]
print(ExtYesOutcomeNo)

EXTNoOutcomeNo = group['count'][0]
print(EXTNoOutcomeNo)

odds = stats.fisher_exact([[ExtYesOutcomeYes,ExtYesOutcomeNo],[ExtNoOutcomeYes,EXTNoOutcomeNo]])
print(odds)

'''
(ExtYesOutcomeYes/ExtNoOutcomeYes)/(ExtYesOutcomeNo/EXTNoOutcomeNo)
'''

ManualValidation = (ExtYesOutcomeYes/ExtNoOutcomeYes)/(ExtYesOutcomeNo/EXTNoOutcomeNo)
print(ManualValidation)


#SD and Variance

list = [600,470,170,430,300]
print(list)

add = sum(list)
total = len(list)
mean = add/total
print(mean)

mean1 = np.mean(list)
print(mean1)

#variance = Get the distance from mean from all values and calculate
difflist = []
#differencce between mean and value
for x in list:
    difflist.append(mean - x)
print(difflist)

#sigma2 or variance formula = Average of square of difflist
squareList = []
for x in difflist:
    squareList.append(x*x)
print(squareList)

variance = np.mean(squareList)
print(variance)

#square root of variance will give standard deviation
sd = math.sqrt(variance)
print(sd)

sd2 = variance**(1/2)
print(sd2)

sd1 = np.std(list)
print(sd1)

ps = pd.Series(list)
print(ps.std()) #Pandas is using Bessels correction by default. to correcct it use ddof=0
print(ps.std(ddof=0))

'''
Calculate mean
Calculate the difference of each value with mean
Average of the square of difference values = variance
square root of variance gives standard deviation
plot SD from mean (positive and negative) -- it will be near all data points    
'''



