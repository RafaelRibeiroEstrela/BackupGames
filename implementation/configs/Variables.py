import json
import os
from enum import Enum

from implementation.exceptions.AppException import AppException

LOCAL_GAMES = os.path.expanduser("~") + r"\BackupGames\Local"
LOCAL_GAMES_UPLOAD = os.path.expanduser("~") + r"\BackupGames\Upload"


LOCAL_GAMES_JSON = os.path.expanduser("~") + r"\BackupGames\Local\LocalGamesJson.json"
LOCAL_GAMES_JSON_UPLOAD = os.path.expanduser("~") + r"\BackupGames\Upload\LocalGamesJsonUpload.json"

class Game(Enum):
    MINECRAFT = "Minecraft"
    CALL_OF_DUTY = "Call of Duty"
    FIFA = "FIFA",
    NEED_FOR_SPEED = "Need For Speed"






