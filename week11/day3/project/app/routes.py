from . import app
from . import forms
import flask

@app.route('/hello')
def hello_world():
    return f"Hello World"


@app.route('/home')
def home_page():
    return flask.render_template('home.html')

@app.route("/happy-birthday", methods=["GET", "POST"])
def happy_birthday():
    form = forms.BirthdayForm()

    if flask.request.method == "POST":
        # form.age.error
        return flask.render_template("happy.html", name = form.name.data, age = form.age.data + 1)
        # return f"Happy birthday, {form.name.data} you're {form.age.data}"
    else:
        return flask.render_template("happy_birthday.html", form=form)


# @app.route("/sign-in", methods=["GET", "POST"])
# def signin():
#     form = forms.SigninForm()
#     if flask.request.method == "POST":
#         if form.username.data == "Irina":
#             flask.flash("welcome", category = "alert-success")
#         else:
#             flask.flash("wrong", category = "alert-danger")
#         return flask.redirect("/")
#
#         # return "Welcome"
#     else:
#         return flask.render_template("signin.html", form = form)


@app.route("/sign-in", methods = ["GET", "POST"])
def signin():
    form = forms.SigninForm()
    print("Checking request method")
    if flask.request.method == "POST":
        #Check if data validators
        print("Validation")
        if form.validate_on_submit():
            flask.flash(f"welcome {form.username.data}", category = "alert-success")
            return flask.redirect("/home")
    # else:
    #Fallback
    # 1) GET method(first is wrong)
    # 2) form is not valid
    return flask.render_template("signin.html", form=form)
