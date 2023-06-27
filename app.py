from flask import Flask, redirect, request, jsonify, render_template, url_for

app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100, 'account': 'Checking'},
    {'id': 2, 'date': '2023-06-02', 'amount': 200, 'account': 'Savings'},
    {'id': 3, 'date': '2023-06-03', 'amount': 300, 'account': 'Investment'}
]

# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation: Display add transaction form
@app.route("/add", methods=["GET"])
def add_transaction_form():
    return render_template("form.html")

# Create operation: Add new transaction
@app.route("/add", methods=["POST"])
def add_transaction():
    date = request.form.get("date")
    amount = float(request.form.get("amount"))
    account = request.form.get("account")

    # Generate a unique ID for the new transaction
    new_id = len(transactions) + 1

    # Create the new transaction object
    new_transaction = {
        'id': new_id,
        'date': date,
        'amount': amount,
        'account': account
    }

    # Add the new transaction to the list
    transactions.append(new_transaction)

    # Redirect to the transactions list page
    return redirect(url_for("get_transactions"))

# Update operation: Display edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET"])
def edit_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            return render_template("edit.html", transaction=transaction)

    # Transaction not found
    return "Transaction not found"

# Update operation: Update an existing transaction
@app.route("/update/<int:transaction_id>", methods=["POST"])
def update_transaction(transaction_id):
    date = request.form.get("date")
    amount = float(request.form.get("amount"))
    account = request.form.get("account")

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transaction['date'] = date
            transaction['amount'] = amount
            transaction['account'] = account
            break

    # Redirect to the transactions list page
    return redirect(url_for("get_transactions"))

# Delete operation: Delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break

    # Redirect to the transactions list page
    return redirect(url_for("get_transactions"))

if __name__ == "__main__":
    app.run(debug=True)
