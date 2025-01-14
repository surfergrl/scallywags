import os 
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("/templates/index.html")


@app.route("/")
def about():
    return render_template("/templates/about.html")


@app.route("/")
def contact():
    return render_template("/templates/contact.html")


@app.route("/")
def services():
    return render_template("/templates/services.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )