from flask import Flask, render_template, request
from responses import getBotResponses
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") #loads html chatbot UI
@app.route("/get")
def get_response():
    user_input = request.args.get("msg")
    response = getBotResponses(userInput)
    return response

if __name__ == "__main__":
    app.run(debug=True)