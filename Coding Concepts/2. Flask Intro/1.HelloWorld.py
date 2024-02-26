# This script sets up a simple Flask application that displays "Hello, World!" on the home page.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

if __name__ == "__main__":
    app.run(debug=True)