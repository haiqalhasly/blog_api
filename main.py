from flask import Flask, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import json
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Haiqal2403.'
app.config['MYSQL_DB'] = 'blogs'


mysql = MySQL(app)

@app.route('/')
def hello():
    return 'Hello'

# Load the JSON data
input_file= "posts.json"
with open(input_file, encoding="utf-8") as json_file:
    parsed_json = json.load(json_file)

@app.route("/posts", methods=["GET"])
def get_post():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM posts')
    account = cursor.fetchone()
    return account



# Flask will always ask for the browser icon, this will ignore it  
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)

