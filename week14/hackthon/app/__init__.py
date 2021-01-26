import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)


app.config["SECRET_KEY"] = "sdshidhjkishdihs"
app.config["UPLOAD_DIR"] = os.path.join(basedir,"uploads")

app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://postgres:V8VcgPjA@localhost:5432/projectdb"

#Create the virtual database
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


from . import routes, models
