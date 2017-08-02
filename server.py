"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import (Flask, jsonify, render_template, redirect, request, flash,
                   session, SQLAlchemy)

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db

# <script src="https://code.jquery.com/jquery.js"></script>

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    a = jsonify([1,3])
    return render_template('homepage.html')

@app.route('/register', methods=['GET'])
def register_form():
    """Show registration form page."""

    return render_template('register_form.html')

@app.route('/register', methods=['POST'])
def register_form():
    """Get data from registration form and redirect to homepage."""
    

    reg_email = request.form.get("email")
    reg_password = request.form.get("password")

    # checking if the email is already in the database
    if User.query.filter(User.email == reg_email):
        alert("This email is already registered")
    else:
    

        if request.form.get("age"):
            age = request.form.get("age")
        else:
            age = None


        if request.form.get("zipcode"):
            zipcode = request.form.get("zipcode")
        else:
            zipcode = None

    return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5000, host='0.0.0.0')
