from . import app
import flask
import json
import os

#Exercise1
@app.route("/hours/<int:hour>")
def greet(hour):
    if 8 <= hour <= 13:
        return f"It's {hour}. Good morning"
    elif 13 < hour <= 17:
        return f"It's {hour}. Good afternoon"
    elif 17 < hour <= 21:
        return f"It's {hour}. Good evening"
    elif (21 < hour <= 23 )or (0 <=  hour< 8):
        return f"It's {hour}. Good night"
    else:
        return f"It's {hour}. You entered the wrong number"

#Exercise 2
@app.route("/")
def greeting_message():
    return flask.render_template("homepage.html")

@app.route("/products")
def store_products(src_file="/Users/irinaignat/Desktop/Python/week11/day3/exercises/app/products.json"):
    # filename = os.path.join(app, "products.json")
    with open(src_file, "r") as f:
        data = json.load(f)
    # f = open("products.json", "r")
    # data = json.load(f)
    # f.close()
    return flask.render_template("productpage.html", data=data)
