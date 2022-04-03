
from models.Game import Game
from services.GameService import zipfolder
import json

def main():

    zipfolder("minecraftsave", "C:/Users/grandejogada/AppData/Roaming/.minecraft/saves")


    #game = Game()
    #game.name = "Euro Truck Simulator"
    #game.path = "C:\Users\grandejogada\Documents\Euro Truck Simulator 2"
    #game.bytes = ""

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

