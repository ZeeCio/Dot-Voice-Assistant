import wolframalpha  # API - expert-level answers using Wolfram's algorithms, knowledgebase and AI technology
from engine import DOT

dot = DOT()

APP_ID = "4YJQ2V-R69HH74AWK"


def computational_intelligence(text: object) -> object:
    try:
        client = wolframalpha.Client(APP_ID)
        answer = client.query(text)
        answer = next(answer.results).text
        return answer
    except Exception as error:
        dot.say("Sorry , I couldn't fetch your question's answer. Please try again ")
        print(error)
        return None
