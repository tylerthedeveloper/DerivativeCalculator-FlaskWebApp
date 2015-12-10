from flask import render_template, flash, redirect, session, g, request, url_for, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from deriver import derive
from .forms import *
from models import User

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
	user = g.user
	#if not logged in or if id exists ? :
	#user = {'nickname': 'New User'}
	return render_template('index.html', user=user, title='Home')
# 	return render_template('index.html', user=user, title='index')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('profile', id=id))
		
	form = LoginForm()
	if form.validate_on_submit():
		#name = form.username.data
		user = User.query.filter_by(name=form.username.data).first()
		id = user.id
		#user_list = User.query.all()
		if user:
			remember_me = False
			if 'remember_me' in session:
				remember_me = session['remember_me']
				#session['remember_me'] = form.remember_me.data
				session.pop('remember_me', None)
			login_user(user, remember=remember_me)
			return redirect(url_for('profile', id=id))
			#return redirect(url_for('user', id=int('<id>')))
			#return redirect(url_for('user', id=current_user.id))
		#flash('You are logged in as %s and set remember me to: %s' %
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if request.method == 'GET':
		return render_template('signup.html', title='signup', form=form)
		
	elif request.method == 'POST':
		username = form.username.data #request.json.get('username')
		nickname = form.nickname.data #request.json.get('nickname')
		#rMData = form.rMData.data #request.json.get('rMData')
		#expressions = form.expressions.data #request.json.get('expressions')
#       derivatives = ''
        pack = User(username, nickname) #, derivatives) , #derivatives) 
        db.session.add(pack)
        db.session.commit()
        flash('Log in with your username %s and nickname %s' % (form.username.data, form.nickname.data))
    	return redirect(url_for('login')) #jsonify(user.report())  #id = int(User.id))
        #render_template('user.html', openid = form.openid.data, title='signup', form=form)
        #return jsonify(user.report())
        #return ('', 200), redirect('/user/<int:id>')
		#flash('You have signed up in as %s and set remember me to: %s' %
		#(form.openid.data, str(form.remember_me.data)))
		#return redirect('/index') --> /index/user/<int:id:>
	return render_template('signup.html', title='signup', form=form)

#@app.route('/user', methods=['GET'])
# @login_required
# def list_users(): #list all..
# 	if request.method == 'GET':
# 		user_list = User.query.all()
# 		report = [user.__repr__() for user in user_list]		
# 		return jsonify(users = report), 200
# 		
# @app.route('/user/<int:id>', methods=['GET', 'POST'])
# @login_required
# def user(id): #id
# 	this_user = User.query.get(id)
# 	if request.method == 'GET':
# 		report = this_user.__repr__()
# 		return jsonify(report), 200
# 
# 	elif request.method == 'POST':
# 		expressions = form.expressions.data #request.json.get('expressions')
# 		e = User(expressions) #update/insert
# 		db.session.add(e)
# 		db.session.commit()
# 		return ('', 200)
# 
# 	return render_template('signup.html', title='signup', form=form)


#add admin auth
@app.route('/user', methods=['GET'])
def list_users(): #list all..
	#if request.method == 'GET':
		user_list = User.query.all()
		report = [user.__repr__() for user in user_list]		
		return jsonify(users = report), 200


#add admin auth
@app.route('/user/<int:id>', methods=['GET'])
def user(id): #id
	this_user = User.query.get(id)
	if request.method == 'GET':
		report = this_user.__repr__()
		return jsonify(report), 200



@app.route('/user/<int:id>/profile', methods=['GET', 'POST'])
def profile(id):
	user = g.user
	id = user.get_id()
	req = request.data
	if req:
		return render_template('deriver.html', title='deriver', user=user, form=form)
	#request.data
	#return redirect(url_for('profile',  id=id))
	#return redirect(request.values.get('next') or url_for('derive'))
	return render_template('user.html', title='profile', user=user, id=id)

 	
@app.route('/user/<int:id>/deriver', methods=['GET', 'POST'])
@login_required
def deriver(id):
	user = g.user
 	form = EntryForm()
 	#form = EntryForm.from_json(request.json)	
	if request.method == 'POST':
		if form.validate_on_submit():
		#from_json
			user.add_expressions(form.expression.data)
			derivative = str(derive(form.expression.data))
			flash('The derivative is %r: ' % derivative)
			user.add_derivatives(derivative)
			db.session.commit()
			#return ('', 200)
		#e = User(expression, derivative) #update/insert
		#e = User(name=name, nickname=nickname, expression, derivative)
		#db.session.add(e)
		#user.derivatives+=(str(derivative))
		#user.expressions+=(form.expression.data)
		#db.session.query(User).filter(User.id ==

		return render_template('deriver.html', title='deriver', user=user, \
			form=form)
	return render_template('deriver.html', title='deriver', user=user, form=form)