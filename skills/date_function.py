import datetime
import calendar
from engine import DOT

dot = DOT()


def date_func():
    time_now = datetime.datetime.now()
    date = datetime.datetime.today()
    week = calendar.day_name[date.weekday()]
    month = time_now.month
    day = time_now.day
    year = datetime.datetime.now().year
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    ordinals = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th',
                '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th',
                '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th',
                '29th', '30th', '31st']
    # return with subtracting from index, as first index is 0
    return f"Today is {week}, {months[month - 1]} {ordinals[day - 1]} {year}"
