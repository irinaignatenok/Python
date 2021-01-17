from flask import Flask, render_template
app = Flask(__name__)
import datetime
import random
from faker import Faker
fake = Faker()




#Exercise XP but css file doesn't work
@app.route('/cv/<name>')
def my_cv(name):
    return render_template('index.html', name = name)

#Exercise gold 1
@app.route('/today')
def display_date():
    today_date = datetime.datetime.now()
    return f"{today_date.day}/{today_date.month}/{today_date.year}"

#Exercise gold 2
@app.route('/countdown')
def countdown():
    current_date = datetime.datetime.now()
    first_januar = datetime.datetime(2022, 1, 1)
    next_year = first_januar - current_date
    return f"{next_year} left before the New Year"

#Exercise gold 3
@app.route('/number/<num>')
def random_number(num):
    ran_number = random.randint(1,100)

    return render_template('exercise_gold.html', num1 = ran_number, num = num)
#Exercise gold 4
@app.route('/nextholiday')
def next_holiday():
    date = datetime.datetime.now()
    holiday = datetime.datetime(2021, 2, 14)
    countdown = holiday - date
    return render_template('exercise_gold.html', date = date, countdown = countdown)

#Exercise NINJA
@app.route('/ninja/<name>')
def exercise_ninja(name):
    name = fake.name()
    text = fake.text()
    return render_template('cv.html', name = name, text = text)

#Exercise NINJA
@app.route('/ninja')
def redirect_page():
    return render_template('cv2.html')


if __name__ == '__main__':
    app.run(debug=True)
