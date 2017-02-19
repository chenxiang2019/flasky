#!/usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('condition.html')

@app.route('/user/<name>')
    return render_template('condition.html', user=name)

if __name__ == '__main__':
    app.run(debug=True)
