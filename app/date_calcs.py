import datetime


def obtain_date():
    is_valid = False
    while not is_valid:
        user_in = input("Enter the first date to start (Use this format mm/dd/yy: ")
        try:  # strptime throws an exception if the input doesn't match the pattern
            date = datetime.datetime.strptime(user_in, "%m/%d/%y")
            is_valid = True
        except:
            print("Doh, that was the wrong format for a date. :(\n")
    return date
