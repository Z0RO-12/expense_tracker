# This contains functions such as add, show, total, search and delete logic
from unicodedata import category

from storage import (

    save_transactions,
)

from database import (
    add_transactions_to_db,
    load_all_db_transactions
)

def add_transaction(transactions):
    description = input("description: ")
    while True:
        try:
            amount = float(input("amount: "))
            if amount <= 0:
                print("invalid amount entered")
                continue
            break

        except ValueError:
            print("invalid value entered")
    category = input("category: ")

    '''transaction = {"description": description,
                    "amount": amount,
                    "category": category}'''

    add_transactions_to_db(description, amount, category)

    '''transactions.append(transaction)
    # save transactions function saves the newly added transactions (RAM)
    # to the SSD memory using files for permanent storage and loading
    save_transactions(transactions)'''


def show_transactions(transactions):
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
            f"{row_transaction[2]} - "
            f"{row_transaction[3]}"
        )

def transactions_total(transactions):
    total = 0

    for transaction in transactions:
        amount = transaction["amount"]
        total += amount

    return total

def search_transactions(transactions):
    # user enter item value to search
    # value is checked through the list of dictionary values
    # if value is found then "match" is printed
    # once matched the transaction amount is also shown on screen

    search_match = []

    search = input("Enter transaction description for search").lower()

    for transaction in transactions:
        if search in transaction["description"].lower():
            search_match.append(transaction)


    return  search_match

def delete_transaction(transactions):

    # choose to delete transaction by index
    # needs to be validated so an index error isn't produced

    for number_it,transaction in enumerate(transactions, start=1):
        print(
            f"{number_it}.{transaction["description"]} - £{transaction["amount"]:.2f}")

    try:
        choice = int(input("Enter number to delete transaction"))


    except ValueError:
        print("Invalid input. Returning to main menu")
        return

    if choice < 1 or choice > len(transactions):
        print ("Invalid transaction number")
        return
        # convert choice to index number
    index = choice - 1
    confirmation = input("Are you sure? Yes(Y) or No(N): ")

    if confirmation.lower() == "y" :
            deleted_transaction = transactions.pop(index)
            print(
                f"Deleted: {deleted_transaction["description"]}" 
                f"- £{deleted_transaction["amount"]:.2f}"
            )
