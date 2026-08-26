import sqlite3


def load_transactions():
    # connect to database
    connection = sqlite3.connect("expense_tracker.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM transactions")
    rows_transactions = cursor.fetchall()

    connection.close()

    return rows_transactions

def add_transactions_to_db(description, amount, category):

    connection = sqlite3.connect("expense_tracker.db")
    cursor = connection.cursor()

    # ? is a placeholder for the values we need to add to the db table
    # parameters description, amount and category are tuple of values that SQLite inserts into placeholders
    cursor.execute(
        "INSERT INTO transactions(description, amount, category) VALUES(?, ?, ?)",
        (description, amount, category)
    )

    connection.commit()
    connection.close()

add_transactions_to_db("Costa", 4.50, "Food")
transactions = load_transactions()
print(transactions)