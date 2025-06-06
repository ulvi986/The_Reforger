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


