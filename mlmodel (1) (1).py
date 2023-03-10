# -*- coding: utf-8 -*-
"""MLModel.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cPqneA4TJ2SMkK9cqYg6vZVdO81xsPH_
"""

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv("/content/drive/MyDrive/BankNote_Authentication.csv")

data.head()

data.tail()

data.isnull().sum()

data.dtypes

x=data.drop('class',axis=1)
y=data['class']
print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=50)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pickle
pickle_out = open("BankNote.pkl","wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()

classifier.predict([[2,3,4,1]])



