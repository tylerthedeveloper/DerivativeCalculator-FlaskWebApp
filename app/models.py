from app import db
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, session
from sqlalchemy import Column, Integer, Boolean #, DateTime, func
from sqlalchemy.dialects.postgresql import JSON, JSONB

class User(db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, index=True, unique=True)
	nickname = db.Column(db.String, index=True, unique=True)
 	expressions = db.Column(JSONB, unique=False)
 	derivatives = db.Column(JSONB, unique=False)
	
	def __init__(self, name, nickname, expressions=[], derivatives=[]): # pWord,
		self.name = name
		self.nickname = nickname
		self.expressions = expressions
		self.derivatives = derivatives
	
# 	def add_expressions(self, expression):
# 		self.expressions.append(expression)
# 		db.session.query(User).filter(User.id == self.id)\
#                 .update({"expressions": self.expressions})
# 		db.session.commit()
# 
# 	def add_derivatives(self, derivatives):
# 		self.derivatives.append(derivatives)
# 		db.session.commit()
	
	@property
	def is_authenticated(self):
		return True
	
	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)  # python 2
		except NameError:
			return str(self.id)  # python 3
            
	def __repr__(self):
		return {'name': self.name, 'nickname': self.nickname, 
				'derivatives': self.derivatives, 'expressions': self.expressions} 
					#, \ #'pWord': self.pWord, 



# class Data(db.Model):
# 	__tablename__ = 'data'
# 	
# 	# foreign_key
# 	#id = db.Column(db.Integer, primary_key=True, unique=True)
# 	expressions = db.Column(db.String)
# 	derivatives = db.Column(db.String)
# 
# 	def __repr__(self):
#         return '<Expression %r>, pass %r, rM %r' 
#         			% ((self.name, self.pWord, self.rMData))