import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    games = json_data["games"]
    for game in games:
        platformInfo = game["platform"]
        newPlatform = test_data.Platform(platformInfo["name"], platformInfo["launchYear"])
        newGame = test_data.Game(game["title"], newPlatform, game["year"])
        game_library.add_game(newGame)

    return game_library

#Part 2
input_json_file = "data/test_data.json"

with open(input_json_file, "r") as reader:
    game_json_data = json.load(reader)

newGameLibrary = make_game_library_from_json(game_json_data)
print(newGameLibrary)