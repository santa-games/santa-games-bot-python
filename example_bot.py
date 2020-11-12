import requests, time, json, os
import argparse, sys
from santa_games import User

parser = argparse.ArgumentParser()
parser.add_argument("user_name")
args = parser.parse_args(sys.argv[1:])

#API_URL = "https://santa-shares.azurewebsites.net"
API_URL = "http://localhost"

user = User(API_URL, args.user_name)
user.register()

time.sleep(1)