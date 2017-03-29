# My Hello.py

import os
from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

# Config the DataBase
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite') # config by URL
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

class Switches(db.Model):
	__tablename__ = 'Switches'
	id = db.Column(db.Integer, primary_key=True)
	sname = db.Column(db.String, unique=True, index=True)
	sprice = db.Column(db.Integer)

	def __repr__(self):
		print('<Switch_id %d>' % id)

class NameForm(FlaskForm):
    name = StringField('What is switch name?', validators=[Required()])
    submit = SubmitField('Submit')

def make_shell_context():
    return dict(app=app, db=db, Switches=Switches)
manager.add_command("shell", Shell(make_context=make_shell_context))

# Error Handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        sw = Switches.query.filter_by(sname=form.name.data).first() # filter the DB
        if sw is None:
            sw = sw(sname=form.name.data)
            db.session.add(sw)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('myindex'))
    return render_template('myindex.html', form=form, name=session.get('name'),
                           known=session.get('known', False))

if __name__ == '__main__':
    manager.run()
