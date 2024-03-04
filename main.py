from flask import Flask, jsonify,redirect, render_template, request, session, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods = ["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        print(request.json)
        data = {"result":question}
        return jsonify(data)
    

app.run(debug=True)

