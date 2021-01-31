import flask
import flask_sqlalchemy
import flask_migrate
import flask_login
import os
from flask_basicauth import BasicAuth

basedir = os.path.abspath(os.path.dirname(__file__))
app = flask.Flask(__name__)


app.config["SECRET_KEY"] = "sdshidhjkishdihs"
app.config["UPLOAD_DIR"] = os.path.join(basedir,"static/uploads")
app.config["BASIC_AUTH_USERNAME"] = 'tatyana'
app.config["BASIC_AUTH_PASSWORD"] = 'T5Y7K2s3'
app.config['BASIC_AUTH_FORCE'] = True

app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://postgres:V8VcgPjA@localhost:5432/projectdb"

#Create the virtual database
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
basic_auth = BasicAuth(app)

login_manager = flask_login.LoginManager(app)

from . import routes, models

@login_manager.user_loader
def load_user(user_id):
    return models.Admin.query.get(user_id)
