import sys
import uuid

from implementation.configs.Variables import GAMES_DICT_IN_MEMORY
from implementation.models.Game import Game


#retorna um
def addGame(game):
    GAMES_DICT_IN_MEMORY.append(game.convertObjToDict())

def removeGame(id):
    pass