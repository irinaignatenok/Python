import flask_wtf
import wtforms
from wtforms.fields.html5 import DateField, TimeField

class ReviewsForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name: ")
    reviews = wtforms.StringField("Reviews: ")

    submit = wtforms.SubmitField("Leave feedback: ")

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ")

    submit  = wtforms.SubmitField("Sign up")

class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username: ")
    password = wtforms.PasswordField("Password: ")

    submit = wtforms.SubmitField("Sign in")

class PicturesForm(flask_wtf.FlaskForm):

    description = wtforms.StringField("Description: ")
    pic = wtforms.FileField("Picture: ")

    submit = wtforms.SubmitField("Add picture")

class AppointmentForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name: ")
    phone = wtforms.IntegerField("Phone: ")
    date = DateField("Date and Time: ")
    time = TimeField("Time: ")
    description = wtforms.StringField("What kind of service would you like? ")
    submit = wtforms.SubmitField("Book an Appointment: ")

class ContactForm(flask_wtf.FlaskForm):
    name = wtforms.StringField("Name: ")
    email = wtforms.StringField("Email: ")
    message = wtforms.TextAreaField("Message: ")
    submit = wtforms.SubmitField("Send: ")


# class AdminForm(flask_wtf.FlaskForm):
#
#     username = wtforms.StringField("Username: ")
#     password = wtforms.PasswordField("Password: ")
#
#     submit  = wtforms.SubmitField("Sign in")
