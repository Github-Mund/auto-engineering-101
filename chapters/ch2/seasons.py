""""" Challenge 2

    Write a program, with Scenarios and Tests, that does the following:
    
    1. Ask the user to enter a Season #Given a season
    2. Using this input, create the logic  to handle different seasons: #When the season is added 

        * If the input is "winter", print "snow"              #Then the results are as follows
        * If the input is "spring", print "flowers"
        * If the input is "summer", print "beach"
        * If the input is "fall" or "autumn", print "leaves"
        * If the input is anything else, print "I don't know that season" """""



def season(season_input):
    if season_input == "winter":
        return "snow"
    elif season_input == "spring":
        return "flowers"
    elif season_input == "summer":
        return "beach"
    elif season_input == "fall":
        return "leaves"
    else:
        return "I don't know that season"

def challenge2():
    season_input = input("Enter a season: ")
    print(season(season_input))

if __name__ == '__main__':
    challenge2()