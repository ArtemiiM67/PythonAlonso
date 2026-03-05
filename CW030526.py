class Minion:
    #define __init __ method
    def __init__(self, theName, theHeight, theEyes, theRage):
        #initialize features here
        self.color = "yellow"
        self.name = theName
        self.height = theHeight
        self.eyes = theEyes
        
minion1 = Minion("Steven", 2.5)
print(minion1.name, minion1.height)
        