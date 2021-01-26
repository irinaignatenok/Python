from . import app, db
import flask
from . import models, forms


@app.route("/search-person", methods = ['GET', 'POST'])
def search_person():
    form = forms.SearchForm()
    return flask.render_template('submit_file.html', form = form)


@app.route("/results", methods = ['GET','POST'])
def show_results():
    form = forms.AddPersonToDatabase()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            person = models.Person(
                name = form.name.data,
                email = form.email.data,
                phone = form.phone.data,
                address = form.address.data,
                nationalities = form.nationalities.data
            )
            if person.save():
                flask.flash(f" Person {person.name} created successfully", category = "success")
                return flask.redirect('/people')

            else:
                flask.flash("Something went wrong", category = "danger")
            return flask.redirect('/home')

    return flask.render_template("people_list.html",form = form)

@app.route("/people")
def display_people():
    users = models.Person.query.all()
    return flask.render_template("people.html", users = users)

@app.route("/nationality", methods = ['GET','POST'])
def add_nationality():
    form = forms.SearchForm()
