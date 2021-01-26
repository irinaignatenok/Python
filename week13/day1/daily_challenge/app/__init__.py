import flask
import flask_sqlalchemy
import flask_migrate
import os

basedir = os.path.abspath(os.path.dirname(__file__))
#Create the app controller
app = flask.Flask(__name__)


app.config["SECRET_KEY"] = "sdshidhoishdijjs"
app.config["UPLOAD_DIR"] = os.path.join(basedir,"uploads")

app.config["SQLALCHEMY_DATABASE_URI"] ="postgres://postgres:V8VcgPjA@localhost:5432/thirddb"
#postgres://<username>:<password>@localhost:5432/<db nmae>
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__name__)), "firstdb.db")

#Create the virtual database
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


from . import routes, models
