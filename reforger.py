import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("telebeanalysis.csv")


X = df.iloc[:,2:9].values
y = df.iloc[:,-1].values

"""from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[0])],
                                      remainder="passthrough")

X = np.array(ct.fit_transform(X))
"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=1)
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)

classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(y_pred)
print("--------------------------------")
print(y_test)
from sklearn.metrics import confusion_matrix, accuracy_score
cmLR = confusion_matrix(y_test, y_pred)
AccuracyScoreLR = accuracy_score(y_test, y_pred)
print(cmLR)
print(AccuracyScoreLR)