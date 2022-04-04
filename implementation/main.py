import json
import os
import shutil
from models.SaveGame import SaveGame
from models.Game import Game
from services.GameService import *
from services.OutputService import *
from services.SaveGameService import *



def main():

    #ADD WITH TKINTER
    minecraft = Game("Minecraft")
    quake = Game("Quake")
    addGame(minecraft)
    addGame(quake)



    #saveGame = addSaveGame(game)

    outPutGame()

















if __name__ == '__main__':
    main()

