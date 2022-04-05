import json
import os
import sys

from implementation.configs.Variables import getLocalDocuments, GAMES_FILE_JSON, GAMES_DICT_IN_MEMORY
from implementation.exceptions.AppException import AppException


def outPutGame():

    print("...verify if exist json file in your system")
    verifyExistJson()
    dictFromJson = readJsonFile()

    print("...verify if exist game in json file")
    for gameDict in GAMES_DICT_IN_MEMORY:
        if not (verifiyExistGame(gameDict["name"], dictFromJson["games"])):
            continue
        dictFromJson["games"].append(gameDict)

    print("...wrinting game in json file")
    writeJsonFile(dictFromJson)
    GAMES_DICT_IN_MEMORY.clear()

#VERIFICA SE JÁ EXISTE UM JOGO NO JSON FILE
def verifiyExistGame(name, listDict):
    if (len(listDict) > 0):
        for dict in listDict:
            if (dict["name"] == name):
                return False
                #raise AppException("Já existe um jogo com o nome " + name)

#VERIFICA SE JÁ EXISTE UM JSON FILE
def verifyExistJson():
    emptyDict = {
        "games":[]
    }
    if not (os.path.isfile(getLocalDocuments() + GAMES_FILE_JSON)):
        print("...creating a json file")
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
