import flask
app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "asdfghjkl"#encrypt the data
from . import routes
