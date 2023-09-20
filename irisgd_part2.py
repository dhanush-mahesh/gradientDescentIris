# -*- coding: utf-8 -*-
"""IrisGD_Part2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gLXtyDk6V_g5AXm31GMv7r-IrbU4CE_9
"""

# Commented out IPython magic to ensure Python compatibility.
#Group Members: Dhanush Mahesh
#Libraries
import numpy as np
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

col_names = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'Iris-setosa']
df_clean.columns = col_names
df_clean

correl_matrix = df_clean.corr()
correl_matrix

#Choose the 5.1, 1.4, 0.2 as the feature selection
x = df_clean[['sepallength', 'petallength', 'petalwidth']]
x

x = df_clean[['sepallength', 'petallength', 'petalwidth']]
xArray = x.to_numpy()

#xArraySL = df_clean[['sepallength']].to_numpy().flatten()
#xArrayPL = df_clean[['petallength']].to_numpy().flatten()
#xArrayPW = df_clean[['petalwidth']].to_numpy().flatten()

yArray = df_clean['Iris-setosa'].to_numpy()
yArray

#Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(xArray, yArray, test_size = 0.2, random_state=5)
print(x_train.shape)
print(y_train.shape)

print(x_test.shape)
print(y_test.shape)

#TRIAL 1
#--------

model = SGDRegressor(learning_rate = 'constant', max_iter = 100000, eta0 = .0008)
model.fit(x_train, y_train)

# model evaluation for training set
y_train_predict = model.predict(x_train)
mse = mean_squared_error(y_train, y_train_predict)
r2 = r2_score(y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test = model.predict(x_test)
rmse = mean_squared_error(y_test, y_test)
r2 = r2_score(y_test, y_test)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))

#TRIAL 2
#--------

model = SGDRegressor(learning_rate = 'constant', max_iter = 50, eta0 = .01)
model.fit(x_train, y_train)

# model evaluation for training set
y_train_predict = model.predict(x_train)
mse = mean_squared_error(y_train, y_train_predict)
r2 = r2_score(y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = model.predict(x_test)
rmse = mean_squared_error(y_test, y_test_predict)
r2 = r2_score(y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))

#TRIAL 3
#--------

model = SGDRegressor(learning_rate = 'constant', max_iter = 10000, eta0 = .000008)
model.fit(x_train, y_train)

# model evaluation for training set
y_train_predict = model.predict(x_train)
mse = mean_squared_error(y_train, y_train_predict)
r2 = r2_score(y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = model.predict(x_test)
rmse = mean_squared_error(y_test, y_test_predict)
r2 = r2_score(y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))

#TRIAL 4
#--------

model = SGDRegressor(learning_rate = 'constant', max_iter = 100000, eta0 = .0002)
model.fit(x_train, y_train)

# model evaluation for training set
y_train_predict = model.predict(x_train)
mse = mean_squared_error(y_train, y_train_predict)
r2 = r2_score(y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = model.predict(x_test)
rmse = mean_squared_error(y_test, y_test_predict)
r2 = r2_score(y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))

#TRIAL 5
#--------

model = SGDRegressor(learning_rate = 'constant', max_iter = 1000000, eta0 = .00009)
model.fit(x_train, y_train)

# model evaluation for training set
y_train_predict = model.predict(x_train)
mse = mean_squared_error(y_train, y_train_predict)
r2 = r2_score(y_train, y_train_predict)

print("The model performance for training set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))
print("\n")

# model evaluation for testing set
y_test_predict = model.predict(x_test)
rmse = mean_squared_error(y_test, y_test_predict)
r2 = r2_score(y_test, y_test_predict)

print("The model performance for testing set")
print("--------------------------------------")
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))