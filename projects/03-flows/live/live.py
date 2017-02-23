import pandas as pd
import numpy as np
import pickle
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import cross_val_score
from sklearn.svm import LinearSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import scale
from sklearn.preprocessing import StandardScaler

with open('logit_ttl.pkl', 'rb') as f:
    logit = pickle.load(f)

with open('svc_ttl.pkl', 'rb') as f:
    svc = pickle.load(f)

with open('forest_ttl.pkl', 'rb') as f:
    forest = pickle.load(f)

#  with open('knn.pkl', 'rb') as f:
#      knn = pickle.load(f)

with open('scale_ttl.pkl', 'rb') as f:
    std_scale = pickle.load(f)

df = pd.read_csv('live_metis.csv')

df['State'] = df['State'].map(lambda x: 1 if x=='REQ' else 0)
#  df = df[df['sHops'] <= 1]
df = df.dropna(subset=['sMaxPktSz'])
df = df.fillna(df.mean())
#  df = df.iloc[:,:7]

df_scale = std_scale.transform(df)

logit_pred = logit.predict(df_scale)
svc_pred = svc.predict(df_scale)
forest_pred = forest.predict(df_scale)
#  knn_pred = knn.predict(df_scale)

print('Logit\nPositive Records:', sum(logit_pred))
print('Total Records:', len(logit_pred))
print('% Positive:', float(int(10000*sum(logit_pred)/len(logit_pred))/100))
print('\n')
print('SVC\nPositive Records:', sum(svc_pred))
print('Total Records:', len(svc_pred))
print('% Positive:', float(int(10000*sum(svc_pred)/len(svc_pred))/100))
print('\n')
print('Forest\nPositive Records:', sum(forest_pred))
print('Total Records:', len(forest_pred))
print('% Positive:', float(int(10000*sum(forest_pred)/len(forest_pred))/100))
print('\n')
#  print('KNN\nPositive Records:', sum(knn_pred))
#  print('Total Records:', len(knn_pred))
#  print('% Positive:', float(int(10000*sum(knn_pred)/len(knn_pred))/100))

