import os  # functions for interacting with the operating system
import datetime  # functions to deal with dates, times and time intervals
import random  # generate random numbers
import sys  # allows operating on the interpreter
import webbrowser  # web browser controller
import pyautogui  # Used to programmatically control the mouse & keyboard
import requests  # Make a request to a web page, and print the response text
import winshell  # Windows shell functionality
from pywikihow import search_wikihow  # wikipedia search
import wikipedia  # wikipedia search
from pywhatkit import playonyt  # play YouTube
from dot_ui import Ui_Dot  # PyQt5 User interface class
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from skills.skills import *
from skills.greet import greet_me   # greet me function
from skills.weather import weather_is   # weather function
from skills.joke import jokes  # jokes function
from skills.time_function import time_func  # time function
from skills.date_function import date_func  # date function
from skills.wikipedia import wiki_who_is  # wikipedia function
from skills.computational import computational_intelligence  # calculate wolframalpha function
from skills.wolf_api import wolf  # main wolframalpha function
from engine import DOT


dot = DOT()

# ================================ MEMORY - lists  ====================================#

GREETINGS = ["hello ", "dot", "wake up dot", "you there dot", "ready to work dot", "hey dot",
             "ok dot", "are you there", "how are you"]
GREETINGS_RES = ["always there for you", "i am ready",
                 "what can I do for you", "how can i help you?", "i am online and ready"]

DATE_LIST = ["date", "day", "month", "what's the date", "what date is today", "what day is today"]
OTHERS = ["Alexa", "Hey Siri"]
MAKE_NOTE = ["remember this", "note", "make a note", "take a note"]
QUESTIONS = ["i want to ask", "question", "i have a question", "i am curious about"]
# =======================================================================================================================================================


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        greet_me()
        while True:
            self.command = dot.listen()
            print("command was:", self.command)
            response = ""

            if self.command in GREETINGS:
                response = response + random.choice(GREETINGS_RES)

            elif "your name" in self.command or "who are you" in self.command or "introduce yourself" in self.command:
                response = response + "My name is Dot. I am a Voice Assistant built by " \
                                      "Zlatka Ciorica. I can help you with daily tasks, " \
                                      "such as search online, play favorite songs and many more. "

            elif "Hey Siri" in self.command or "Alexa" in self.command:
                response = response + "hey, honey  \
                        you can call me whatever you want,\
                        but this doesn't mean I will get the job done "

# ------------------------Time and Date --------------------------------------------- #
            elif "time" in self.command:
                response = response + time_func()

            elif self.command in DATE_LIST:
                response = response + date_func()

# ------------------------conditions for Opening different apps---------------------#
            elif "open" in self.command:
                if "word" in self.command:
                    response = response + "Opening Microsoft Word"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "visual studio code" in self.command:
                    response = response + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\Zlatk\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )

                elif "pycharm" in self.command:
                    response = response + "Opening PyCharm"
                    os.startfile(
                        r"C:\Program Files\JetBrains\PyCharm Community Edition 2021.3.2\bin\pycharm64.exe"
                    )

# ---------------------------closing apps-------------------------------------------- #
            elif "close" in self.command:
                if "word" in self.command:
                    response = response + "closing Microsoft Word"
                    os.system("TASKKILL /F /IM word.exe")

                elif "visual studio code" in self.command:
                    response = response + "closing Visual Studio Code"
                    os.system("TASKKILL /F /IM Code.exe")

                elif "pycharm" in self.command:
                    response = response + "closing PyCharm"
                    os.system("TASKKILL /F /IM pycharm64.exe")

# ---------------------------taking notes----------------------------------- #
            elif self.command in MAKE_NOTE:
                dot.say("What should I write ?")
                memory = dot.listen()
                file = open('Notes.txt', 'w')
                dot.say("Should I include the date and time??")
                memory_time = dot.listen()
                if "yes" in memory_time:
                    str_time = datetime.datetime.now().strftime("%H:%M")
                    file.write(str_time)
                    file.write(" --> ")
                    file.write(str(memory))
                    dot.say("Note made successfully with date and time.")
                    print("Note made successfully with date and time.")
                else:
                    file.write("\n")
                    file.write(str(memory))
                    dot.say(" Note made successfully.")
                    print("DOT said: Note made successfully.")

            elif "show note" in self.command or "read note" in self.command:
                dot.say("Reading Notes")
                file = open("Notes.txt", "r")
                notes = file.readlines()
                # for points in data_note:
                print("DOT said:" + str(notes))
                dot.say(notes)

