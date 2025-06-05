import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("telebeanalysis.csv")


X = df.iloc[:,2:9].values
y = df.iloc[:,-1].values

#Train ve Test Setleri
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=1)

#Feature Scaling (Özellik Ölçekleme)
#Standardization
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)

from sklearn.svm import SVC
classifier = SVC(probability=True, kernel="rbf")

classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)

#Confusion Matrix ve Accuracy Score
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
AccuracySVM = accuracy_score(y_test, y_pred)
print(cm)
print(AccuracySVM)