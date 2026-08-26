# This file contains save/load JSON functions
import json
from json import JSONDecodeError

# program starts running and loaded transactions is imported from json format to python list format
# transactions is empty list awaiting values to be placed into it


def load_transactions():
    # opens file as read to export transactions into python format (list)
    try:
        with open("transactions_list.json", "r") as file:
            transactions = json.load(file)
            # .load() allows for the process of json to python format to happen

        return transactions

    except FileNotFoundError:
        print("Save file not found ")
        return []

    except json.JSONDecodeError :
        print("Save file contains invalid json")
        return []


def save_transactions(transactions):
    # data goes into the file
    with open("transactions_list.json", "w") as file:
        json.dump(transactions, file)

