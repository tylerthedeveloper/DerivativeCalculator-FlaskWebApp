from flask.ext.wtf import Form
from wtforms import StringField, BooleanField #,FieldList
from wtforms.validators import DataRequired
#from wtforms_json import flatten_json
#import wtforms_json

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
    #expressions = StringField('expressions')
#   derivative = StringField('derivative') #listfield

class EntryForm(Form):
    expression = StringField('expression', validators=[DataRequired()]) #FieldList
    #derivative = StringField('derivative') #listfield
    
#wtforms_json.init()

#form = SignupForm.from_json(json)

#form = EntryForm.from_json()