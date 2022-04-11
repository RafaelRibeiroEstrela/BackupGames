import datetime
import os
import sys
import uuid
import zipfile
from zipfile import ZipFile




from client.configs import Variables
from client.services import GameService, InputOutputService


def saveAll():
    dictGames = GameService.findGames()
    dictSave = InputOutputService.readJsonFile(Variables.LOCAL_GAMES_JSON_UPLOAD)
    if (len(dictGames["games"]) == 0):
        print("Não foi encontrado nenhum backup de jogo")
        return
    for index in dictGames["games"]:
        saveGame = {
            "id":str(uuid.uuid1()),
            "saveData":str(datetime.date.today()),
            "bytes":str(getArrayBytes(index["directory"])),
            "game":index
        }
        dictSave["games"].append(saveGame)
    InputOutputService.writeJsonFile(Variables.LOCAL_GAMES_JSON_UPLOAD, dictSave)
    os.remove(Variables.LOCAL_GAMES_UPLOAD + r"\temp.zip")
    print("game saved")

def getArrayBytes(dir):
    with zipfile.ZipFile(Variables.LOCAL_GAMES_UPLOAD + r"\temp.zip", mode='w') as zipf:
        len_dir_path = len(dir)
        for root, _, files in os.walk(dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])

    with open(Variables.LOCAL_GAMES_UPLOAD + r"\temp.zip", 'rb') as file_data:
        bytesContent = file_data.read()

    return bytesContent




