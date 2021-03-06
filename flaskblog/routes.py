from flask import flash, render_template,url_for, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
def home():
    return render_template("index.html", movies = movies)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.email.data == 'admin@gmail.com' and form.password.data == 'pass':
        flash('You have logged in successfully', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login unsuccessfull please try again', 'danger')
    return render_template('login.html', title="Login", form = form)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title= 'Register', form = form)
