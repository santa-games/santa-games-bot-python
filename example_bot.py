import requests, time, json, os
import argparse, sys
from santa_games import API

parser = argparse.ArgumentParser()
parser.add_argument("user_name")
args = parser.parse_args(sys.argv[1:])

#API_URL = "https://santa-shares.azurewebsites.net"
API_URL = "http://localhost"

REFRESH_RATE_SECONDS = 5

api = API(API_URL, args.user_name)
api.register()

time.sleep(1)

while True:
    print(" ")

    # check if its my go for any games

    games = api.get_games()



    time.sleep(REFRESH_RATE_SECONDS)