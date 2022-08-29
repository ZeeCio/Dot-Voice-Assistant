import psutil
from engine import DOT

dot = DOT()


def cpu():
    usage = str(psutil.cpu_percent())
    battery = str(psutil.sensors_battery())
    return f'CPU is at' + usage \
           + "Battery is at" + battery


def short_talk():
    try:
        dot.say("I am fine. Thanks for asking")
        dot.say("How are you")
        answer = dot.listen()
        if answer in ["good", "fine", "awesome", "all good"]:
            dot.say("It's good to know that you are fine")
        elif answer in ["not good", "i am not feeling", "i am ill"]:
            dot.say("I hope you get well soon.")
    except Exception as error:
        print(error)

