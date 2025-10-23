from flask import render_template, request  # <-- added 'request' for POST handling
from common import app

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Tutorial: Operators / Percentage Difference
@app.route("/tutorial/operators", methods=["GET", "POST"])
def tutorial_operators():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            if b != 0:
                result = round((a / b) * 100, 2)  # Calculate percentage, round to 2 decimals
            else:
                result = "Division by zero!"
        except (ValueError, TypeError):
            result = "Invalid input"
    return render_template("tutorial/operators.html", result=result)

