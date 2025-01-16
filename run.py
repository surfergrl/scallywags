import os 
from flask import Flask, render_template, request, flash

app = Flask(__name__)

if os.path.exists("env.py"):
    import env

app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/about")
def about():
    return render_template("/about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form["email"])
        print(request.form["phone"])
        print(request.form["message"])
        flash("Thanks {}, I have received your message!".format(request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/services")
def services():
    return render_template("/services.html")


@app.route("/login")
def login():
    return render_template("/login.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )