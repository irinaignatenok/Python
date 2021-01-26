import flask_wtf
import wtforms
from wtforms import validators


class SearchForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name: ")
    phone_number = wtforms.IntegerField("Phone number: ", validators=[validators.Optional()])
    submit = wtforms.SubmitField("Submit!")

class AddPersonToDatabase(flask_wtf.FlaskForm):

    id = wtforms.IntegerField('id')
    name = wtforms.StringField("Name")
    email =  wtforms.StringField('Email')
    phone =  wtforms.StringField("Phone")
    address =  wtforms.StringField("Address")
    nationalities =  wtforms.StringField("Nationality")
    submit =  wtforms.SubmitField("Add")
