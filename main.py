from flask import Flask, request, jsonify
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

@app.route("/posts", methods=["GET"])
def get_post():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM posts')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    return jsonify(rows)

@app.route("/posts/<int:post_id>", methods=["GET"])
def get_one_post(post_id):

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = 'SELECT * FROM posts WHERE id = %s;'
    id = (post_id, )
    cursor.execute(sql, id)

    row = cursor.fetchone()
    print(row)
    
    return jsonify(row)


@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')
    category = data.get('category')
    tags = data.get('tags')

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sql = "INSERT INTO posts (title, content, category, tags) VALUES (%s, %s, %s, %s)"
    val = (title, content, category, tags)
    cursor.execute(sql, val)

    mysql.connection.commit()

    # 4. Done (return success)
    return jsonify({
        "message": "Post created successfully", 
        "id": cursor.lastrowid # Tell the user the ID of the new post
    }), 201 # 201 is the HTTP status code for 'Created'

@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):
    data = request.get_json()

    id = post_id
    title = data.get('title')
    content = data.get('content')
    category = data.get('category')
    tags = data.get('tags')

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sql = "UPDATE posts SET title = %s, content = %s, category = %s, tags = %s WHERE id = %s;"
    val = (title, content, category, tags, id)
    cursor.execute(sql, val)

    mysql.connection.commit()

    return '201'


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):


    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    sql = "DELETE FROM posts WHERE id = %s"
    id = (post_id,)
    cursor.execute(sql, id)

    mysql.connection.commit()

    return '204'

# Flask will always ask for the browser icon, this will ignore it  
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)

