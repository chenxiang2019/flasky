#!/usr/bin/env python3

from flask import Flask, render_template
from flask_wtf import Form
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# using to define the form 
class NameForm(Form):
	"""docstring for NameForm"""
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

# set flask-wtf
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string' # set secret key

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# handle error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
	name = None # set default
	form = NameForm()
	if form.validate_on_submit(): # user's form is fine
		name = form.name.data
		form.name.data = ''
	return render_template('index.html', form=form, name=name)

if __name__ == '__main__':
	manager.run(debug=True)	
