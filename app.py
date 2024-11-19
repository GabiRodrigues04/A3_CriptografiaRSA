from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "a3_criptografia"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'a3_criptografia'

mysql = MySQL(app)


@app.route ('/')
def Index():
    return render_template('index.html')

@app.route ('/voteslist')
def VotesList():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM votes")
    votes = cursor.fetchall()
    cursor.close()

    return render_template('votes.html', votes = votes)

@app.route('/insert', methods = ['POST'])
def Insert():
    
    if request.method == 'POST':

        flash("Voto registrado com sucesso!")

        candidato = request.form['candidato']
        username = request.form['username']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO votes (cripto_vote, username) VALUES (%s, %s)", (candidato, username))
        mysql.connection.commit()
        return redirect (url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)