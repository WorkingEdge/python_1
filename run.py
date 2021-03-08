import os
from flask import Flask, render_template


app = Flask(__name__)


# When try to browse to root directory ("/"), function index() runs
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")
"""
main is the default that py looks for.
If not imported run app with the fall-back values provided
debug should only be enabled for testing/dev, never for production
"""
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
