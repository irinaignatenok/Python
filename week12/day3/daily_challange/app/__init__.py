import flask
import flask_migrate
import flask_sqlalchemy

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "200891da40be484a869a3b8205522bee"


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:V8VcgPjA@localhost:5432/firstdb"

db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)


from . import routes, models
