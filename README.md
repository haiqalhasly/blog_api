# BLOG API

API for blog platform 

## Features

Here's some features that are implemented in this app:

* Create a new blog post
* Update an existing blog post
* Delete an existing blog post
* Get a single blog post
* Get all blog posts
* Filter blog posts by a search term


## Getting Started

### Prerequisites

* Python 3.1 or higher
* Flask
* MySQL 
* cURL or Postman for API testing


### Installation
1. Clone the repository (in the terminal of your ide)

```py
git clone https://github.com/haiqalhasly/blog_api.git
```
3. Create a virtual environment

```py
  python -m venv venv
```
5. Activate the virtual environment
   * On windows
    ```py
    venv\Scripts\activate
    ```

   * On macOS/Linux
    ```py
    source venv/bin/activate
    ```

7. Install dependencies
```py
  pip install -r requirements.txt
```
8. Create environments variable
 ```bash
  touch.env
```
9. Within the `env`, add following content:
```env
    PASS='your_password_for_sql
```

## Usage

Run `app.py` in command line or F5 key to start the server
```bash
python app.py
```


## API Response Format
The tool processes JSON responses from the Visual Crossing Weather API API using this format.
```
    {   
        "id":1,
        "title": "My First Blog Post",
        "content": "This is the content of my first blog post.",
        "category": "Technology",
        "tags": ["Tech", "Programming"]
    }
```

## Things that I have learned:
This project is a good starter to learn HTTP requests, SQL database integration etc. Here's what I have achieved :

* Database Integration : How to integrate code with database.
* MySQL Setup : How to setup MySQL for VS Code.
* cURL API Testing : How to test API using cURL for methods like GET, POST, PUT and DELETE.
* Environment Variable Support: Uses a .env file for secure configuration of password.
* RESTful API: Simple endpoints for easy integration with other applications.
* Error Handling: Handles HTTP and SQL database errors gracefully.

## References

1. Flask & API Development
* <https://pythonbasics.org/flask-http-methods>
* <https://flask.palletsprojects.com/en/stable/api/>
* <https://www.youtube.com/watch?v=Cz3WcZLRaWc>
* <https://www.youtube.com/watch?v=U79OeSC75bs>

2. SQL & Database Operations
* <https://www.w3schools.com/sql/default.asp>
* <https://www.w3schools.com/python/python_mysql_insert.asp>
* <https://stackoverflow.com/questions/44864695/loop-through-an-table-in-sql-and-update-a-row-every-time>
* <https://www.youtube.com/watch?v=ROcZyGYtjOE>
* <https://www.youtube.com/watch?v=3tguxobYsq4>

3. Utilities & Troubleshooting
* <https://10web.io/blog/how-to-fix-mysql-error-1049-unknown-database/>
* <https://scrapingant.com/blog/curl-cheatsheet>
* <https://kb.naverisk.com/en/articles/5569958-how-to-install-curl-in-windows>
