
import uuid

class Game:
    def __init__(self):
        self.id = None
        self.name = None
        self.directory = None

    def convertObjToDict(self):
        dictObj = {
            "id":self.id,
            "name":self.name,
            "directory":self.directory
        }
        return dictObj

    def toString(self):
        print("id = " + self.id + "\n" + "name = " + self.name + "\n" + "directory = " + self.directory + "\n")
