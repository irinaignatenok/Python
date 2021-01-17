from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/lesson')
def lesson():
    return render_template('in-this-chapter.md')


@app.route('/exercises')
def exercises():
    return render_template('exercises.md')


if __name__ == "__main__":
    app.run(debug=True)
