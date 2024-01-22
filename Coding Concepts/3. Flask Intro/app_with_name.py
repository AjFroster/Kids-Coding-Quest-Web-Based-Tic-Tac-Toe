from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my website!"

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/<name>')
def name(name):
    return render_template('name.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
