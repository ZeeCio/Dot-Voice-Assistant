import datetime
from engine import DOT

dot = DOT()


def greet_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        dot.say("Good Morning! What Can I do for you ?")
        print("Good Morning! What Can I do for you ?")
    elif 12 <= hour < 18:
        dot.say("Good Afternoon! What Can I do for you ?")
        print("Good Afternoon! What Can I do for you ?")
    else:
        dot.say("Good Evening! What Can I do for you ?")
        print("Good Evening! What Can I do for you ?")