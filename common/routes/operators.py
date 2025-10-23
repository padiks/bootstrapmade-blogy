from flask import render_template, request
from common import app

@app.route("/tutorial/operators", methods=["GET", "POST"])
def tutorial_operators():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form.get("a"))
            b = float(request.form.get("b"))
            if b != 0:
                result = round((a / b) * 100, 2)
            else:
                result = "Division by zero!"
        except (ValueError, TypeError):
            result = "Invalid input"
    return render_template("tutorial/operators.html", result=result)
