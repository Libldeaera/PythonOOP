class staff(object):
    firstName = " "
    familyName = " "

    def __init__(self, firstName, familyName):
        self.firstName = firstName
        self.lastName = familyName

class Sta(staff):
    levelOfExcellence = 0

    def __init__(self, firstName, familyName, levelOfExcellence):
        self.levelOfExcellence = levelOfExcellence
        staff.__init__(self, firstName, familyName)

    def toString(self):
        return "{}:{}has an level of excellence {}".format(self.firstName, self.familyName, self.levelOfExcellence)

characterX = Sta("X", "xxx", 100)
characterY = Sta("Y", "yyy", 1000)

print(characterX.toString())
print(characterY.toString())
