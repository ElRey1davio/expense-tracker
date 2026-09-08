import flask
import requests
from flask import Flask, request, render_template

app = Flask(__name__)
expenses = [] #standin database for now 

@app.route("/", methods=["GET"])
def index():
    lines = []
    for expense in expenses:
        lines.append(f" {expense['id']}:  {expense['description']} - ${expense['amount']}")
    return "\n".join(lines)

@app.route('/convert/<from_currency>/<to_currency>')
def convert(from_currency, to_currency):
    response = requests.get(f'https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}')
    data = response.json()
    if "rates" not in data:
        return f"Sorry, could'nt convert {from_currency} to {to_currency} ."
    old_currency = data["base"]
    new_currency= data["rates"][to_currency]
    return f"1 {old_currency} = {new_currency} {to_currency}"

 
@app.route('/add-expense' , methods=['POST'])
def add_expense():
    data = request.json
    amount = data['amount']
    description = data['description']
    id_prod = len(expenses)
    new_expense = {"id": id_prod , "description": description, "amount": amount}
    expenses.append(new_expense)
    return f"Received expense:{id_prod}. {description} - ${amount}"
     
 
@app.route('/delete-expense/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    global expenses
    expenses = [e for e in expenses if e['id'] != expense_id]
    return f"Deleted expense {expense_id}"

@app.route('/add-expense-form' , methods = ['GET'])
def add_expense_form():
    return render_template('add_expense.html')


@app.route('/submit-expense' , methods = ['POST'])
def submit_expense():
    description = request.form["description"]
    amount = float(request.form["amount"])
    id_prod = len(expenses)
    new_expense = {"id":id_prod , "description":description , "amount":amount}
    expenses.append(new_expense)
    return f"Expense {description} has been added"


@app.route('/update-expense/<int:expense_id>' , methods = ["PUT"])
def update_expense(expense_id):
    global expenses
    for expense in expenses:
        if expense["id"] == expense_id:
            data = request.json
            expense["description"] = data["description"] 
            expense["amount"]= data["amount"]

    return f"Data updated"
        
if __name__ == "__main__":
    app.run(debug=True)
    