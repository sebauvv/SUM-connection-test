from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)
db_local = 'alumnos.db'

@app.route('/')
def index():
    student_data = query_details()
    return render_template('index.html', student_data=student_data)

def query_details():
    connect = sqlite3.connect(db_local)
    c = connect.cursor()
    c.execute("""
              SELECT * FROM personas
              """)
    student_data = c.fetchall()
    return student_data
    
if __name__ == "__main__":
    app.run(debug=True)
    
    