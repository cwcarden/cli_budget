import csv
import sys
from expense import add_expense
from income import add_income
from app import create_budget


def welcome():
    while True:
        print("\n                    Welcome to CLI Budget\n")
        print("Select an Option\n")
        selection = input("(E) Add a New Expense\n(I) Add a New Income\n(V) View Budget\n(B) Edit Budget\n(A or Ctrl "
                          "C) To Abort\n").upper()
        if selection = 'N'
            create_new_budget()

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
    with open('app.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Name", "Category", "Occurrence", "Amount", "Start_Date"])
        file.close()









if __name__ == '__main__':
    while True:
        welcome()
