from flask import Flask, render_template
from data import testimonials, beers

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', testimonials=testimonials)


@app.route('/menu')
def menu():
    return render_template('menu.html', beers=beers)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
