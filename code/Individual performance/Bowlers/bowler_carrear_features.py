# -*- coding: utf-8 -*-
"""Bowler_carrear_features.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MMAzVNx93E_iWxdfqchSdr1pCSXuOMyh
"""

from google.colab import auth
auth.authenticate_user()
import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

wb = gc.open_by_url('https://docs.google.com/spreadsheets/d/1peLpNFoEu8NHtVPttJXz4-aScixYu5dh_-6gYPOi9rQ/edit?ts=5f7f50be#gid=924430584')

sheet = wb.worksheet('bo_data')

data = sheet.get_all_values()

df = pd.DataFrame(data)
df.columns = df.iloc[0]
df = df.iloc[1:]

df.head()

del df["u"]
del df["v"]
del df["w"]
del df["Bowler Score"]

df.dtypes

df.replace('',"?",inplace = True)
df.replace('-',"?",inplace = True)

df.replace('?',np.nan,inplace = True)

df["Height (cm)"]= df["Height (cm)"].astype(float)
df["Man of the match"]= df["Man of the match"].astype(int)
df["Inns"]= df["Inns"].astype(int)
df["Balls"]= df["Balls"].astype(int)
df["Runs"]= df["Runs"].astype(int)
df["Wkts"]= df["Wkts"].astype(int)
df["Ave"]= df["Ave"].astype(float)
df["Econ"]= df["Econ"].astype(float)
df["SR"]= df["SR"].astype(float)
df["4"]= df["4"].astype(int)
df["5"]= df["5"].astype(int)
df["Hat tricks"]= df["Hat tricks"].astype(int)

df['BW'], df['ws'] = df['BBI'].str.split('/', 1).str

df.head()

del df["u"]
del df["v"]
del df["w"]
del df["Bowler Score"]
del df["BBI"]

df.head()

df.dtypes

df["BW"]= df["BW"].astype(int)
df["ws"]= df["ws"].astype(int)

df['BBI'] = df['BW']/df['ws']

df.head(15)

df.tail(15)

df["BBI"].replace(np.inf,1, inplace=True)

df.tail(15)

df['WktAve'] = df['Wkts']/df['Inns']

df.head(15)

df.tail(15)

df.tail(60)

df.mean()

df = df.fillna(df.mean())

print(df.info())

print(df['Bowling Style'].value_counts())

df['Bowling Style'].replace(np.nan,'Right-arm fast-medium', inplace=True)
print(df['Bowling Style'].value_counts())

from sklearn.preprocessing import LabelEncoder

label = LabelEncoder()
df['Bowling Style'] = label.fit_transform(df['Bowling Style'])
le_name_mapping = dict(zip(label.classes_, label.transform(label.classes_)))
print(le_name_mapping)

feature_names = ['Height (cm)', 'Man of the match', 'Bowling Style', 'Runs', 'Wkts', 'Ave', 'Econ', 'SR', '4', '5', 'Hat tricks', 'BBI' ]
X = df[feature_names]
Y = df['WktAve']

import sklearn
print(sklearn.__version__)

#split the data set as training set and test set randomly
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

#apply scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

"""Linear Regression"""

from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot

# define the model
modelreg = LinearRegression()
# fit the model
modelreg.fit(X_train, y_train)
print('Accuracy of Linear regression classifier on training set: {:.2f}'
     .format(modelreg.score(X_train, y_train)))
print('Accuracy of Linear regression classifier on test set: {:.2f}'
     .format(modelreg.score(X_test, y_test)))
# get importance
importance = modelreg.coef_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature:%0d -> %s, Score: %.5f' % (i,feature_names[i],v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.xticks(np.arange(len(feature_names)), feature_names,rotation='vertical')
pyplot.show()

from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from matplotlib import pyplot
# define dataset
#X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
modelran = RandomForestRegressor()
# fit the model
modelran.fit(X_train, y_train)
print('Accuracy of Random Forest classifier on training set: {:.2f}'
     .format(modelran.score(X_train, y_train)))
print('Accuracy of Random Forest classifier on test set: {:.2f}'
     .format(modelran.score(X_test, y_test)))
# get importance
importance = modelran.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature:%0d -> %s, Score: %.5f' % (i,feature_names[i],v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.xticks(np.arange(len(feature_names)), feature_names,rotation='vertical')
pyplot.show()

"""Decision Tree"""

from sklearn.datasets import make_regression
from sklearn.tree import DecisionTreeRegressor
from matplotlib import pyplot
# define dataset
#X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
modeltree = DecisionTreeRegressor()
modeltree.fit(X_train, y_train)
print('Accuracy of Decision Tree on training set: {:.2f}'
     .format(modelran.score(X_train, y_train)))
print('Accuracy of Decision Tree on test set: {:.2f}'
     .format(modelran.score(X_test, y_test)))
# fit the model

# get importance
importance = modeltree.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature:%0d -> %s, Score: %.5f' % (i,feature_names[i],v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.xticks(np.arange(len(feature_names)), feature_names,rotation='vertical')
pyplot.show()

"""Permutation"""

from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance
from matplotlib import pyplot
# define dataset
#X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
modelkn = KNeighborsRegressor()
# fit the model
modelkn.fit(X_train, y_train)
print('Accuracy of knn on training set: {:.2f}'
     .format(modelkn.score(X_train, y_train)))
print('Accuracy of knn on test set: {:.2f}'
     .format(modelkn.score(X_test, y_test)))
# perform permutation importance
results = permutation_importance(modelkn,X_train, y_train, scoring='neg_mean_squared_error')
# get importance
importance = results.importances_mean
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature:%0d -> %s, Score: %.5f' % (i,feature_names[i],v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.xticks(np.arange(len(feature_names)), feature_names,rotation='vertical')
pyplot.show()

"""Xgboost"""

from sklearn.datasets import make_regression
from xgboost import XGBRegressor
from matplotlib import pyplot
# define dataset
X, y = make_regression(n_samples=1000, n_features=10, n_informative=5, random_state=1)
# define the model
modelxg = XGBRegressor()
# fit the model
modelxg.fit(X_train, y_train)
print('Accuracy of knn on training set: {:.2f}'
     .format(modelxg.score(X_train, y_train)))
print('Accuracy of knn on test set: {:.2f}'
     .format(modelxg.score(X_test, y_test)))
# get importance
importance = modelxg.feature_importances_
# summarize feature importance
for i,v in enumerate(importance):
	print('Feature:%0d -> %s, Score: %.5f' % (i,feature_names[i],v))
# plot feature importance
pyplot.bar([x for x in range(len(importance))], importance)
pyplot.xticks(np.arange(len(feature_names)), feature_names,rotation='vertical')
pyplot.show()

"""Carrear Features relationship visualization"""

data = df.copy()

data.dtypes

del data["Player"]
del data["Span"]
del data["Mat"]
del data["Inns"]
del data["Balls"]
del data["BW"]
del data["ws"]

data.dtypes

from pandas.plotting import scatter_matrix
sm = scatter_matrix(data, alpha=0.2, figsize=(13, 13), diagonal='kde')

#Change label rotation
[s.xaxis.label.set_rotation(90) for s in sm.reshape(-1)]
[s.yaxis.label.set_rotation(0) for s in sm.reshape(-1)]

#May need to offset label when rotating to prevent overlap of figure
[s.get_yaxis().set_label_coords(-1.5,0.5) for s in sm.reshape(-1)]

#Hide all ticks
[s.set_xticks(()) for s in sm.reshape(-1)]
[s.set_yticks(()) for s in sm.reshape(-1)]
plt.show()