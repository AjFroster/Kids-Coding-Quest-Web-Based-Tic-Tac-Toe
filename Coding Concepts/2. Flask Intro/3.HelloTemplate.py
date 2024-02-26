# Flask can render templates using the Jinja2 template engine. This example requires creating an HTML file named hello.html in a folder named templates in your project directory.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
