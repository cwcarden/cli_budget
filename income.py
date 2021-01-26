import csv
from date_calcs import obtain_date

def add_income():
    income_name = input("Please enter the income source name: ").upper()
    income_category = input("Please enter an income category name: ").upper()
    income_occurence = input("Is this a (w)weekly, (b)biweekly, or (m)monthly reoccurring income?").upper()

    if income_occurence == 'W':
        income_occurence = 'WEEKLY'
    elif income_occurence == 'B':
        income_occurence = 'BIWEEKLY'
    elif income_occurence == 'M':
        income_occurence = 'MONTHLY'
    elif income_occurence == 'A':
        income_occurence = 'ANNUALLY'

    income_amount = float(input("Please enter the income amount: "))
    income_list = ["Income", income_name, income_category, income_occurence, income_amount, obtain_date()]

    with open('budget.csv', 'a') as file:
        writer_object = csv.writer(file)
        writer_object.writerow(income_list)
        file.close()

    print(f"Income {income_name} has been added to the {income_category} category .\n")
