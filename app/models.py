from app import db
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, session
from sqlalchemy import Column, Integer, Boolean #, DateTime, func
from sqlalchemy.dialects.postgresql import JSON, JSONB

class User(db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, index=True, unique=False)
	nickname = db.Column(db.String, index=True, unique=False)
	#^encrypt / hash
 	expressions = db.Column(db.String)
 #	derivatives = db.Column(db.String, default='')
	
	def __init__(self, name, nickname, expressions): #, derivatives): # pWord,
		self.name = name
		#self.pWord = pWord
		self.nickname = nickname
		self.expressions = expressions
#		self.derivatives = derivatives
	
	
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
		return {'name': self.name, 'expressions': self.expressions, \
					'nickname': self.nickname } #, \
 				#'pWord': self.pWord, 'derivatives': self.derivatives}



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