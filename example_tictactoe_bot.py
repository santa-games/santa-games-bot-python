import requests, time, json, os, random
import argparse, sys
from santa_games import API

parser = argparse.ArgumentParser()
parser.add_argument("user_name")
args = parser.parse_args(sys.argv[1:])

#API_URL = "https://santa-games.azurewebsites.net"
API_URL = "http://localhost"

REFRESH_RATE_SECONDS = 1

api = API(API_URL, args.user_name)

time.sleep(1)

while True:
    time.sleep(REFRESH_RATE_SECONDS)
    print("Doing something...")

    # get a list of games from the server where it's my turn
    games = api.get_games_my_turn()
    if len(games) > 0:
        for game_info in games:
            # Extract the game_id from the response
            game_id = game_info.get("game_id")
            if game_id is None:
                print("Huh, game_id wasn't in the dictionary :/")
                continue
            print(f"Taking my turn for game [{game_id}]")

            # get the full game information
            game = api.get_game(game_id)
            if game is None:
                print(f"Unable to get game {game_id} from the API :(")
                continue

            game_data = game.get("data")
            if game_data is None:
                print("I kinda needed the game data to make my move...")
                continue

            # I'll choose a random free space (because totally the best strategy)
            options = [i for i, c in enumerate(game_data) if c == ' ']
            if len(options) == 0:
                print("Doesn't look like there's space for me to play..")
                continue

            option = random.choice(options)
            print(f"I'm going to play at [{option}]")

            response = api.action(game_id, option)
            print(response.json())
    else:
        # I should see if someone wants to play a game..
        proposed_games = api.get_proposed_games()
        valid_proposed_games = [proposed_game for proposed_game in proposed_games if proposed_game["host_user_id"] != api.user_id]
        
        if len(valid_proposed_games) > 0:
            proposed_game = valid_proposed_games[0]

            game_id = proposed_game.get("game_id")
            if game_id is None: continue

            print(f"I'm going to accept a proposed game [{game_id}]...")
            response = api.accept(game_id)
            print(response.json())
        else:
            if len(proposed_games) - len(valid_proposed_games) != 0:
                continue

            # I shall host my own game
            print("I shall propose my own game...")
            response = api.propose("0")
            print(response.json())

    