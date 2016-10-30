class Team:
    def __init__(self, id, teamName, league, city):
        self.id = id
        self.teamName = teamName
        self.league = league
        self.city = city
        self.listOfSportsmen = []

    def printTeam(self):
        print str(self.id) + self.teamName + "  " + self.league + "  " + self.city

    def addSportsmanToList(self, sportsman):
        self.listOfSportsmen.append(sportsman)

    def findSportsmanInList(self, sportsmanName):
        for i in self.listOfSportsmen:
            if i.sportsmanName == sportsmanName:
                return i
        return None

    def removeSportsmanFromList(self, sportsmanName):
        for v in self.listOfSportsmen:
            if v.sportsmanName == sportsmanName:
                self.listOfSportsmen.remove(v)
                break
        else:
            print "Sportsman not found"

    def printListOfSportsmen(self):
        for i in self.listOfSportsmen:
            i.printSportsman()

    def deleteSportsmanFromList(self, name):
        self.listOfSportsmen.remove(name)

    def getTeamId(self):
        return self.id
