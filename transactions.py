
from database import (
    add_transactions_to_db,
    load_all_db_transactions,
    show_transactions_total,
    search_transactions_in_db,
    delete_transactions_from_db,
)

def add_transaction():
    description = input("description: ")
    # catches invalid entries
    while True:
        try:
            # turns amount into float input
            amount = float(input("amount: "))
            if amount <= 0:
                print("invalid amount entered")
                continue
            break

        except ValueError:
            print("invalid value entered")
    category = input("category: ")

    add_transactions_to_db(description, amount, category)


def show_transactions():
    # number transaction in a loop by each description and amount
    # print each transaction that is numbered

    transactions = load_all_db_transactions()


    if not transactions:
        print("No transactions found")
        return

    for row_transaction in transactions:
        print(
            f"{row_transaction[0]}. "
            f"{row_transaction[1]} - "
            f"{row_transaction[2]:.2f} - "
            f"{row_transaction[3]}"
        )

def transactions_total():


    total = show_transactions_total()
    if total is None :
        total = 0

    print(f"Total of transactions is £{total:.2f}")


def search_transactions():

    search = input("Enter transaction description or category for search")
    search_pattern = f"%{search}%"
    search_results = search_transactions_in_db(search_pattern)

    if not search_results:
        print("No matching transactions found.")
    else:
        for transaction in search_results:
            print(f"{transaction[0]}. {transaction[1]} - £{transaction[2]:.2f} - {transaction[3]}")


def delete_transaction():


    # choose to delete transaction by id
    id_found = False
    # present id and all transaction for user to see before deleting
    transactions = load_all_db_transactions()
    if not transactions:
        print("No transactions found")
        return

    for row_transaction in transactions:
        print(
            f"{row_transaction[0]}. "
            f"{row_transaction[1]} - "
            f"£{row_transaction[2]:.2f} - "
            f"{row_transaction[3]}"
        )
    # catches value error meaning entries that are not integers
    try:
        transaction_id = int(input("Enter id to delete transaction"))

    except ValueError:
        print("Invalid input. Returning to main menu")
        return
    # if id is found rest of the logic continues
    for row_transaction in transactions:
        if transaction_id == row_transaction[0]:
            id_found = True
            break
    # if id not found then remains false and stops function back to main menu
    if not id_found :
        print("Transaction id not found")
        return

    confirmation = input("Are you sure? Yes(Y) or No(N): ")

    if confirmation.lower() == "y":
        delete_transactions_from_db(transaction_id)
    else:
        print("Returning to menu")
        return

