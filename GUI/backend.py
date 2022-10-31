import interface as frontend
from interface import InterfaceApp as interface
from main import *


def validateState(inputState):
    seen = []
    if len(inputState) != 9 or not inputState.isnumeric():
        return False
    for dig in inputState:
        if dig in seen or dig == '9':
            return False
        seen.append(dig)
    return True


def adjustDigit(dig):
    if dig == '0':
        return ' '
    return dig
