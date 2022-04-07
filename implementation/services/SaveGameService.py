import datetime
import shutil
import uuid

from implementation.models.SaveGame import SaveGame
from implementation.services import GameService


def saveAll():

    listObj = GameService.findGames()
    for index in listObj:
        getArrayBytes(index)


def addSaveGame(game):
    saveGame = SaveGame()
    saveGame.id = uuid.uuid1()
    saveGame.saveDate = datetime.date.today()
    saveGame.arrayBytes = getArrayBytes(game)
    saveGame.game = game
    return saveGame


def getArrayBytes(gameDict):
    shutil.make_archive(base_name=gameDict["name"], format="zip", root_dir=gameDict["directory"])
    shutil.make_archive()

    with open("Minecraft - save.zip", 'rb') as file_data:
        bytesContent = file_data.read()

    return bytesContent