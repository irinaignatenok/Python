from . import app
import flask
import json


@app.route('/layout')
def home_page():
    return flask.render_template("layout.html")

@app.route('/homepage')
def home_page():
    return flask.render_template("homepage.html")

@app.route("/products")
def all_products():
    f = open("/Users/irinaignat/Desktop/Python/week11/day5/miniproject/app/product.json", 'r')
    content = json.load(f)
    f.close()
    return flask.render_template("allproducts.html", data = content, title = "All Products")

@app.route("/product_details/<int:product_id>")
def product_details(product_id):
    f = open("/Users/irinaignat/Desktop/Python/week11/day5/miniproject/app/product.json", 'r')
    content = json.load(f)
    this_product = content[product_id]
    f.close()
    return flask.render_template("productdetail.html", product = this_product, title = "Product")
