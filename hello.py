from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "Your name is Robbie!"

if __name__ == "__main__":
    app.run()