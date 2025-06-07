from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


def get_student_by_parent(parent_id, parent_name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="School"
    )
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
                   SELECT s.*, p.name AS Parent_Name
                   FROM students s
                            JOIN parents p ON s.Parent_ID = p.Parent_ID
                   WHERE p.Parent_ID = %s
                     AND p.name = %s
                   """, (parent_id, parent_name))

    result = cursor.fetchall()
    conn.close()
    return result


@app.route('/', methods=['GET', 'POST'])
def index():
    students = []
    if request.method == 'POST':
        parent_id = request.form['parent_id']
        parent_name = request.form['parent_name']
        students = get_student_by_parent(parent_id, parent_name)
    return render_template('index.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
