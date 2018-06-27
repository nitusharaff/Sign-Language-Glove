import numpy as np
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neural_network import MLPClassifier

import pandas as pd
df= pd.read_csv("final data.csv")

from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size = 0.2)


x_train = train[['F1','F2','F3','F4','F5','X','Y','Z','C1','C2']]
y_train = train.cl

x_test = test[['F1','F2','F3','F4','F5','X','Y','Z','C1','C2']]
y_test = test.cl


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit only to the training data
scaler.fit(x_train)
StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

mlp = MLPClassifier(hidden_layer_sizes=(50,50,50))
mlp.fit(x_train,y_train)
MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(30, 30, 30), learning_rate='constant',
       learning_rate_init=0.001, max_iter=200, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)

predictions = mlp.predict(x_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))