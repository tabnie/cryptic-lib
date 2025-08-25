from random import shuffle, randint
from string import ascii_letters, digits, punctuation

class Key():
    def __init__(self, name="", secret=""):
        self.chars = list(" "+ascii_letters+digits+punctuation)
        self.names = ["John", "Burger", "Pizza", "Secret", "Box", "Script", "Cryptic", "Garganza", "Soluat", "Bokatio", "Bagino"]
        self.name = name
        self.secret = secret

    def randomize(self):
        self.name += self.names[randint(0, len(self.names)-1)]
        match randint(0, 1):
            case 0:
                self.name += self.names[randint(0, len(self.names)-1)]
            case 1:
                pass
        self.secret = self.chars.copy()
        shuffle(self.secret)
        print(self.secret)

class substitute():
    def __init__(self, key, text):
        self.chars = list(" "+ascii_letters+digits+punctuation)
        self.key = key
        self.text = text

key = Key()
key.randomize()
