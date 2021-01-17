import flask_wtf
import wtforms
from wtforms import validators

class BirthdayForm(flask_wtf.FlaskForm):
    age = wtforms.IntegerField("Age:")
    name = wtforms.StringField("Name:")

    submit = wtforms.SubmitField("Greet!")



class SigninForm(flask_wtf.FlaskForm):
    username = wtforms.StringField("Username: ", validators = [validators.DataRequired("A name is require")])
    password = wtforms.PasswordField("Password: ")

    submit = wtforms.SubmitField("Sign in! ")
