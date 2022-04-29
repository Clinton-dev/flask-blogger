from math import remainder
from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e11cf5a9529dd1a984dc6a390c1d06094c9b6a2e'

movies = [
    {
        "author":"Clinton-dev",
        "name": "Dark night rises",
        "description": "After Gordon, Dent and Batman begin an assault on Gotham's organised crime, the mobs hire the Joker, a psychopathic criminal mastermind who offers to kill Batman and bring the city to its knees.",
        "rating":8,
        "year":2007
    },
    {
        "author":"Kwambugu",
        "name": "Creed",
        "description": "Adonis Johnson, the son of heavyweight champion Apollo Creed, embraces his legacy as a boxer and seeks mentorship from Rocky Balboa, his father's old friend and rival.",
        "rating":9,
        "year":2017
    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("index.html", movies = movies)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form = form)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title= 'Register', form = form)

if __name__ == '__main__':
    app.run(debug=True)