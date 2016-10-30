class SearchFunction:
    def __init__(self):
        pass

    @staticmethod
    def findBestSportsman(database):
        for key in database:
            listOfSportsman = database.get(key).listOfSportsmen
            rating = 0
            for value in listOfSportsman:
                if value.rating > rating:
                    rating = value.rating
            for value in listOfSportsman:
                if value.rating == rating:
                    value.printSportsman()