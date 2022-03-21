# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 10:10:03 2022

@author: chand
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import datasets

iris = datasets.load_iris()
x =iris.data
y=iris.target

print('speal-length','sepal-width','petal-length','petal-width')
print(x)
print('class: 0-iris-setosa, 1-iris-versicolor, 2-iris-verginica')
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)
print('Confusion Matrix')
print(confusion_matrix(y_test,y_pred))

print('Accuracy Matrix')
print(classification_report(y_test, y_pred))