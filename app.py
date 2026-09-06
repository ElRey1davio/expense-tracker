import flask
from flask import Flask, request, render_template

app = Flask(__name__)
expenses = [] #standin database for now 

@app.route("/", methods=["GET"])
def index():
    return "\n".join(expenses)
if __name__ == "__main__":
    app.run(debug=True)