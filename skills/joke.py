import pyjokes
from engine import DOT

dot = DOT()


def jokes():
    return pyjokes.get_joke()