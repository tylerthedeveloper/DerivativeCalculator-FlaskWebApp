from flask import render_template, flash, redirect
from app import app
from deriver import derive
from .forms import *

@app.route('/')
@app.route('/index', methods=['GET'])
def index(): #id
	#if not logged in or if id exists ? :
	user = {'nickname': 'New User'}
	return render_template('index.html', user=user, title='index')
	#else:
# 	user = {'nickname': id}
# 	return render_template('index.html', user=user, title='index')

#@app.route('/index/user<int:id:>', methods=['GET'])
# -> learn javascript ...
# @app.route('/user/<int:id:>', methods=['GET'])
# def user(id): #id
#  	user = {'nickname': id}
#  	return render_template('user.html', user=user, title='user')

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('You are logged in as %s and set remember me to: %s' %
		(form.name.data, str(form.remember_me.data)))
		return redirect('/index')
#return redirect('/index') --> /deriver/user/<int:id:>
	return render_template('login.html', title='login', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if form.validate_on_submit():
		flash('You have signed up in as %s and set remember me to: %s' %
		(form.name.data, str(form.remember_me.data)))
		return redirect('/index')
#return redirect('/index') --> /index/user/<int:id:>
#if logged-in: get rid of text, and say hello to logged in user
	return render_template('signup.html', title='signup', form=form)
	
					#user/<int:id:>
@app.route('/deriver', methods=['GET', 'POST'])				
def enterData(): #id 
	#if logged in ?
	#user = user
 	form = EntryForm()
 	if form.validate_on_submit():
 		derivative = derive(form.expression.data)
 		flash('Expression %s has the derivative of %s' % 
 		(form.expression.data, derivative))
	 	return redirect('/deriver')
 	return render_template('deriver.html', title='deriver', form=form)
	#derivatives=derivatives