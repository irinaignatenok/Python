import flask_wtf
import wtforms

class ReviewsForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name: ")
    reviews = wtforms.StringField("Reviews: ")

    submit = wtforms.SubmitField("Leave feedback: ")


class AppointmentForm(flask_wtf.FlaskForm):

    name = wtforms.StringField("Name: ")
    phone = wtforms.IntegerField("Phone: ")
    # data = wtforms.
