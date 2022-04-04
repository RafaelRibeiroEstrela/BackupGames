import datetime
import shutil
import uuid

from implementation.models.SaveGame import SaveGame


def addSaveGame(game):
    saveGame = SaveGame()
    saveGame.id = uuid.uuid1()
    saveGame.saveDate = datetime.date.today()
    saveGame.arrayBytes = getArrayBytes(game)
    saveGame.game = game
    return saveGame


def getArrayBytes(game):
    shutil.make_archive(game.name + " - save", "zip", game.directory)

    with open("Minecraft - save.zip", 'rb') as file_data:
        bytesContent = file_data.read()

    return bytesContent