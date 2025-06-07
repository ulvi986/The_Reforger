import pandas as pd
import mysql.connector
import random

# ✅ 1. CSV faylını oxu
df = pd.read_csv("studentanalysis.csv")

# ✅ 2. Lazım olan sütunları seç və ilk 50 tələbəni götür
required_columns = [
    "Attendance (%)", "Midterm_Score", "First_Name", "Last_Name", "Final_Score",
    "Assignments_Avg", "Quizzes_Avg", "Projects_Score",
    "Participation_Score", "Total_Score", "Study_Hours_per_Week", "Grade"
]
df = df[required_columns].head(50).copy()

# ✅ 3. 50 unikal valideyn yarat (ad + soyad random)
parent_first_names = ["Aysel", "Elvin", "Murad", "Gunay", "Samir", "Lale", "Rauf", "Nigar", "Kamran", "Sevda"]
parent_last_names = ["Mammadov", "Aliyeva", "Huseynov", "Ismayilova", "Taghiyev", "Najafli", "Guliyev", "Rustamli", "Rahimov"]

parent_list = []
for i in range(50):
    parent_id = f"P{i+1:02d}"
    name = f"{random.choice(parent_first_names)} {random.choice(parent_last_names)}"
    contact = f"+99455{random.randint(1000000,9999999)}"
    parent_list.append((parent_id, name, contact))

# ✅ 4. Hər tələbəyə uyğun valideyn təyin et (1:1)
df["Parent_ID"] = [parent_list[i][0] for i in range(50)]

# ✅ 5. MySQL bağlantısı
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  # buranı öz şifrənlə dəyiş
    database="School"
)
cursor = conn.cursor()

# ✅ 6. Cədvəlləri təmizlə
cursor.execute("DELETE FROM parents")
cursor.execute("DELETE FROM students")

# ✅ 7. Valideynləri əlavə et
cursor.executemany(
    "INSERT INTO parents (Parent_ID, name, contact) VALUES (%s, %s, %s)",
    parent_list
)

# ✅ 8. Tələbələri əlavə et
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO students (
            Attendance, Midterm_Score, First_Name, Last_Name, Final_Score,
            Assignments_Avg, Quizzes_Avg, Projects_Score,
            Participation_Score, Total_Score, Study_Hours_per_Week,
            Grade, Parent_ID
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row["Attendance (%)"], row["Midterm_Score"], row["First_Name"], row["Last_Name"], row["Final_Score"],
        row["Assignments_Avg"], row["Quizzes_Avg"], row["Projects_Score"],
        row["Participation_Score"], row["Total_Score"], row["Study_Hours_per_Week"],
        row["Grade"], row["Parent_ID"]
    ))

# ✅ 9. Yadda saxla
conn.commit()
print("✅ 50 tələbə və 50 valideyn MySQL-ə əlavə olundu – hər biri unikal və əlaqəlidir.")
