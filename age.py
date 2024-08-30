import datetime


def calc_age(date):
    try:
        day, month, year = map(int, date.split("-"))
        dob = datetime.datetime(year, month, day)
        today = datetime.date.today()
        age = today.year - dob.year
        if today.month < dob.month:
            age -= 1
        return age
    except:
        return "Your date format was incorrect. Please try again."


date_of_birth = input(
    "Please input your date of birth in the following format:\n30-06-2001 for the 30th of June, 2001.\n")
print(calc_age(date_of_birth))
