


class Game:
    def __init__(self):
        self.name = None
        self.directory = None

    def convertObjToDict(self):
        dictObj = {
            "name":self.name,
            "directory":self.directory
        }
        return dictObj
