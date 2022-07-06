import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as pt

data = pd.read_csv("Files/weight-height.csv")
data_Male = data[data["Gender"] == "Male"]
data_Female = data[data["Gender"] == "Female"]

plt.subplot(2,3,1)
plt.bar(data_Male["Height"],data_Male["Weight"])

plt.subplot(2,3,2)
plt.barh(data_Male["Height"],data_Male["Weight"])

plt.subplot(2,3,3)
plt.hist([data_Male["Height"],data_Male["Weight"]])

plt.subplot(2,3,4)
x = [20,40,60,60,100]
y = ["car","bike","bus","van","motor"]
plt.pie(x,labels=y,explode=[0.2,0,0,0,0],shadow=True)
plt.show()

dict = { "value":[20,30,40,50],
         "brand":["car","bike","motor","van"]}
plt.pie(dict["value"],labels=dict["brand"])
plt.legend(title="Sales",loc="upper right")
plt.show()

