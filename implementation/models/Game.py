
import uuid

class Game:
    def __init__(self, name):
        self.id = str(uuid.uuid1())
        self.name = name

    def convertObjToDict(self):
        dictObj = {
            "id":self.id,
            "name":self.name
        }
        return dictObj
