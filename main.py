from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

# Load the JSON data
input_file= "posts.json"
with open(input_file, encoding="utf-8") as json_file:
    parsed_json = json.load(json_file)

@app.route("/posts", methods=["GET"])
def get_post():
    return parsed_json



# Flask will always ask for the browser icon, this will ignore it  
@app.route('/favicon.ico')
def favicon():
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=True)

