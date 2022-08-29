import datetime
from engine import DOT

dot = DOT()


def time_func():
    time_now = datetime.datetime.now()

    if time_now.hour >= 12:
        at_end = "p.m."
        hr = time_now.hour - 12
    else:
        at_end = "a.m."
        hr = time_now.hour

    if time_now.minute < 10:
        minute = "0" + str(time_now.minute)
    else:
        minute = str(time_now.minute)

    return "The current time is " + str(hr) + " and " + minute + "" + at_end + "."

