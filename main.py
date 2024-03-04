from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api")
def qa():
    return render_template("qa.html")

app.run(debug=True)

