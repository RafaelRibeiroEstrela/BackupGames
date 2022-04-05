
import uuid

class Game:
    def __init__(self):
        self.id = None
        self.name = None

    def convertObjToDict(self):
        dictObj = {
            "id":self.id,
            "name":self.name
        }
        return dictObj

    def toString(self):
        print("id = " + self.id + "\n" + "name = " + self.name + "\n")
