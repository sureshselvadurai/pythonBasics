# Chapter 7: Web Development with Python

# Flask - A Web Framework for Python

from flask import Flask, render_template, request

# Creating a Flask application
app = Flask(__name__)


# Basic Route
@app.route('/')
def home():
    return 'Hello, Flask!'


# Route with HTML template rendering
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)


# Handling form submissions
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        return f'Submitted! Hello, {username}!'


# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
