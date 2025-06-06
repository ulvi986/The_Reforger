import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("studentanalysis.csv")

print(df.head()) #ilk 5 setir
print("--------------------")
print(df.tail()) #son 5 setir
print("--------------------")
print(df.info()) #data-type gormek,non-null
print("--------------------")
print(df.describe()) #max,min,mean kimi deyerleri gormek
print("--------------------")
print(df.columns) #sutunlari gormek

"""
X Features:
Attendance (%)
Midterm_Score
Final_Score
Assignments_Avg
Quizzes_Avg
Projects_Score
Participation_Score
Total_Score
Study_Hours_per_Week
Stress_Level (1-10)


y feature:
Grade
"""


X = df[["Attendance (%)","Midterm_Score","Final_Score","Assignments_Avg","Quizzes_Avg","Projects_Score","Participation_Score","Total_Score","Study_Hours_per_Week","Stress_Level (1-10)"]].to_numpy()
y = df["Grade"].to_numpy()

grade_map = {"A": 1, "B": 1, "C":0, "D": 0, "F": 0}
df["Grade_numeric"] = df["Grade"].map(grade_map)
y = df["Grade_numeric"]


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.2,
                                                    random_state=1)

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

X_train = ss.fit_transform(X_train)
X_test = ss.transform(X_test)


#Logistic Regression Modelinin Kurulması
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(y_pred)
print("--------------------------------")
print(y_test)
#Confusion Matrix (Hata Matrisi) ve Accuracy Score
from sklearn.metrics import confusion_matrix, accuracy_score
cmLR = confusion_matrix(y_test, y_pred)
AccuracyScoreLR = accuracy_score(y_test, y_pred)
print(cmLR)
print("--------------------------------")
print(AccuracyScoreLR)
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(classifier, X, y, cv=5)
print("Cross-Validation Scores:", cv_scores)
print("Orta CV Score:", np.mean(cv_scores))
