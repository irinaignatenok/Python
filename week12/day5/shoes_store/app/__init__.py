import flask

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = 'sectdsdsdsd'

inventory = "inventory.json"

from . import routes
