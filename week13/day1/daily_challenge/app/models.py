from . import db
#secondary table for Person <--> Nationality
nationalities_people = db.Table('nationalities_people',
                            db.Column("person_id", db.ForeignKey('person.id'), primary_key = True),
                            db.Column('nationality_id', db.ForeignKey('nationality.id'), primary_key = True)
                            )

class Person(db.Model):
    #db.Column(<TYPE>)
    id = db.Column(db.Integer(), primary_key = True) #this column will be the same

    name = db.Column(db.String(64), nullable = False)
    email = db.Column(db.String(64), unique = True)
    phone = db.Column(db.Integer(), unique = True)
    address = db.Column(db.String(64))
    nationalities = db.Column(db.String(64))
    person_nationality = db.relationship("Nationality", secondary = nationalities_people, backref = db.backref("nat_people", lazy = 'dynamic'))
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return False
    # Password  !flask db migrate, flask db upgrade



class Nationality(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64))


    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
            return True
        except Exception as e:
            print(str(e))
            db.session.rollback()
            return False
