from flask import render_template, flash, redirect
from app import app
from deriver import derive
from .forms import *

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
	user = {'nickname': 'New User'}
	return render_template('index.html', user=user, title='index')


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('You are logged in as %s and set remember me to: %s' %
		(form.name.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title='login', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		flash('You have signed up in as %s and set remember me to: %s' %
		(form.name.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('signup.html', title='signup', form=form)
	
	
@app.route('/deriver', methods=['GET', 'POST'])				
#def enterData():
def enterData(): 
 	form = EntryForm()
 	if form.validate_on_submit():
 		derivative = derive(form.expression.data)
 		flash('Expression %s has the derivative of %s' % 
 		(form.expression.data, derivative))
	 	return redirect('/deriver')
 	return render_template('deriver.html', title='deriver', form=form)

# def derive(form.expression.data): 
# 	return render_template('deriver.html', title='deriver', form=form)
#derivatives=derivatives