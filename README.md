# Dot-Voice-Assistant
Python based project for voice assistant

MANUAL:


#	Greet user
Commands from list GREETINGS triggers random phrase from GREETINGS_RES.
GREETINGS = ["hello ", "dot", "wake up dot", "you there dot", "ready to work dot", "hey dot",
             "ok dot", "are you there", "how are you"]
GREETINGS_RES = ["always there for you", "i am ready",
                 "what can I do for you", "how can i help you?", "i am online and ready"]


# Introduction 
Command:   "your name" or "who are you"
Triggers introduction 

# 	Tell current time 
Command  : Any question containing phrase “time”

# 	and date
Command :
Any question containing phrase  from list:
DATE_LIST = ["date", "day", "month", "what's the date", "what date is today", "what day is today"]

# 	Launch applications/software
Command:
- open + ……………..(target phrase) shown bellow 
               - word, visual studio code, pycharm

# 	Tells about weather of any city
Command:
What is the weather in…………………… + (target phrase)

# 	Tells about any person (via Wikipedia)
Command:
Who is …………. + (target phrase)

# 	Can search anything on Google
Command:
-	Google ……………… + (target phrase)
-	Search ……………… + (target phrase)

# 	Can play any song on YouTube
Command:
Containing “play on youtube" or "youtube" in command triggers the task

# 	Calculate any mathematical expression
Command:
Calculate + ………….(target phrase)

# 	Answer any generic question (via Wolframalpha)
Command containing “ask” takes to next step 
Takes Input = any question

# 	Take important note in notepad
Command from list :
MAKE_NOTE = ["remember this", "note", "make a note", "take a note"]

# 	Reads and shows notes:
Command containing “show note” or “read note”

# 	Tells a random joke
Command containing “tell me a joke”

# 	Check product prices on Amazon
Command containing "find the price of “…………+(target phrase)

# 	Tells your IP address
Command containing “ip address”

# 	Finds latest news the news
Command containing “news” 

# 	Play songs from local folder
       Command “play song”, “play music” 

# 	Give tips
Command containing “how to”

# 	Controls volume of pc
Command containing “volume up, volume down or volume mute”

# 	Empties bin
Command containing “empty bin”


