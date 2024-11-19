from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/about")
def about():
    return "This is a Flask web app that greets users by name!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
