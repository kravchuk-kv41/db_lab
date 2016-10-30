import sportsman
import team
import pickle
import task


i = 0
database = {}
currentId = 0
# set database
while i != 1 and i != 2:
    try:
        i = input("1 - Read database from file \n"
                  "2 - Work with database sample \n")
    except NameError:
        print "Error, try again"
    # read from file
    if i == 1:
        # exception
        # currentId here
        f = open(r"database.txt", 'rb')
        database = pickle.load(f)
        f.close()
        currentId = len(database) - 1
    # sample
    elif i == 2:
        team1 = team.Team(currentId, "team1", "league1", "city1")
        team1.addSportsmanToList(sportsman.Sportsman(currentId, "team1_player1", "position1", "50"))
        team1.addSportsmanToList(sportsman.Sportsman(currentId, "team1_player2", "position1", "66"))
        team1.addSportsmanToList(sportsman.Sportsman(currentId, "team1_player3", "position2", "90"))
        team1.addSportsmanToList(sportsman.Sportsman(currentId, "team1_player4", "position2", "85"))
        team1.addSportsmanToList(sportsman.Sportsman(currentId, "team1_player5", "position3", "90"))

        currentId += 1
        team2 = team.Team(currentId, "team2", "league2", "city2")
        team2.addSportsmanToList(sportsman.Sportsman(currentId, "team2_player1", "position1", "50"))
        team2.addSportsmanToList(sportsman.Sportsman(currentId, "team2_player2", "position2", "60"))
        team2.addSportsmanToList(sportsman.Sportsman(currentId, "team2_player3", "position2", "70"))
        team2.addSportsmanToList(sportsman.Sportsman(currentId, "team2_player4", "position3", "80"))
        team2.addSportsmanToList(sportsman.Sportsman(currentId, "team2_player5", "position3", "90"))

        currentId += 1
        team3 = team.Team(currentId, "team3", "league3", "city3")
        team3.addSportsmanToList(sportsman.Sportsman(currentId, "team3_player1", "position1", "50"))
        team3.addSportsmanToList(sportsman.Sportsman(currentId, "team3_player2", "position1", "50"))
        team3.addSportsmanToList(sportsman.Sportsman(currentId, "team3_player3", "position2", "70"))
        team3.addSportsmanToList(sportsman.Sportsman(currentId, "team3_player4", "position2", "75"))
        team3.addSportsmanToList(sportsman.Sportsman(currentId, "team3_player5", "position2", "85"))

        currentId += 1
        team4 = team.Team(currentId, "team4", "league4", "city4")
        team4.addSportsmanToList(sportsman.Sportsman(currentId, "team4_player1", "position1", "50"))
        team4.addSportsmanToList(sportsman.Sportsman(currentId, "team4_player2", "position1", "60"))
        team4.addSportsmanToList(sportsman.Sportsman(currentId, "team4_player3", "position2", "80"))
        team4.addSportsmanToList(sportsman.Sportsman(currentId, "team4_player4", "position2", "85"))
        team4.addSportsmanToList(sportsman.Sportsman(currentId, "team4_player5", "position2", "95"))

        currentId += 1
        team5 = team.Team(currentId, "team5", "league5", "city5")
        team5.addSportsmanToList(sportsman.Sportsman(currentId, "team5_player1", "position1", "50"))
        team5.addSportsmanToList(sportsman.Sportsman(currentId, "team5_player2", "position1", "60"))
        team5.addSportsmanToList(sportsman.Sportsman(currentId, "team5_player3", "position2", "80"))
        team5.addSportsmanToList(sportsman.Sportsman(currentId, "team5_player4", "position2", "95"))
        team5.addSportsmanToList(sportsman.Sportsman(currentId, "team5_player5", "position2", "95"))

        database[team1.getTeamId()] = team1
        database[team2.getTeamId()] = team2
        database[team3.getTeamId()] = team3
        database[team4.getTeamId()] = team4
        database[team5.getTeamId()] = team5
    # error
    else:
        print "Wrong choice, try again"

i = 0
while i != 7:
    try:
        i = input("1 - Output list of teams \n"
                  "2 - Edit or remove team \n"
                  "3 - Add new team \n"
                  "4 - Output list of sportsmen from team \n"
                  "5 - Find best from each team \n"
                  "6 - Save data into file \n"
                  "7 - Exit \n")
    except NameError:
        print "Error, try again"
        continue
    # list of teams
    if i == 1:
        for k in database:
            database.get(k).printTeam()
    # edit team
    elif i == 2:
        print "You can't edit data of main essence"
    # list of sportsmen
    elif i == 3:
        teamName = raw_input("Team name = ")
        teamLeague = raw_input("Team league = ")
        teamCity = raw_input("Team city = ")
        currentId += 1
        newTeam = team.Team(currentId, teamName, teamLeague, teamCity)
        j = raw_input("Do you want to add an athlete in the team? ")
        # print n or y
        while j != "n":
            sportsmanName = raw_input("Sportsman name = ")
            sportsmanPosition = raw_input("Sportsman position = ")
            try:
                sportsmanRating = input("Sportsman rating = ")
                newSportsman = sportsman.Sportsman(currentId, sportsmanName, sportsmanPosition, sportsmanRating)
                newTeam.addSportsmanToList(newSportsman)
            except NameError:
                print "Error, try again"
            j = raw_input("Do you want to add one more athlete in the team? \n")
        database[newTeam.getTeamId()] = newTeam
    elif i == 4:
        teamName = raw_input("Team name = ")
        flag = False
        key = 0  # team
        for key in database:
            if database.get(key).teamName == teamName:
                flag = True
                break
        if flag:
            database.get(key).printListOfSportsmen()
            k = 0
            while k != 5:
                try:
                    k = input("1 - Edit sportsman \n"
                              "2 - Remove sportsman \n"
                              "3 - Add new sportsman to team \n"
                              "4 - Output list of sportsmen \n"
                              "5 - Return to main menu \n")
                except NameError:
                    print "Error, try again"
                if k == 1:
                    sportsmanName = raw_input("Sportsman name = ")
                    if database.get(key).findSportsmanInList(sportsmanName) is not None:
                        database.get(key).findSportsmanInList(sportsmanName).sportsmanName = sportsmanName
                        database.get(key).findSportsmanInList(sportsmanName).position = raw_input("Sportsman position = ")
                        try:
                            database.get(key).findSportsmanInList(sportsmanName).rating = input("Sportsman rating = ")
                        except NameError:
                            print "Error, try again"
                    else:
                        print "Sportsman not found"
                elif k == 2:
                    database.get(key).removeSportsmanFromList(raw_input("Sportsman name = "))
                elif k == 3:
                    sportsmanName = raw_input("Sportsman name = ")
                    sportsmanPosition = raw_input("Sportsman position = ")
                    try:
                        sportsmanRating = input("Sportsman rating = ")
                        newSportsman = sportsman.Sportsman(database.get(key).getTeamId(), sportsmanName,
                                                           sportsmanPosition, sportsmanRating)
                        database.get(key).addSportsmanToList(newSportsman)
                    except NameError:
                        print "Error, try again"
                elif k == 4:
                    database.get(key).printListOfSportsmen()

        else:
            # not found
             print "Team not found"
    elif i == 5:
        task.SearchFunction.findBestSportsman(database)
    elif i == 6:
        f = open(r"database.txt", 'wb')
        pickle.dump(database, f)
        f.close()
    elif i == 7:
        break
    else:
        print "Wrong choice, try again"