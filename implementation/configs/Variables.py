
import os

from implementation.exceptions.AppException import AppException


def getLocalDocuments():
    LOCAL_DOCUMENTS = os.getenv("LOCAL_DOCUMENTS")
    if (LOCAL_DOCUMENTS == None):
        raise AppException("Não foi encontrado a variavel de ambiente ou valor LOCAL_DOCUMENTS")

    return LOCAL_DOCUMENTS

GAMES_FILE_JSON = "games_json.json"

GAMES_DICT_IN_MEMORY = []




