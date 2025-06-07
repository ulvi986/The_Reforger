import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
df = pd.read_csv("studentanalysis.csv")


X = df[["Attendance (%)","Midterm_Score","Final_Score","Assignments_Avg","Quizzes_Avg","Projects_Score","Participation_Score","Study_Hours_per_Week","Stress_Level (1-10)"]].values
y = df["Total_Score"].values

from sklearn.ensemble import RandomForestRegressor
rg = RandomForestRegressor(random_state = 42,n_estimators = 10,max_depth=100,criterion="absolute_error")
#n_estimators = agac sayi mesedeki

rg.fit(X,y)
y_predict = rg.predict(X)
score = r2_score(y,y_predict)
print(y_predict)
print(score)
from sklearn.model_selection import cross_val_score

cv_scores = cross_val_score(rg, X, y, cv=5)
print("Cross-Validation Scores:", cv_scores)
print("Orta CV Score:", np.mean(cv_scores))

from sklearn.model_selection import cross_validate

scores = cross_validate(rg, X, y, cv=5, return_train_score=True)
print("Train mean:", scores["train_score"].mean())
print("Test mean :", scores["test_score"].mean())
