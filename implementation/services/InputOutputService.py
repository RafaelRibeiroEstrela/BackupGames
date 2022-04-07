import json
import os
import sys

from implementation.configs import Variables



#LE UM ARQUIVO JSON
def readJsonFile(dir):
    with open(dir, "r") as inputFile:
        data = json.loads(inputFile.read())
    return data

#ESCREVE UM ARQUIVO JSON
def writeJsonFile(dir, dict):
    with open(dir, "w") as outfile:
        json.dump(dict, outfile)

def verifyExistFiles():
    if not os.path.isdir(Variables.LOCAL_GAMES):
        os.makedirs(Variables.LOCAL_GAMES)
        with open(Variables.LOCAL_GAMES_JSON, "a") as outfile:
            json.dump({"games":[]}, outfile)

    if not os.path.isdir(Variables.LOCAL_GAMES_UPLOAD):
        os.makedirs(Variables.LOCAL_GAMES_UPLOAD)
        with open(Variables.LOCAL_GAMES_JSON_UPLOAD, "a") as outfile:
            json.dump({"savegames": []}, outfile)
