from flask import Flask, render_template

from flask_mysqldb import MySQL





app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'

app.config['MYSQL_USER']='root'

app.config['MYSQL_PASSWORD']='SURYAteja123'

app.config['MYSQL_DB']='db'

mysql = MySQL(app)



@app.route("/")

def hello():

    cur = mysql.connection.cursor()

    cur.execute('''SELECT text FROM data WHERE id = 123''')

    result = cur.fetchall()

    return render_template('home1.html', result=result)

 









if __name__ == "__main__":

       app.run(debug=1)