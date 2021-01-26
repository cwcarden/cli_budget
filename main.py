import csv
import sys
from expense import add_expense
from income import add_income


def welcome():
    while True:
        print("\n                    Welcome to CLI Budget\n")
        print("Select an Option\n")
        selection = input("(E) Add a New Expense\n (I) Add a new Income\n(V) View current Budget\n(EB) Edit Budget\n(L or anything else) To Exit\n").upper()
        if selection == 'E':
            add_expense()

        elif selection == 'I':
            add_income()

        elif selection == 'V':
            print(selection)

        elif selection == 'EB':
            print(selection)

        else:
            print("    Goodbye   ")
            sys.exit()


def create_csv():
    with open('budget.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Name", "Category", "Occurrence", "Amount", "Start_Date"])
        file.close()









if __name__ == '__main__':
    while True:
        welcome()
