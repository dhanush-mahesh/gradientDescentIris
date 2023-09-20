# -*- coding: utf-8 -*-
"""IrisGD_Part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PbNDQIDNJAxUO4dSsb4EXd9arlqyDtXC
"""

# Commented out IPython magic to ensure Python compatibility.
#Group Members: Dhanush Mahesh
#Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import SGDRegressor

import statsmodels.api as sm

# %matplotlib inline

df = pd.read_csv("https://raw.githubusercontent.com/dhanush-mahesh/gradientDescentIris/main/iris.data")

df = pd.DataFrame(df)

df.head(50)

#DROP NA values
df_clean = df.dropna()

#Drop Duplicate Rows
df_clean = df_clean.drop_duplicates(keep = False)

#Converting Iris-setosa column to numerical
df_clean['Iris-setosa'] = pd.factorize(df_clean['Iris-setosa'])[0]
df_clean

#Converting the column names to their respective names
col_names = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'Iris-setosa']
df_clean.columns = col_names
df_clean

# plot correlation matrix
correl_matrix = df_clean.corr()
correl_matrix.style.background_gradient()
correl_matrix.style.background_gradient().set_precision(2)

sns.heatmap(data=correl_matrix, annot=True)

# plot distributions
fig, axes = plt.subplots(ncols=2, nrows=3, figsize=[10, 10])
for idx, col in enumerate(df_clean.columns):
  sns.histplot(df_clean[col], ax = axes[idx // 2, idx % 2])

sns.pairplot(df_clean)

#Choose the 5.1, 1.4, 0.2 as the feature selection
x = df_clean[['sepallength', 'petallength', 'petalwidth']]
x

#Assigning x variable with the following variables
x = df_clean[['sepallength', 'petallength', 'petalwidth']]
xArray = x.to_numpy()

yArray = df_clean['Iris-setosa'].to_numpy()
yArray

#Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(xArray, yArray, test_size = 0.2, random_state=5)
print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

#Gradient Descent with multiple attributes
import numpy as np

def gradient_descent(
     gradient, x, y, start, learn_rate=0.1, n_iter=50, tolerance=1e-06
 ):
  vector = start
  for _ in range(n_iter):
    diff = -learn_rate * np.array(gradient(x, y, vector))
    if np.all(np.abs(diff) <= tolerance):
      break
    vector += diff
  return vector

def gradient(X, y, vector):
    # Calculate predicted values
    y_pred = np.dot(X, vector)

    # Calculate residuals
    residuals = y_pred - y

    # Calculate gradients
    gradients = np.dot(X.T, residuals) / len(y)

    return gradients

start_vector = np.zeros(xArray.shape[1])  # Initialize start vector with zeros

coefficients1 = gradient_descent(gradient, x_train, y_train, start_vector, learn_rate = .00009, n_iter = 1000000)
print("Optimal coefficients:", coefficients1)

coefficients2 = gradient_descent(gradient, x_train, y_train, start_vector, learn_rate = .01, n_iter = 50, tolerance = 1e-08)
print("Optimal coefficients:", coefficients2)

coefficients3 = gradient_descent(gradient, x_train, y_train, start_vector, learn_rate = .000008, n_iter = 10000)
print("Optimal coefficients:", coefficients3)

coefficients4 = gradient_descent(gradient, x_train, y_train, start_vector, learn_rate = .0002, n_iter = 100000, tolerance = 1e-09)
print("Optimal coefficients:", coefficients4)

coefficients5 = gradient_descent(gradient, x_train, y_train, start_vector, learn_rate = .0008, n_iter = 100000)
print("Optimal coefficients:", coefficients5)

#Trial 1
y_pred = np.dot(x_train, coefficients1)
mse = mean_squared_error(y_train, y_pred)
print("Training MSE:", mse)

r2 = r2_score(y_train, y_pred)
print("Training R^2:", r2)

#Trial 2
y_pred = np.dot(x_train, coefficients2)
mse = mean_squared_error(y_train, y_pred)
print("Training MSE:", mse)

r2 = r2_score(y_train, y_pred)
print("Training R^2:", r2)

#Trial 3
y_pred = np.dot(x_train, coefficients3)
mse = mean_squared_error(y_train, y_pred)
print("Training MSE:", mse)

r2 = r2_score(y_train, y_pred)
print("Training R^2:", r2)

#Trial 4
y_pred = np.dot(x_train, coefficients4)
mse = mean_squared_error(y_train, y_pred)
print("Training MSE:", mse)

r2 = r2_score(y_train, y_pred)
print("Training R^2:", r2)

#Trial 5
y_pred = np.dot(x_train, coefficients5)
mse = mean_squared_error(y_train, y_pred)
print("Training MSE:", mse)

r2 = r2_score(y_train, y_pred)
print("Training R^2:", r2)

#Trial 1
y_pred = np.dot(x_test, coefficients1)
mse = mean_squared_error(y_test, y_pred)
print("Tested MSE:", mse)

r2 = r2_score(y_test, y_pred)
print("Tested R^2:", r2)

#Trial 2
y_pred = np.dot(x_test, coefficients2)
mse = mean_squared_error(y_test, y_pred)
print("Tested MSE:", mse)

r2 = r2_score(y_test, y_pred)
print("Tested R^2:", r2)

#Trial 3
y_pred = np.dot(x_test, coefficients3)
mse = mean_squared_error(y_test, y_pred)
print("Tested MSE:", mse)

r2 = r2_score(y_test, y_pred)
print("Tested R^2:", r2)

#Trial 4
y_pred = np.dot(x_test, coefficients4)
mse = mean_squared_error(y_test, y_pred)
print("Tested MSE:", mse)

r2 = r2_score(y_test, y_pred)
print("Tested R^2:", r2)

#Trial 5
y_pred = np.dot(x_test, coefficients5)
mse = mean_squared_error(y_test, y_pred)
print("Tested MSE:", mse)

r2 = r2_score(y_test, y_pred)
print("Tested R^2:", r2)