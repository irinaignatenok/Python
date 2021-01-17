import flask_wtf
import wtforms
from wtforms import validators

class UserForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name: ", validators = [validators.Required("A name is required!")])
    age = wtforms.IntegerField("Age: ")

    submit = wtforms.SubmitField("Sign in!")
