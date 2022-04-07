import datetime
import os
import shutil
import uuid
import zipfile

from implementation.configs import Variables
from implementation.models.SaveGame import SaveGame
from implementation.services import GameService


def saveAll():
    dict = GameService.findGames()
    if (dict["games"] == 0):
        print("Não foi encontrado nenhum backup de jogo")
        return
    list = []
    for index in dict["games"]:
        saveGame = {
            "id":str(uuid.uuid1()),
            "saveData":datetime.date.today()
        }



def addSaveGame(game):
    saveGame = SaveGame()
    saveGame.id = uuid.uuid1()
    saveGame.saveDate = datetime.date.today()
    saveGame.arrayBytes = getArrayBytes(game)
    saveGame.game = game
    return saveGame


def getArrayBytes(dir):
    print("implementar")
