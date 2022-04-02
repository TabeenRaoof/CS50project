import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]

    shares = db.execute("SELECT symbol, name, price, SUM(shares) FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    total = cash

    for share in shares:
        total += share["price"] * share["SUM(shares)"]

    return render_template("index.html", stocks=shares, remainingCash=cash, usd=usd, totalAssets = total)





@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # Check if method is POST
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        item = lookup(symbol)
        # If symbol is not entered, send an apology message
        if not symbol:
            return apology("Please enter a valid symbol")
        # If symbol is not valid, send an apology message
        elif not item:
            return apology("Symbol is not valid")

        # get the number of shares as an integer
        shares = int(request.form.get("shares"))

        # If number of shares is not an integer, send an apology
        if not shares:
            return apology("Number of shares must be an integer")

        # If the number of shares is 0 or less, send an apology
        if shares <= 0:
            return apology("Number of shares must be a posative integer")

        # Take the user id from current session
        user_id = session["user_id"]
        # Get the amount of cash currently in the user's account
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

        # Take item name price and total price
        item_name = item["name"]
        item_price = item["price"]
        total_price = item_price * shares

        # If user does not have enough cash, send an apology
        if cash < total_price:
            return apology("You don't have enough cash")
        else:
            # If stock is purchased, update amount of cash the user currently
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - total_price, user_id)
            # If stock is purchased, update number of stocks in the user's account
            db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)",
                        user_id, item_name, shares, item_price, 'buy', symbol)

        return redirect('/')
    #  If method is GET
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]
    transactions = db.execute("SELECT type, symbol, price, shares, time FROM transactions WHERE user_id = ?", user_id)
    
    return render_template("history.html", transactions=transactions, usd=usd)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # Check if method is POST
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Error checking: if symbol is not entered
        if not symbol:
            return apology("Please enter a valid stock symbol")

        item = lookup(symbol)

        # Error checking: if symbol is not valid
        if not item:
            return apology("Symbol is not valid")


        # Implement quoted page by getting its html page
        return render_template("quoted.html", stock=item, currency=usd)

    else:
        # Implement quote page by getting its html page
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Check if method is POST
    if(request.method == "POST"):
        # define username, password and confirm
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')
        # Error checking: if user name field is empty
        if not username:
            return apology('Please enter your username')

        # Error checking: if user password field is empty
        elif not password:
            return apology('Please enter your password')

        # Error checking: if user password confirmation field is empty
        elif not confirmation:
            return apology('please confirm your password')

        # Error checking: if user password and password confirmatoin do not match
        elif password != confirmation:
            return apology('passwords do not match')

        # Generate hash for the password
        hash = generate_password_hash(password)

        # Use try, except method to insert username and hash values into database
        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash)
            # If both are correct, the function goes through
            return redirect('/')
            # If username is already used, let the user know to choose another username
        except:
            return apology('The username is in use!')

    # Once all fields are correct and information is entered into the databese, the page is redirected to homepage
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]
    # If POST method is used, implement sell
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Verify and make sure that number of shares is a positive number
        if shares <= 0:
            return apology("Number of shares must be a positive number")

        item_name = lookup(symbol)["name"]
        item_price = lookup(symbol)["price"]
        # Calculate the price of shares
        price = shares * item_price

        user_shares = db.execute("SELECT shares FROM transactions WHERE user_id = ? AND symbol = ? GROUP BY symbol", user_id, symbol)[0]["shares"]
        # Verify to ensure that number of shares selected is not larger than the shares owned by the user
        if shares > user_shares:
            return apology("You are trying to sell more shares than you own, please try again")

        # Get the amount of cash the user currently have from current session
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        # Update the amount of cash the user received from the sell transaction
        db.execute("UPDATE users SET cash = ? WHERE id = ?" , user_cash + price, user_id)
        # Update the number of shares of the stock the user has sold
        db.execute("INSERT INTO transactions (user_id, name, shares, price, type, symbol) VALUES (?, ?, ?, ?, ?, ?)",
        user_id, item_name, -shares, item_price, "sell", symbol)
        return redirect('/')
    else:
        # If method is GET, show the symbols from the list of stocks the user owns and put then in the drop-down menue
        symbols = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
        return render_template("sell.html", shares=symbols)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
