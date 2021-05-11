from Gamedata import *

def Auto_Complete(input):
    possible_genres = []
    for genre in Genres:
        if genre.startswith(input):
            possible_genres.append(genre)
    return possible_genres


def GameSearch():
    Selected_game = ""

    while Selected_game == "":
        user_input = str(input("What type of game are you looking for? \nPlease type out all or some of a genre name to see what is available."))

        possible_genres = Auto_Complete(user_input)

        print(f"It looks like you may have been looking for the following genres: {possible_genres}")

        if len(possible_genres) == 1:
            See_games = str(input("You seem to have found a genre.  Would you like to view the available games in that genre?  y/n"))
            if See_games == "y":
                Games_list = []
                for game in Games:
                    if possible_genres[0] == game[1]:
                        print(f"Game Name: {game[0]}")
                        print(f"Dollar Price: {game[2]}")
                        print(f"Rating: {game[3]}")
                        print(" --- ")
                Try_Again = str(input("Would you like to search again?  y/n"))
                if Try_Again == "n":
                    Selected_game = Games_list

GameSearch()