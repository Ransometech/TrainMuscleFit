import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    print("jjindex_portfolio222")

    db.execute('''
    CREATE TABLE IF NOT EXISTS portfolio (
        user_id INTEGER,
        symbol TEXT,
        shares INTEGER,
        price NUMERIC,
        total NUMERIC,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    ''')
    print("index22")

    index_portfolio = db.execute(
            "SELECT symbol, shares, price, total, cash FROM portfolio JOIN users ON id = user_id WHERE id = ?",  session["user_id"])

    print(index_portfolio, "index_portfolio222")
    print("index_portfolioweefdwedfe111")

    return render_template("index.html", index_portfolio = index_portfolio)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        get_quote = lookup(symbol)
        if get_quote is None:
            return apology("Invalid Symbol", 403)

        price = get_quote["price"]
        total_cost = price * shares

        user_id = session.get("user_id")

        # Fetch user's current cash balance
        user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        if not user or user[0]['cash'] < total_cost:
            return apology("Insufficient funds", 403)

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # Insert the transaction into the portfolio table
        db.execute("INSERT INTO portfolio (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)",
                   user_id, symbol, shares, price, total_cost)

        flash(f'Bought {shares} shares of {symbol}!')
        return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        flash('Logged in!')
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol.upper() != "USD":
            return apology("Invalid Symbol", 403)

        get_quote = lookup(symbol)
        return render_template("quote.html", get_quote = get_quote)

    else:
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")

        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        elif not request.form.get("confirm_password"):
            return apology("must confirm password", 403)

        elif request.form.get("confirm_password") != request.form.get("password"):
            return apology("The password confirmation does not match", 403)

        # Check if username is available
        check_username = db.execute(
            "SELECT * FROM users WHERE username = ?", username)
        if len(check_username) != 0:
            return apology("Username already exist", 403)

        print("worked")
        hash_password = generate_password_hash(request.form.get("password"))
        print("worked2")
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",username, hash_password)
        print("worked3")
        reg_rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = reg_rows[0]["id"]
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return render_template("sell.html")
