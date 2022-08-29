import wolframalpha  # API - expert-level answers using Wolfram's algorithms, knowledgebase and AI technology
from engine import DOT

dot = DOT()

APP_ID = "4YJQ2V-R69HH74AWK"


def wolf(text):
    try:
        dot.say("I can answer to computational and geographical questions "
                "and what question do you want to ask now")
        print("I can answer to computational and geographical questions and many more." 
              "What question do you want to ask now")
        question = dot.listen()
        client = wolframalpha.Client(APP_ID)
        response = client.query(question)
        answer = next(response.results).text
        return answer
    except Exception as error:
        dot.say("Sorry , I couldn't fetch your question's answer. Please try again ")
        print(error)
        return None
