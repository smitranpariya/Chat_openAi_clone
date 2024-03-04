from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

app.run(debug=True)

