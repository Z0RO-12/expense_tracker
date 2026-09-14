import sqlite3


def load_all_db_transactions():
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



def show_transactions_total():
    # SUM totals all values under amount
    # fetchone allows for only one value to be returned for formatting

    connection = sqlite3.connect("expense_tracker.db")
    cursor = connection.cursor()

    cursor.execute("SELECT SUM(amount) FROM transactions")
    total_of_transactions = cursor.fetchone()

    connection.close()
    return total_of_transactions[0]




def search_transactions_in_db(search_pattern):
    connection = sqlite3.connect("expense_tracker.db")
    cursor = connection.cursor()
    # this allows for user to input description or category and for program to search for similar values


    cursor.execute(
        "SELECT * FROM transactions WHERE description LIKE ? OR category LIKE ?",
        (search_pattern,search_pattern)
    )

    search_results = cursor.fetchall()
    connection.close()

    return search_results

def delete_transactions_from_db(transaction_id):
    # delete using placeholder and a variable called transaction_id to use delete
    # this is better than deleting using indexing or place values
    connection = sqlite3.connect("expense_tracker.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM transactions WHERE id = ?",
        (transaction_id,)
    )
    connection.commit()
    connection.close()
