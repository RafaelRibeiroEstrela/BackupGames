import json
import os
import shutil

from implementation.services import GameService
from models.SaveGame import SaveGame
from models.Game import Game
from services.OutputService import *
from services.SaveGameService import *





def main():

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





    #ADD WITH TKINTER
    #minecraft = Game("Minecraft")
    #quake = Game("Quake")
    #addGame(minecraft)
    #addGame(quake)



    #saveGame = addSaveGame(game)

    #outPutGame()

def addGame():
    print("\n!. VOLTAR PARA MENU ANTERIOR")
    name = input("Nome: ")
    if (len(name) == 0 or name.isspace()):
        print("É obrigatório preencher o jogo com o um nome válido")
        addGame()
    elif (name == "!"):
        return

    game = Game()
    game.id = uuid.uuid1()
    game.name = name
    GameService.addGame(game)
    print("game inseted!")

def findGames():
    listObj = GameService.findGames()
    if (len(listObj) == 0):
        print("Não foi encontrado nenhum jogo")
        return

    for index in listObj:
        print(index.toString())

def findGameWithParameters():
    print("\n!. VOLTAR PARA MENU ANTERIOR")
    print("1. BUSCAR POR ID")
    print("2. BUSCAR POR NOME")
    subcomand = input("COMANDO: ")

    if (subcomand == "1"):
        id = input("id: ")
        game = GameService.findGameById(id)
        if (game == None):
            print("Não foi encontrado nenhum jogo")
        else:
            print(game.toString())
    elif (subcomand == "2"):
        name = input("Name: ")
        listObj = GameService.findGameByName(name)
        if (len(listObj) == 0):
            print("Não foi encontrado nenhum jogo")
        else:
            for index in listObj:
                print(index.toString())
    elif (subcomand == "!"):
        return

    findGameWithParameters()

def saveAll():
    print("saveAll")

def saveGame():
    print("saveGame")

def downloadAll():
    print("downloadAll")

def downloadSave():
    print("downloadSave")













if __name__ == '__main__':
    main()

