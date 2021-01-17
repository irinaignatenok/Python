from . import db, app
import flask
from . import models
from . import forms


@app.route("/home")
def home():
    # return flask.render_template("home.html")
    return "Hello World"

@app.route("/sign-up", methods = ["GET", "POST"])
def add_user():
    form = forms.UserForm()
    print("Checking request method")
    if flask.request.method == "POST":
        if form.validate_on_submit():
            user = models.User()
            db.session.add(user)
            try:
                db.session.commit()
                flask.flash(f" User {form.name.data} created successfully", category = "success")
            except:
                db.session.rollback()
                flask.flash("Something went wrong", category = "danger")

            return flask.redirect('/home')
    return flask.render_template("signin.html", form = form)
