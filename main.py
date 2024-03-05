from flask import Flask, jsonify, render_template, request
from flask_pymongo import PyMongo
import openai



api_key = "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"
openai.api_key = api_key

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/openai"
mongo = PyMongo(app)

@app.route("/")
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    print(myChats)
    return render_template("index.html", myChats=myChats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question = request.json.get("question")
        chat = mongo.db.chats.find_one({"question": question})
        print(chat)
        if chat:
            data = {"result": f"{chat['answer']}"}
            return jsonify(data)
        else:
            data = {"question": question, "answer": f"answer of this {question}"}
            mongo.db.chats.insert_one({"question": question, "answer": f"answer of this {question}"})
            return jsonify(data)
    data = {"result": "hello"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


