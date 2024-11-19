from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'a3_criptografia'

mysql = MySQL(app)

@app.route ('/')
def Index():
    return render_template('index.html')

@app.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        name = request.form['candidato']


if __name__ == "__main__":
    app.run(debug=True)