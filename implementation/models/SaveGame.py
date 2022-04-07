class SaveGame:
    def __init__(self):
        self.id = None
        self.saveDate = None
        self.arrayBytes = None
        self.game = None

    def convertObjToDict(self):
        dictObj = {
            "id":self.id,
            "saveData":self.saveDate,
            "arrayBytes":self.arrayBytes,
            "game":self.game
        }
        return dictObj