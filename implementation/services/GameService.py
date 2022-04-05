
from implementation.configs.Variables import GAMES_DICT_IN_MEMORY
from implementation.models.Game import Game
from implementation.services.OutputService import readJsonFile, outPutGame


def addGame(game):
    GAMES_DICT_IN_MEMORY.append(game.convertObjToDict())
    print("...game inserted in app memory")
    outPutGame()


def findGames():
    dictObj = readJsonFile()
    listObj = []
    for index in dictObj["games"]:
        game = Game()
        game.id = index["id"]
        game.name = index["name"]
        listObj.append(game)
    return listObj

def findGameById(id):
    listObj = findGames()
    for index in listObj:
        if (index.id == id):
            return index

def findGameByName(name):
    listObj = findGames()
    listResults = []
    for index in listObj:
        if name.upper()  in index.name.upper():
            listResults.append(index)

    return listResults



