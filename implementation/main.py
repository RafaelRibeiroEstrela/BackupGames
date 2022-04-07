

from implementation.configs.Variables import Game
from implementation.services import InputOutputService, SaveGameService
from services.SaveGameService import *
from tkinter import filedialog
from tkinter import *





def main():

    InputOutputService.verifyExistFiles()

    while(True):
        print(".................MENU.................\n\n")
        print("1. ADICIONAR JOGO")
        print("2. BUSCAR TODOS OS JOGOS")
        print("3. BUSCAR JOGO ESPECÍFICO")
        print("4. SALVAR TODOS OS SAVES")
        print("5. SALVAR SAVE ESPECÍFICO")
        print("6. BAIXAR TODOS OS SAVES")
        print("7. BAIXAR SAVE ESPECÍFICO")
        print("0. SAIR DO PROGRAMA")

        command = input("COMANDO: ")
        if (command == "1"):
            addGame()
        elif (command == "2"):
            findGames()
        elif (command == "3"):
            findGameWithParameters()
        elif (command == "4"):
            saveAll()
        elif (command == "5"):
            saveGame()
        elif (command == "6"):
            downloadAll()
        elif (command == "7"):
            downloadSave()
        elif (command == "0"):
            break

    print("APP ENCERRADO")

def addGame():
    print("\n!. VOLTAR PARA MENU ANTERIOR")
    name = Game.NEED_FOR_SPEED.value
    directory = input("Diretorio: ")
    game = {
        "id":str(uuid.uuid1()),
        "name":name,
        "directory":directory
    }
    GameService.addGame(game)
    print("game inseted!")

def findGames():
    print(GameService.findGames())

def findGameWithParameters():
    print("\n!. VOLTAR PARA MENU ANTERIOR")
    print("1. BUSCAR POR ID")
    print("2. BUSCAR POR NOME")
    subcomand = input("COMANDO: ")

    if (subcomand == "1"):
        id = input("id: ")
        print(GameService.findGameById(id))

    elif (subcomand == "2"):
        name = input("Name: ")
        print(GameService.findGameByName(name))

    elif (subcomand == "!"):
        return

    findGameWithParameters()

def saveAll():
    SaveGameService.getArrayBytes("C:/Users/rafaelestrela/Pictures")

def saveGame():
    print("saveGame")

def downloadAll():
    print("downloadAll")

def downloadSave():
    print("downloadSave")


def verifyEntry(name):
    if (len(name) == 0 or name.isspace()):
        print("Não é aceito espaços em branco")
        addGame()
    elif (name == "!"):
        return










if __name__ == '__main__':
    main()

