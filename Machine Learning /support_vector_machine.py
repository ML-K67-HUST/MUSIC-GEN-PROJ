import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix, classification_report
import pickle
dataset = pd.read_csv("GTZAN/Data/features_30_sec.csv")

df = dataset.copy()

non_floats = []
for col in df.iloc[:,:-1]:
    if df[col].dtypes != "float64":
        non_floats.append(col)
df = df.drop(columns=non_floats)

L = len(df.columns)
X = df.iloc[:,:L-1].values
df.label = pd.Categorical(df.label)
y = np.array(df.label.cat.codes)


scaler = StandardScaler()


clf = svm.SVC(kernel='rbf', gamma='scale', C=50)

clf.fit(X,y)

with open('svm_model.pkl','wb') as file:
  pickle.dump(clf, file)


