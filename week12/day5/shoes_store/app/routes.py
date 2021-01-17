import flask
import json
from . import forms
from . import app, inventory

@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = forms.LocationForm()
    if flask.request.method == "POST":
        city = form.city.data
        return flask.redirect('/main')
    else:
        return flask.render_template("home.html", form = form)


@app.route('/main', methods = ['GET', 'POST'])
def main():
    form = forms.LocationForm()
    form1 = forms.CustomerItem()
    if flask.request.method == "POST":
        city = form.city.data
        size = form1.size.data
        color = form1.color.data
        with open("/Users/irinaignat/Desktop/Python/week12/day5/shoes_store/app/inventory.json", 'rb') as f:
            data = json.load(f)
            f.close()
            stores = data["stores"]
            # for store in stores:
            #     if store["city"] == city:
            products = data["products"]
            # return flask.redirect('/cart')
            return flask.render_template("main.html", city = city,stores=stores, form1 = form1, products = products)
    else:
        return flask.render_template("home.html", form = form)

# @app.route('/add-item',  methods = ['GET', 'POST'])
# def add_item():
#     form = forms.CustomerItem()
#     if flask.request.method == "POST":
#         size = form.size.data
#         color = form.color.data
#         with open("/Users/irinaignat/Desktop/Python/week12/day5/shoes_store/app/inventory.json", 'rb') as f:
#             content = json.load(f)
#             f.close
#             stores = content['stores']
#             return flask.redirect('/cart')
#     else:
#         return flask.render_template("main.html", form = form)




@app.route('/cart')
def cart():
    return "Hello world"
