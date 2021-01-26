import datetime

def obtain_date():
    is_valid=False
    while not is_valid:
        user_in = input("Type Date mm/dd/yy: ")
        try: # strptime throws an exception if the input doesn't match the pattern
            d = datetime.datetime.strptime(user_in, "%m/%d/%y")
            is_valid=True
        except:
            print("Doh, try again!\n")
    return d