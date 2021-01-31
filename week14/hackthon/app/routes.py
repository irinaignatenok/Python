from . import app, db, basic_auth
import flask
from . import models, forms
import os
import time
from flask import url_for
import flask_login
import datetime
from flask_basicauth import BasicAuth


@app.route('/home')
def home():
    pictures = models.Pictures.query.all()
    return flask.render_template("home.html", pictures = pictures)


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

@app.route('/my-reviews')
def my_reviews():
    reviews = models.Reviews.query.all()
    return flask.render_template("my_reviews.html", reviews = reviews)

@app.route('/delete/<int:id>')
def delete_review(id):
    reviews_to_delete = models.Reviews.query.get_or_404(id)

    try:
        db.session.delete(reviews_to_delete)
        db.session.commit()
        flask.flash("Review has been deleted...")
        return flask.redirect('/my-reviews')
    except:
        return "There was a problem deleting that post..."

    # user = models.Admin.query.get(1)
    # reviews.admin = user
    # db.execute = ([request.form[admin_id]])
    # db.commit()
    # flask.flash("Review was deleted")
    # return flask.redirect('/my-reviews')

@app.route('/make-appointment', methods = ["GET", "POST"])
def make_appointment():
    form = forms.AppointmentForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            date = datetime.datetime.combine(form.date.data,form.time.data)
            appointment = models.Appointment(
                    name = form.name.data,
                    phone = form.phone.data,
                    date = date,
                    description = form.description.data
              )
            # admin = flask_login.current_user

            # appointment.admin_id = admin.id

            appointment.save()
            flask.flash("Appointment booked successfully...")

            # return flask.redirect('/all-appointments')

            return flask.redirect("/home")

    return flask.render_template("appointment.html", form = form)
@app.route('/all-appointments')
def all_appointments():

    all_appointments = models.Appointment.query.all()

    return flask.render_template("all_appointments.html", appointments = all_appointments)

@app.route('/delete-appointment/<int:id>')
def delete_appointment(id):
    appointment_to_delete = models.Appointment.query.get_or_404(id)

    try:
        db.session.delete(appointment_to_delete)
        db.session.commit()
        flask.flash("Appointment has been deleted...")
        return flask.redirect('/all-appointments')
    except:
        return "There was a problem deleting that appointment..."

@app.route("/pictures/new/", methods = ["GET", "POST"])
def add_pictures ():
    form = forms.PicturesForm()
    if flask.request.method == "POST":
      if form.validate_on_submit():
          pic = form.pic.data

          pic_name = f" {int(time.time())}.jpg"
          pic_filename = os.path.join(app.config["UPLOAD_DIR"], pic_name)

          pic.save(pic_filename)

          picture = models.Pictures(
                description = form.description.data,
                pic_path = pic_name,
          )
          admin = models.Admin.query.get(1)
          picture.admin_id = admin.id

          picture.save()
          return flask.redirect('/home')
    return flask.render_template("pictures.html", form = form)

@app.route('/all-pictures')
def all_pictures():
    pictures = models.Pictures.query.all()
    return flask.render_template("home.html", pictures = pictures)

@app.route("/trendy-hairstyles")
def trendy_hairstyles():
    return flask.render_template("trendy_hairstyles.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    form = forms.ContactForm()
    if flask.request.method == "POST":
      if form.validate_on_submit():
          contact = models.Contact(
                name = form.name.data,
                email = form.email.data,
                message = form.message.data
          )
          # admin = models.Admin.query.get(1)
          # picture.admin_id = admin.id

          contact.save()
          flask.flash("Your message has been sent...")
          return flask.redirect('/home')
    return flask.render_template('contact.html', form = form)


@app.route('/messages')
def message():
    messages = models.Contact.query.all()

    return flask.render_template('messages.html', messages = messages)

@app.route('/reply')
def reply_client():
    form = forms.ContactForm()
    client = models.Contact.query.filter_by(email = form.email.data)
    flask.flash("Thank you for your message. I will answer you as soon as possible ")
    return flask.redirect('/home')






@app.route('/secret')
@basic_auth.required
def secret_view():

    return flask.render_template('home.html')

@app.route('/my-page')
def my_page():
    return flask.render_template("my_page.html")

# @app.route('/login-page', methods= ["GET", "POST"])
# def my_page():
#     form = forms.SigninForm()
#     if flask.request.method == "POST":
#       if form.validate_on_submit():
#           password = 'irina'
#           if password == form.data.password:
#               return flask.redirect("my_page.html")
#
#     return flask.render_template("login_page.html", form = form)

@app.route('/sign-up', methods = ["GET", "POST"])
def add_admin():
     form = forms.SignupForm()
     if flask.request.method == "POST":
         if form.validate_on_submit():
             admin = models.Admin(
                username=form.username.data.lower(),
                password=form.password.data
                )
             if admin.save():
                flask.flash(f"User {admin.username} created successfully", category="success")
             else:
                flask.flash("Something went wrong..")
             return flask.redirect("/my-page")
     return flask.render_template("signup.html", form=form)


@app.route('/sign-in', methods = ["GET", "POST"])
def sign_in():
    form = forms.SigninForm()
    if flask.request.method == "POST":
        if form.validate_on_submit():
            admin = models.Admin.query.filter_by(username = form.username.data.lower()).first()
            if admin is None:
                flask.flash("User does not exist...")
                return flask.redirect("/sign-in")
            else:
                if admin.password == 'irina':
                    flask_login.login_user(admin)

                    flask.flash(f"Welcome, {admin.username.title()}")
                    return flask.redirect('/my-page')
                else:
                    flask.flash("Wrong credentials")
    return flask.render_template("sign_in.html", form = form)

@app.route('/sign-out')
def signout():
    flask_login.logout_user()
    return flask.redirect("/home")
