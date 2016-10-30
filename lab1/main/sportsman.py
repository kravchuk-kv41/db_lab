class Sportsman:
    def __init__(self, id, sportsmanName, position, rating):
        self.id = id
        self.sportsmanName = sportsmanName
        self.position = position
        self.rating = rating

    def printSportsman(self):
        print str(self.id) + self.sportsmanName + "\t" + self.position + "\t" + str(self.rating)

    def editSportsmanName(self, name):
        self.sportsmanName = name

    def editSportsmanPosition(self, position):
        self.position = position

    def editSportsmanRating(self, rating):
        self.rating = rating