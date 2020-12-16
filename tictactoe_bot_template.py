import requests, time, json, os, random
import argparse, sys
from santa_games import API

USER_NAME = "" # Enter a unique name here.
API_URL = "https://santa-games.azurewebsites.net"
REFRESH_RATE_SECONDS = 1

api = API(API_URL, USER_NAME)
time.sleep(1)

print("Starting the bot!")
while True:
    time.sleep(REFRESH_RATE_SECONDS)
    print("Evaluating behaviour loop.")

    # get a list of games from the server where it's my turn
    games = api.get_games_my_turn()
    if len(games) > 0:
        for game_info in games:
            
            # extract the game_id from the response
            game_id = game_info.get("game_id")
            if game_id is None:
                print(f"game_id [{game_id}] wasn't provided.")
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

            # get a list of the free spaces
            options = [i for i, c in enumerate(game_data) if c == ' ']
            if len(options) == 0:
                print("Doesn't look like there's space for me to play..")
                continue

            # EDIT HERE
            # =========

            option = random.choice(options)

            # =========

            print(f"I'm going to play at [{option}]")
            response = api.action(game_id, option)
    else:
        # check if there are any proposed games
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

            print("Proposing a new game")
            response = api.propose("0")
            print(response.json())

    