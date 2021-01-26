from . import db



class Reviews(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64))
    reviews = db.Column(db.String(200))

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False


class Admin(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))

    appointments = db.relationship('Appointment', uselist = False, backref='admin')
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
    phone = db.Column(db.Integer())
    data = db.Column(db.DateTime())
    description = db.Column(db.String(64))
    admin_id = db.Column(db.Integer(), db.ForeignKey("admin.id"))

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False
