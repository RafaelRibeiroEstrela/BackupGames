from client.configs import Variables
from client.services import InputOutputService


def addGame(game):
    dict = InputOutputService.readJsonFile(Variables.LOCAL_GAMES_JSON)
    search = verifyExistGame(game["name"], dict)
    if search == None:
        dict["games"].append(game)
    InputOutputService.writeJsonFile(Variables.LOCAL_GAMES_JSON, dict)
    print("game inseted!")

def findGames():
    return InputOutputService.readJsonFile(Variables.LOCAL_GAMES_JSON)


def findGameById(id):
    dict = findGames()
    if (len(dict["games"]) > 0):
        for index in dict["games"]:
            if (index["id"] == id):
                return index

def findGameByName(name):
    dict = findGames()
    if (len(dict["games"]) > 0):
        listResults = []
        for index in dict["games"]:
            if name.upper() in index["name"].upper():
                listResults.append(index)

    return listResults

#VERIFICA SE JÁ EXISTE UM JOGO NO JSON FILE
def verifyExistGame(name, dict):
    if len(dict["games"]) > 0:
        for index in dict["games"]:
            if index["name"] == name:
                return index

