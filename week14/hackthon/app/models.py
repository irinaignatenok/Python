from . import db
import flask_login


class Reviews(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64))
    reviews = db.Column(db.String(200))

    admin_id = db.Column(db.Integer(), db.ForeignKey("admin.id"))

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

    def deleteFun(self):
        db.session.delete(self)
        try:
            db.session.commit()
            return true
        except:
            db.session.rollback()
            return False


class Admin(db.Model, flask_login.UserMixin):
    id = db.Column(db.Integer(), primary_key = True, autoincrement=True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(128))
    add_picture = db.relationship("Pictures", backref = 'admin')
    delete_review = db.relationship("Reviews", backref = 'admin')

    # appointments = db.relationship('Appointment', backref='admin')
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False


class Pictures(db.Model):
    id = db.Column(db.Integer(), primary_key = True)

    description = db.Column(db.String(64))
    pic_path = db.Column(db.String(512))
    admin_id = db.Column(db.Integer(), db.ForeignKey("admin.id"))

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False


class Appointment(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64))
    phone = db.Column(db.Integer(), nullable = False)
    date = db.Column(db.DateTime())
    description = db.Column(db.String(64))
    # admin_id = db.Column(db.Integer(), db.ForeignKey("admin.id"))

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique = True, nullable = False)
    message = db.Column(db.Text)
    # admin_id = db.Column(db.Integer(), db.ForeignKey("admin.id"))
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
