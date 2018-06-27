import numpy as np
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

import pandas as pd
df= pd.read_csv("final.csv")


#########################################################################


from sklearn.model_selection import train_test_split
train, test = train_test_split(df, test_size = 0.2)


train_features = train[['F1','F2','F3','F4','F5','X','Y','Z','C1','C2']]
train_label = train.cl

test_features = test[['F1','F2','F3','F4','F5','X','Y','Z','C1','C2']]
test_label = test.cl

## SVM
model = svm.SVC(kernel='linear', gamma=1, C=1)
model.fit(train_features, train_label)
model.score(train_features, train_label)
predicted_svm = model.predict(test_features)
print "svm"
print accuracy_score(test_label, predicted_svm)
cn =confusion_matrix(test_label, predicted_svm)

"""""
##Decision Tree
print "dtree"
clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_features, train_label)
predicted_dt = clf.predict(test_features)
print accuracy_score(test_label, predicted_dt)
confusion_matrix(test_label, predicted_dt)

#########################################################################

##Random Forest
print  "rf"
rf = RandomForestClassifier(max_depth = 5)
rf = rf.fit(train_features, train_label)
predicted_rf = rf.predict(test_features)
print accuracy_score(test_label, predicted_rf)
confusion_matrix(test_label, predicted_rf)

########################################################################

##Naive Bayes
print "naive"
gnb = GaussianNB()
gnb = gnb.fit(train_features, train_label)
predicted_gnb = gnb.predict(test_features)
print accuracy_score(test_label, predicted_gnb)
confusion_matrix(test_label, predicted_gnb)

"""""