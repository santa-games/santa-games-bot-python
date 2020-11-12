import requests, time, json, datetime, os, random, logging
import argparse, sys
from santa_games import User

logging.basicConfig(level=logging.DEBUG)

API_URL = os.environ.get("SANTA_GAMES_API_URL", "https://santa-games.azurewebsites.net")
#API_URL = "http://localhost" 

class ManualBot:

    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("command")
        args = parser.parse_args(sys.argv[1:2])
        command_name = args.command

        if hasattr(self, command_name):
            command = getattr(self, command_name)
            command()

    def propose(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("user_name")
        parser.add_argument("game_type_id")
        args = parser.parse_args(sys.argv[2:])

        user_name = args.user_name
        game_type_id = args.game_type_id

        user = User(API_URL, user_name)
        user.register()
        response = user.propose(game_type_id)
        print(response.text)

    def accept(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("user_name")
        parser.add_argument("game_id")
        args = parser.parse_args(sys.argv[2:])

        user_name = args.user_name
        game_id = args.game_id

        user = User(API_URL, user_name)
        user.register()
        user.accept(game_id)

    def action(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("user_name")
        parser.add_argument("game_id")
        parser.add_argument("action")
        args = parser.parse_args(sys.argv[2:])

        user_name = args.user_name
        game_id = args.game_id
        action = args.action

        user = User(API_URL, user_name)
        user.register()
        user.action(game_id, action)

if __name__ == "__main__":
    ManualBot()