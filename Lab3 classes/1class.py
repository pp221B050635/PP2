class MyString():
    def __init__(self):
        self.s=""

    def getstring(self):
        self.s=input()

    def printstring(self):
        print(self.s.upper())

s=MyString()
s.getstring()
s.printstring()
