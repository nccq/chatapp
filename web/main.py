from flask import flask, render_template, url_for, redirect, request, session


NAME_KEY = "name"


app = flask(__name__)
app.secret_key = "cloudy"


@app.route("/login")
def login():
    return render_template("")


@app.route("/home")

def home():
    if NAME_KEY not in session:
        return redirect(url_for("login"))
    return render_template("") 


if __name__ == "__main__":
    app.run(debug = True)