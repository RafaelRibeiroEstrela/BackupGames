import json
import os
import sys

from implementation.configs.Variables import getLocalDocuments, GAMES_FILE_JSON, GAMES_DICT_IN_MEMORY
from implementation.exceptions.AppException import AppException


def outPutGame():
    verifyExistJson()
    dictFromJson = readJsonFile()
    for gameDict in GAMES_DICT_IN_MEMORY:
        verifiyExistGame(gameDict["name"], dictFromJson["games"])
        dictFromJson["games"].append(gameDict)
    writeJsonFile(dictFromJson)
    GAMES_DICT_IN_MEMORY.clear()

#VERIFICA SE JÁ EXISTE UM JOGO NO JSON FILE
def verifiyExistGame(name, listDict):
    if (len(listDict) > 0):
        for dict in listDict:
            if (dict["name"] == name):
                raise AppException("Já existe um jogo com o nome " + name)

#VERIFICA SE JÁ EXISTE UM JSON FILE
def verifyExistJson():
    emptyDict = {
        "games":[]
    }
    if not (os.path.isfile(getLocalDocuments() + GAMES_FILE_JSON)):
        with open(getLocalDocuments() + GAMES_FILE_JSON, "w") as outfile:
            json.dump(emptyDict, outfile)

#LE UM ARQUIVO JSON
def readJsonFile():
    with open(getLocalDocuments() + GAMES_FILE_JSON, "r") as inputFile:
        data = json.loads(inputFile.read())

    return data

#ESCREVE UM ARQUIVO JSON
def writeJsonFile(dictObj):
    with open(getLocalDocuments() + GAMES_FILE_JSON, "w") as outfile:
        json.dump(dictObj, outfile)