# --------------------------searching online-------------------#
            elif "search" in self.command:
                what_index = self.command.split().index("search")
                search = self.command.split()[what_index + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                response = response + " Searching " + str(search) + " on google"

            elif "google" in self.command:
                what_index = self.command.split().index("google")
                search = self.command.split()[what_index + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search)
                )
                response = response + " Searching " + str(search) + " on google"

            elif "who is" in self.command:
                person = wiki_who_is(text=self.command)
                wiki = wikipedia.summary(person, sentences=2)
                response = response + " " + wiki

            elif "play on youtube" in self.command or "youtube" in self.command:
                song = self.command.replace('play', '')
                response = response + 'playing ' + song
                playonyt(song)

            elif "empty bin" in self.command:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                response = response + "The bin has been emptied"

            elif "play song" in self.command or "play music" in self.command:
                dot.say("Playing song")
                music_directory = r"C:\Users\Zlatk\Music"
                songs = os.listdir(music_directory)
                d = random.choice(songs)
                song = os.path.join(music_directory, d)
                print("DOT said: Playing song")
                os.startfile(song)

            elif "calculate" in self.command:
                response = response + "The answer is " + str(computational_intelligence(text=self.command))

            elif "tell me a joke" in self.command:
                response = response + str(jokes())

            elif "what is the weather in" in self.command:
                response = response + str(weather_is(text=self.command))

            elif "ask" in self.command:
                response = response + "The answer is " + str(wolf(text=self.command))

            elif "news" in self.command:
                url = "https://www.bbc.co.uk/news"
                webbrowser.open(url)
                response = "Here are some headlines from BBC news,Happy reading"

            elif "the price of" in self.command:
                q = self.command.replace("the price of", "")
                query = "https://www.amazon.in/s?k=" + q  # for the keyword
                webbrowser.open(query)

            elif "how to" in self.command:
                try:
                    query = self.command.replace('how to', '')
                    max_results = 1
                    data = search_wikihow(query, max_results)
                    data[0].print()
                    dot.say(data[0].summary)
                except Exception as e:
                    print(e)
                    dot.say('Sorry, I am unable to find the answer for your query.')

            elif "ip address" in self.command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                dot.say(f"Your ip address is {ip}")

            elif "volume up" in self.command:
                pyautogui.press("volumeup")

            elif "volume down" in self.command:
                pyautogui.press("volumedown")

            elif "volume mute" in self.command:
                pyautogui.press("volumemute")

            elif "Goodbye" in self.command or "bye" in self.command or "offline" in self.command:
                dot.say("Goodbye, I'm going to sleep now")
                print("Goodbye, I'm going to sleep now")
                sys.exit(app.exec_())

            dot.say(response)
            print("DOT said: " + response)


start_execution = MainThread()


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Dot()
        self.ui.setupUi(self)
        # self.ui.btn_login.clicked.connect(self.gotologin)
        # self.ui.btn_manual.clicked.connect(self.gotocreate)
        self.ui.btn_start.clicked.connect(self.start_task)
        self.ui.btn_exit.clicked.connect(self.close)

    def start_task(self):
        # --------------------------Play energy.gif -----------------------------------#
        self.ui.movie_energy = QMovie("images/gifs/energy.gif")
        self.ui.lbl_energy.setMovie(self.ui.movie_energy)
        self.ui.movie_energy.start()
        # --------------------------Play loading.gif -----------------------------------#
        self.ui.movie_blue = QMovie("images/gifs/initial.gif")
        self.ui.lbl_blue.setMovie(self.ui.movie_blue)
        self.ui.movie_blue.start()
        start_execution.start()


app = QApplication(sys.argv)
ui = Main()
#widget = QtWidgets.QStackedWidget()
#widget.addWidget(ui)
ui.setFixedHeight(800)
ui.setFixedWidth(1200)
ui.show()
sys.exit(app.exec_())
