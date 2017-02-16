#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

@app.route('/user/<id>')
def index(name):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user.name

if __name__ == '__main__':
    app.run(debug=True)

