import flask_wtf
import wtforms as wtf
from wtforms import validators
import json
from . import inventory

with open("/Users/irinaignat/Desktop/Python/week12/day5/shoes_store/app/inventory.json", 'rb') as f:
    data = json.load(f)

class LocationForm(flask_wtf.FlaskForm):
    city = wtf.SelectField('Location:', choices=['New York', 'Paris', 'Tel Aviv'])
    submit = wtf.SubmitField('Submit')


class CustomerItem(flask_wtf.FlaskForm):
    size = wtf.SelectField('Size:', choices = ['38','39','40','41','42'])
    color = wtf.SelectField('color', choices = ['blue', 'red', 'black'])
    submit = wtf.SubmitField('Add to cart')
