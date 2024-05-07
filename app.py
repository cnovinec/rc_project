import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///rc.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show profile data"""
    # gets all users shares and stocks and remaing monney
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id",
                      user_id=session["user_id"])[0]["cash"]

    # create variubles
    total_value = cash
    grand_total = cash

    # add price and total value of stock
    for stock in stocks:
        quote = lookup(stock["symbol"])
        # this wont work with the quote functiona and does not load page .stock["name"] = quote["name"]
        stock["price"] = quote["price"]
        stock["value"] = quote["price"] * stock["total_shares"]
        total_value += stock["value"]
        grand_total += stock["value"]

    return render_template("index.html", stocks=stocks, cash=cash, total_value=total_value, grand_total=grand_total)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # gets all transactions from current user
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY id DESC", user_id=session["user_id"])

    # renders template
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            flash("Invalid username and/or password")
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return apology("must provide password", 400)


        # Checks re-type was entered
        elif not request.form.get("confirmation"):
            flash("must provide both password")
            return apology("must provide both passwords", 400)

        # Checks passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            flash("Passwords must match")
            return apology("Passwords must match", 400)

        # checks that there is not already username in db
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # checks if username exists
        if len(rows) != 0:
            flash("Username taken please enter a new username.")
            return apology("Username taken please enter a new username.", 400)

        # if new user adds user to db and logs them in
        else:
            reg_username = request.form.get("username")
            hashed_password = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                       reg_username, hashed_password)
            rows = db.execute("SELECT * FROM users WHERE username = ?", reg_username)
            session["user_id"] = rows[0]["id"]
            return redirect("/")

    return render_template("register.html")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """Changes user password"""

    username = db.execute("SELECT username FROM users WHERE id = :user_id",
                          user_id=session["user_id"])[0]["username"]
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure password was submitted
        if not request.form.get("password"):
            flash("must provide password")
            return apology("must provide password", 403)

        # Checks re-type was entered
        elif not request.form.get("retype_password"):
            flash("mustprovide both passwords")
            return apology("must provide both passwords", 403)

        # Checks passwords match
        elif request.form.get("password") != request.form.get("retype_password"):
            flash("Password must match")
            return apology("Passwords must match", 403)

        # updates new password to DB if all other conditions are meet.
        else:
            hashed_password = generate_password_hash(request.form.get("password"))
            db.execute("UPDATE users SET hash = :hash WHERE id = :user_id",
                       hash=hashed_password, user_id=session["user_id"])
            flash("Your Password has successfully been changed")
            return redirect("/")

    return render_template("changepassword.html", username=username)

@app.route("/tests")
@login_required
def tests():
    """Form to submit test results"""
    # gets all transactions from current user
    transactions = db.execute(
        "SELECT * FROM transactions WHERE user_id = :user_id ORDER BY id DESC", user_id=session["user_id"])

    # renders template
    return render_template("tests.html")

@app.route("/climbing_wheel")
@login_required
def climbing_wheel():
    """Climbing Wheel function showing wheel of skills"""

    # set variubles to be inserted into db
    user_id = session["user_id"]
    flexability = request.form.get("flexability")
    dynamic_movement = request.form.get("dynamic_movement")
    strength = request.form.get("strength")
    power = request.form.get("power")
    endurance = request.form.get("endurance")
    finger_strength = request.form.get("finger_strength")
    balance = request.form.get("balance")
    technique = request.form.get("technique")
    total_score = flexability + dynamic_movement + strength + power + endurance + finger_strength + balance + technique


    # enters all information into the db
    db.execute("INSERT INTO results_wheel (user_id, flexability, dynamic_movment, strength, power, endurance, finger_strength, balance, technique, total_score) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
               user_id, flexability, dynamic_movement, strength, power, endurance, finger_strength, balance, technique, total_score)
    # renders template
    return render_template("climbing_wheel.html")
