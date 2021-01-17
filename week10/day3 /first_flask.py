#creating a controler
import flask
app = flask.Flask(__name__)#name of this file(required by flask)
import datetime

#create a view
            #URI you want to map your function to
# @app.route("/hello") #decorator(put the function definition)
#
#
def helloworld():
    return "Hello world!"
@app.route("/")
@app.route("/about")
def info_about_me():
    return "My name is Irina, I'm 30 years old"
@app.route("/today")
def about_today():
    today_date = datetime.datetime.now()
    return f"{today_date.day}/{today_date.month}/{today_date.year}"
#Run the server(listen to connections and answer clients)
@app.route("/profile")
def profile():
    return flask.render_template("profile.html", name = "Eyal")


@app.route("/article")
def article():
    article = {
        "source": {
            "id": "handelsblatt",
            "name": "Handelsblatt"
        },
        "author": "J\u00fcrgen R\u00f6der",
        "title": "Dax aktuell: Dax schlie\u00dft nach neuem Rekordstand im Minus",
        "description": "Der aktuelle Aufw\u00e4rtstrend am deutschen Aktienmarkt verl\u00e4uft sehr dynamisch. An diesem Dienstag haben sich Anleger besonders auf die SAP-Aktie fokussiert.",
        "url": "https://www.handelsblatt.com/finanzen/maerkte/marktberichte/dax-aktuell-dax-schliesst-nach-neuem-rekordstand-im-minus/26755142.html",
        "urlToImage": "https://www.handelsblatt.com/images/dax-kurve-im-handelssaal-in-frankfurt/23734752/66-format2003.jpg",
        "publishedAt": "2020-12-29T16:51:29Z",
        "content": "D\u00fcsseldorf Der deutsche Leitindex Dax ist am Dienstag mit einem leichten Minus aus dem Handel gegangen. Er schloss 0,2 Prozent tiefer bei 13.761 Punkten. Am Vormittag hatte der Dax allerdings zun\u00e4chs\u2026 [+6393 chars]"
        }
    return flask.render_template("news.html", article = article)


@app.route("/my-friends")
def my_friends():
    friends = ["Irina", "Tom", ]
    return flask.render_template("friends.html", friends = friends)


@app.route("/greet/<name>")# 127.0.0.1:5000/greet/eyal
def greet(name):
    return f"Hello {name}"

@app.route("/birthday/<int:age>")# 127.0.0.1:5000/greet/eyal
def birthday(age):
    next_age = age +1
    # return f"Hello, next year you will be {next_age}"
    return flask.render_template("condition.html", age = next_age)

@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
    multiplication = num1*num2
    return flask.render_template("multiplication.html",multiplication = multiplication)

@app.route("/str-len/<word>")
def how_long(word):

    return f"{word} contains {len(word)} characters"

def lookup_news(query_keyword):
    import requests
    url = f"http://newsapi.org/v2/everything?q={query_keyword}&from=2020-12-03&sortBy=publishedAt&apiKey=5719809a4f814d0d9f8cb98e7a3d97de"
    return requests.get(url).json()['articles'][:5]


@app.route('/news/bitcoin')
def bitcoin_news():
    articles = lookup_news("bitcoin")
    return render_template("news.html", articles = articles)

if __name__ == "__main__":
    app.run(debug=True) #to refresh terminal
#120.0.0.1 --> Aliased to your IP address
#5000 --> port
#127.0.0.1:5000 domain name (like www.facebook.com)
#to get the data go to the --> http://127.0.0.1:5000/hello
