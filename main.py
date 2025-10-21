from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
from MySQLdb import Error as DBError
import re, os
import json, requests
from dotenv import load_dotenv


load_dotenv()
password = os.environ.get('PASS')
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = password
app.config['MYSQL_DB'] = 'blogs'


mysql = MySQL(app)

@app.route('/')
def hello():
    return 'This is blog api'

@app.route("/posts", methods=["GET"])
def get_post():

    term = request.args.get("term")

    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        if term != None:
            sql = 'SELECT * FROM posts WHERE content = %s OR category = %s OR tags = %s'
            val = (term, term, term)
            cursor.execute(sql, val)
            rows = cursor.fetchall()
            for row in rows:
                if row == None:
                    return 204
                else:
                    print(row)
        else:
            cursor.execute('SELECT * FROM posts')
            rows = cursor.fetchall()
            for row in rows:
                if row == None:
                    return 204
                else:
                    print(row)

    except DBError as e:
        print(f"Database Error: {e}") # Use proper logging in production
        return jsonify({"message": "An internal database error occurred."}), 500
    except Exception as e:
        print(f"Unexpected Error: {e}") 
        return jsonify({"message": "An unexpected error occurred."}), 500   
        
    return jsonify(rows), 200

@app.route("/posts/<int:post_id>", methods=["GET"])
def get_one_post(post_id):

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = 'SELECT * FROM posts WHERE id = %s;'
    id = (post_id, )
    cursor.execute(sql, id)

    row = cursor.fetchone()
    if row:
        print(row)
        return jsonify(row)
    else:
        print("No posts with the ID found")
        return jsonify("No posts with the ID found")
    



@app.route('/posts', methods=['POST'])
def create_post():

    try:
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Invalid JSON or empty request body."}), 400
        
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        tags = data.get('tags')

        if not title or not content:
            return jsonify({"message": "Missing required fields: 'title' and 'content' are mandatory."}), 400
        
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "INSERT INTO posts (title, content, category, tags) VALUES (%s, %s, %s, %s)"
        val = (title, content, category, tags)
        cursor.execute(sql, val)

        mysql.connection.commit()

        return jsonify({
            "message": "Post created successfully", 
            "id": cursor.lastrowid # Tell the user the ID of the new post
        })
    
    except DBError as e:
        # Log the error (use a proper logger in production)
        print(f"Database Error: {e}") 
        return jsonify({"message": f"Database error occurred: {str(e)}"}), 500
    
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return jsonify({"message": "An unexpected server error occurred."}), 500

@app.route("/posts/<int:post_id>", methods=["PUT"])
def update_post(post_id):

    try:
        data = request.get_json()

        if data is None:
            return jsonify({"message": "Invalid JSON or empty request body."}), 400
        

        id = post_id
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        tags = data.get('tags')

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "UPDATE posts SET title = %s, content = %s, category = %s, tags = %s WHERE id = %s;"
        val = (title, content, category, tags, id)
        cursor.execute(sql, val)

                # 4. Check how many rows were affected
        if cursor.rowcount == 0:
            # Post not found, but query executed successfully
            return jsonify({"message": f"Post with ID {post_id} not found."}), 404
        
        mysql.connection.commit()

        return jsonify({
        "message": f"Post with ID {post_id} updated successfully.", 
        "updated_id": post_id}), 200

    except DBError as e:
        print(f"Database Error during update: {e}") 
        return jsonify({"message": f"Database error occurred: {str(e)}"}), 500

    except Exception as e:
        print(f"Unexpected Error during update: {e}")
        return jsonify({"message": "An unexpected server error occurred."}), 500


@app.route("/posts/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    try:

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = "DELETE FROM posts WHERE id = %s"
        id = (post_id,)
        cursor.execute(sql, id)

        mysql.connection.commit()

        return '',204
    
    except DBError as e:
        print(f"Database Error during update: {e}") 
        return jsonify({"message": f"Database error occurred: {str(e)}"}), 500

    except Exception as e:
        print(f"Unexpected Error during update: {e}")
        return jsonify({"message": "An unexpected server error occurred."}), 500


# Flask will always ask for the browser icon, this will ignore it  
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)

