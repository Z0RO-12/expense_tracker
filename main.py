from storage import (
    load_transactions,
    save_transactions,
)

from transactions import (
    add_transaction,
    show_transactions,
    transactions_total,
    search_transactions,
    delete_transaction,
)
# calls upon functions built from other files
def main_menu(transactions):
    # main menu for the whole program to run through
    while True:
        try:
            # try/except for ValueError
            options = int(input("------ Expense Tracker ------"
                  "\n 1. Add transaction"
                  "\n 2. Show transactions"
                  "\n 3. Show total"
                  "\n 4. Search transactions"
                  "\n 5. Delete transactions"
                  "\n 6. Exit\n"      ))

        except ValueError:
            print("Enter valid input")
            continue

        if options == 1:
            # ask for description and amount of item
            # add item into a dictionary that describes item
            # add transaction dictionary into list

            add_transaction(transactions)



        elif options == 2:
            #show list: transactions
            show_transactions(transactions)

        elif options == 3:
            # go through the list and identify the value of each item
            # add the values together
            # print the total of values

            total = transactions_total(transactions)
            print(f"Total spent: ${total:.2f}")

        elif options == 4:
            # search through transactions for match
            # if no transactions found then return error message and return to menu
            matches = search_transactions(transactions)

            if matches:
                for number_it, transaction in enumerate(matches, start=1):
                    print(
                        f"{number_it}.{transaction["description"]} - £{transaction["amount"]:.2f}"
                    )
            else:
                print("No transactions found")

        elif options == 5:
            # delete transactions
            # if empty or no transactions return error message

            if not transactions:
                print("No transactions to delete")
                continue
            else:
                delete_transaction(transactions)

        elif options == 6:
            # deals with valid integer but invalid choice
            save_transactions(transactions)
            break

        else:
            print("Choose option from 1 to 6")




if __name__ == "__main__":
    transactions = load_transactions()
    main_menu(transactions)







