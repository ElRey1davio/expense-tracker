import flask
import requests
from flask import Flask, request, render_template

app = Flask(__name__)
expenses = [] #standin database for now 

@app.route("/", methods=["GET"])
def index():
    return "\n".join(expenses)

@app.route('/convert/<from_currency>/<to_currency>')
def convert(from_currency, to_currency):
    response = requests.get(f'https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}')
    data = response.json()
    if "rates" not in data:
        return f"Sorry, could'nt convert {from_currency} to {to_currency} ."
    old_currency = data["base"]
    new_currency= data["rates"][to_currency]
    return f"1 {old_currency} = {new_currency} {to_currency}"
    
    
if __name__ == "__main__":
    app.run(debug=True)
    