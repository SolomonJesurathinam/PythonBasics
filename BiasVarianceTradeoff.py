import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from mlxtend.evaluate import bias_variance_decomp

#Bias Variance Tradeoff (Bias is ignore/missing data, variance is considering all data)

#Edit all testing

df = pd.read_csv('weight-height.csv')
df = df[df['Gender']=='Female']
df = df[:]
print(df.head())

# Train Test Split Data
df = df[:]
x_train = df.iloc[:, 1:2].values
x_train = x_train[:3000]
print(x_train)

y_train = df.iloc[:, 2].values
y_train = y_train[:3000]

# Test data

x_test = df.iloc[:, 1:2].values
x_test = x_test[:2000]
y_test = df.iloc[:, 2].values
y_test = y_test[:2000]
print(x_test)
print(y_test)

# Linear Regression
lin = LinearRegression()
lin.fit(x_train, y_train)
plt.scatter(x_train, y_train, color = 'blue')
plt.plot(x_train, lin.predict(x_train), color = 'red')
plt.show()

# Test Plot
plt.scatter(x_test, y_test, color = 'blue')
plt.scatter(x_test, lin.predict(x_test), color = 'red')
plt.show()

model = LinearRegression()
print(model)
# estimate bias and variance
mse, bias, var = bias_variance_decomp(model, x_train, y_train, x_test, y_test, loss='mse', num_rounds=200, random_seed=1)
# summarize results
print('MSE: %.3f' % mse)
print('Bias: %.3f' % bias)
print('Variance: %.3f' % var)