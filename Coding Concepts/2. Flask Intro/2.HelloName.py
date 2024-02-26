# This demonstrates how to use routing to handle different URLs. It includes a dynamic route that takes a name as part of the URL.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/hello')
def hello():
    return 'Hello, there!'

@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True)
