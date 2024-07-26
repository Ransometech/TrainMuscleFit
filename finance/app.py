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
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    ''')

    user_id = session.get("user_id")

    # Get the user's portfolio
    portfolio = db.execute("""
        SELECT symbol, SUM(shares) AS shares, price, ROUND(SUM(total), 2) AS total
        FROM portfolio
        WHERE user_id = ?
        GROUP BY symbol
    """, user_id)

    # Get the user's current cash balance
    user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = user[0]['cash'] if user else 0

    # Calculate the total portfolio value
    total_portfolio_value = sum([item['total'] for item in portfolio]) + cash

    return render_template('index.html', portfolio=portfolio, cash=round(cash,2), total=round(total_portfolio_value, 2))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        get_quote = lookup(symbol)
        if get_quote is None:
            return apology("Invalid Symbol", 400)


        if not shares.isdigit() or int(shares) <=0:
            return apology("Invalid Shares", 400)
        shares = int(shares)
        price = get_quote["price"]
        total_cost = round(price * shares, 2)

        user_id = session.get("user_id")

        # Fetch user's current cash balance
        user = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        if not user or user[0]['cash'] < total_cost:
            return apology("Insufficient funds", 400)

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_cost, user_id)

        # Insert the transaction into the portfolio table
        db.execute("INSERT INTO portfolio (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)",
                   user_id, symbol, shares, round(price,2), total_cost)

        flash(f'Bought {shares} shares of {symbol}!')
        return redirect("/")
    else:
        return render_template("buy.html")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")

    # Get the user's transaction history
    history = db.execute("SELECT symbol, shares, price, ROUND(total, 2) AS total, timestamp FROM portfolio WHERE user_id = ?", user_id)

    return render_template('history.html', history=history)


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
        get_quote = lookup(symbol)
        if get_quote is None:
            return apology("Invalid Symbol", 400)


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
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        elif request.form.get("confirmation") != request.form.get("password"):
            return apology("The password confirmation does not match", 400)

        # Check if username is available
        check_username = db.execute(
            "SELECT * FROM users WHERE username = ?", username)
        if len(check_username) != 0:
            return apology("Username already exist", 400)

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
    if request.method == "POST":
        symbol = request.form.get("symbol")
        sell_shares = int(request.form.get("shares"))
        get_quote = lookup(symbol)
        if get_quote is None:
            return apology("Invalid Symbol", 403)

        price = get_quote["price"]
        total_value = price * sell_shares

        user_id = session.get("user_id")

        # Get user's current shares of the stock
        user_shares = db.execute("SELECT SUM(shares) as total_shares FROM portfolio WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)
        if not user_shares or user_shares[0]['total_shares'] < sell_shares:
            return apology("Insufficient shares", 403)

        # Insert the transaction into the portfolio table
        db.execute("INSERT INTO portfolio (user_id, symbol, shares, price, total) VALUES (?, ?, ?, ?, ?)",
                   user_id, symbol, -sell_shares, price, -total_value)

        # Update the user's cash balance
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total_value, user_id)

        flash(f'Sold {sell_shares} shares of {symbol}!')

        return redirect("/")

    else:
        user_id = session.get("user_id")
        symbols = db.execute("SELECT symbol FROM portfolio WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", symbols=symbols)
