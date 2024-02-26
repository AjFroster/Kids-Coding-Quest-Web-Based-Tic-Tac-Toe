# This example demonstrates handling form data. You'll need an HTML form in a template named submit.html.

from flask import Flask, request, render_template, render_template_string
app = Flask(__name__)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return render_template_string(f'<h1>Hello, {name}!</h1>')
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
