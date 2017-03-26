#!/usr/bin/env python
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# define the form
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

# page not found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# handle error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST']) # 'POST' is necessary
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name') # the value that saved in session(cookie)
        # using flash
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data # the dict
        return redirect(url_for('index')) # redirect the URL
    return render_template('index.html', form=form, name=session.get('name'))


if __name__ == '__main__':
    manager.run()
