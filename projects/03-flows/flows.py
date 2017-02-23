import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from tqdm import tqdm
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.learning_curve import learning_curve
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale

df_clean = pd.read_pickle('flows_clean.pkl')

y = df_clean['Label']
X = df_clean.drop(['StartTime', 'SrcAddr', 'Sport', 'DstAddr', 'Label'], axis=1)
X = X.drop(['Proto', 'Dir', 'State', 'Dport', 'TcpOpt', 'sHops', 'sTtl', /
            'TotAppByte', 'SrcBytes', 'SrcJitter', 'PCRatio', 'Load', /
            'TotPkts', 'pLoss'], axis=1)

X['sMaxPktSz'] = df_clean['sMaxPktSz'].fillna(0)
X['sMinPktSz'] = df_clean['sMinPktSz'].fillna(0)
X['SIntPkt'] = df_clean['SIntPkt'].fillna(0)

X_scaled = scale(X)
y_bin = [0 if i == 'normal' else 1 for i in y]

# Logistic Regression
# logreg = LogisticRegression(class_weight={0: 0.05})
# log_acc = cross_val_score(logreg, X, y_bin, cv=10, scoring='f1')
# print(log_acc)

# Gaussian Naive Bayes
# gauss = GaussianNB()
# gauss_acc = cross_val_score(gauss, X_scaled, y_bin, cv=10, scoring='f1')
# print(gauss_acc)

# SVM
# svm = SVC()
# svm_acc = cross_val_score(svm, X_scaled, y_bin, cv=10, scoring='f1')
# print(svm_acc)

# Decision Trees
# tree = DecisionTreeClassifier()
# tree_acc = cross_val_score(tree, X_scaled, y_bin, cv=10, scoring='f1')
# print(tree_acc)

# Random Forests
# forest = RandomForestClassifier()
# forest_acc = cross_val_score(forest, X_scaled, y_bin, cv=10, scoring='f1')
# print(forest_acc)
