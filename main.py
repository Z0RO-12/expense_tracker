from transactions import (
    add_transaction,
    show_transactions,
    transactions_total,
    search_transactions,
    delete_transaction,
)

# calls upon functions built from other files
def main_menu():
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

            add_transaction()



        elif options == 2:
            #show list: transactions
            show_transactions()

        elif options == 3:
            # print value from transactions.py

            transactions_total()

        elif options == 4:
            # search through transactions for match
            # if no transactions found then return error message and return to menu
            search_transactions()




        elif options == 5:
            # delete transactions
            delete_transaction()

        elif options == 6:
            # deals with valid integer but invalid choice
            print("Exiting expense tracker")
            break

        else:
            print("Choose option from 1 to 6")




if __name__ == "__main__":
    main_menu()







