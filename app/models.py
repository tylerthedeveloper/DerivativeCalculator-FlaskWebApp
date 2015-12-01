from app import db
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask import render_template, session
from sqlalchemy import Column, Integer #, Boolean #, DateTime, func
from sqlalchemy.dialects.postgresql import JSON



class User(db.Model):
	__tablename__ = 'user'
	
	id = db.Column(db.Integer, primary_key=True, unique=True)
	name = db.Column(db.String(64), unique=True)
	pWord = db.Column(db.String(64), unique=True)
	#^encrypt / hash
	rMData = db.Column(db.Boolean, default=False)
 	expressions = db.Column(db.String)
 	derivatives = db.Column(db.String)
	
	def __init__(self, name, pWord, rMData, expressions, derivatives):
		self.name = name
		self.pWord = pWord
		self.rMData = rMData
		self.expressions = expressions
		self.derivatives = derivatives
	
	def __repr__(self):
		return {'name': self.name, 'pWord': self.pWord, \
 				'rMData': self.rMData, 'expressions': self.expressions, \
 				'derivatives': self.derivatives}



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