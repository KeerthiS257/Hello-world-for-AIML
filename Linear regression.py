# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TZ7dZdGkfO6lkmkH6KUh2LnHJhmks2Ju
"""

#import dependencies
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split

# Include previously executed cell's content at the beginning of new cell, or if in a single script, maintain sequential execution.
from sklearn.datasets import fetch_california_housing
housing=fetch_california_housing()

df_x = pd.DataFrame(housing.data, columns=housing.feature_names)
df_y = pd.DataFrame(housing.target)

#Get some statistics from the data set, count,mean
df_x.describe()

#Initialize the linear regression model
reg = linear_model.LinearRegression()

#Split the data into 67% training and 33% testing data
x_train, x_test, y_train, y_test = train_test_split(df_x,df_y,test_size = 0.33, random_state= 42)

#Train the model with our training data
reg.fit(x_train, y_train)

#Print the coefficient for each feature
print(reg.coef_)

# The original print function was overwritten by a numpy array.
# Re-importing the built-in print function to restore its functionality.
from builtins import print

y_pred = reg.predict(x_test)
print(y_pred)

#Print the actual value
print(y_test)

#Check the model performance/ accuracy using mean squared error (MSE)
print( np.mean( (y_pred - y_test)**2))

#Check the model performance/ accuracy using mean squared error(MSE) and sklearn.metrics
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))