import json
import shutil
from models.SaveGame import SaveGame
from models.Game import Game
import datetime

def main():

    game = Game()
    game.name = "Minecraft"
    game.directory = "C:/Users/rafa_/AppData/Roaming/.minecraft/saves"

    save = SaveGame()
    save.saveDate = datetime.date.today()

    shutil.make_archive(game.name + " - save", "zip", game.directory)

    with open("Minecraft - save.zip", 'rb') as file_data:
        bytes_content =  file_data.read()

    save.arrayBytes = bytes_content

    gameJson = game.convertObjToDict()

    print(gameJson)













if __name__ == '__main__':
    main()

