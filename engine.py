import pyttsx3
import speech_recognition as sr


class DOT:

    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        print("Listening...")

        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        with self.m as source:
            print("Listening...")
            self.r.adjust_for_ambient_noise(source, duration=1)
            self.r.pause_threshold = 1
            audio = self.r.listen(source)
            print("got it")
            phrase = ""
            try:
                phrase = self.r.recognize_google(audio, show_all=False, language="en_UK")
                print("Recognizing...")
                sentence = "Got it, you said" + phrase
                self.say(sentence)

            except Exception as e:
                print("Sorry, didn't catch that", e)
                self.say("Sorry didn't catch that")

        print("You Said: ", phrase)
        return phrase.lower()
