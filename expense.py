import csv
from date_calcs import obtain_date

def add_expense():
    expense_name = input("Please enter the expense name: ").upper()
    expense_category = input("Please enter an expense category: ").upper()
    expense_occurence = input("Is this a (w)weekly, (b)biweekly, or (m)monthly reoccurring expense?").upper()

    if expense_occurence == 'W':
        expense_occurence = 'WEEKLY'
    elif expense_occurence == 'B':
        expense_occurence = 'BIWEEKLY'
    elif expense_occurence == 'M':
        expense_occurence = 'MONTHLY'
    elif expense_occurence == 'A':
        expense_occurence = 'ANNUALLY'

    expense_amount = float(input("Please enter the expense amount: "))

    expense_list = ["Expense", expense_name, expense_category, expense_occurence, expense_amount, obtain_date()]

    with open('budget.csv', 'a') as file:
        writer_object = csv.writer(file)
        writer_object.writerow(expense_list)
        file.close()

    print(f"\n\033[96m {expense_occurence.title()} expense {expense_name} \n has been added to the {expense_category} category.\n")

def create_expense_category():
    # Todo: create function that creates a list of expense categories adds them to the csv or db.
