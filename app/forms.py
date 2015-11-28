from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# Super...
# class Form(Form):
#     name = StringField('name', validators=[DataRequired()])
#     #password = StringField('name', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)

class LoginForm(Form):
    name = StringField('name', validators=[DataRequired()])
    #password = StringField('name', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    
class SignupForm(Form):
    name = StringField('name', validators=[DataRequired()])
    #password = StringField('name', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    
class EntryForm(Form):
    expression = StringField('expression', validators=[DataRequired()])
#    derivative = StringField('derivative') #listfield