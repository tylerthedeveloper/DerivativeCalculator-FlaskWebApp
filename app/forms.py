from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# Super...
# class Form(Form):
#     name = StringField('name', validators=[DataRequired()])
#     password = StringField('name', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    nickname = StringField('nickname', validators=[DataRequired()])
    #pWord = StringField('pWord', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    
class SignupForm(Form):
    username = StringField('username', validators=[DataRequired()])
    nickname = StringField('nickname', validators=[DataRequired()])
    #pWord = StringField('pWord', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    expressions = StringField('expressions', validators=[DataRequired()])
#   derivative = StringField('derivative') #listfield

class EntryForm(Form):
    expressions = StringField('expressions', validators=[DataRequired()])
    derivative = StringField('derivative') #listfield