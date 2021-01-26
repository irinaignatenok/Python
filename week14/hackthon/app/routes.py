from . import app, db
import flask
from . import models, forms
import os
import time
from flask import url_for

@app.route('/home')
def home():
    return flask.render_template("home.html")

@app.route('/reviews', methods = ["GET", "POST"])
def reviews():
    form = forms.ReviewsForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            review = models.Reviews(
                name = form.name.data,
                reviews = form.reviews.data
              )
            review.save()
            return flask.redirect("/all-reviews")

    return flask.render_template("reviews.html", form = form)
@app.route('/all-reviews')
def all_reviews():
    all_reviews = models.Reviews.query.all()
    return flask.render_template("all_reviews.html", all_reviews = all_reviews)
