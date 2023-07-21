import datetime


def welcome():
    hours = datetime.datetime.now().hour
    if hours >= 6 and hours <= 12:
        return "Good morning"
    elif hours >= 12 and hours <= 17:
        return "Good afternoon"
    elif hours >= 17 and hours <= 19:
        return "Good evening"
    else:
        return "Hello"
