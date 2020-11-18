import os, requests, json

class API:
    def __init__(self, api_url, user_name):
        self.user_name = user_name
        self.config_file_name = f"{user_name}.json"
        self.api_url = api_url
        self.token = None

        if not os.path.exists(self.config_file_name):
            response = requests.post(self.api_url+"/api/users", json={ "user_name" : self.user_name })
            if response.status_code != 201:
                print(f"[{response.status_code}]")
                exit()
            else:
                json_response = response.json()
                self.user_id = json_response.get("user_id")
                self.token = json_response.get("token")
                with open(self.config_file_name, "w") as file:
                    json.dump({
                        "user_id" : self.user_id,
                        "user_name" : self.user_name,
                        "token" : self.token,
                    }, file)

        with open(self.config_file_name, "r") as file:
            json_data = json.load(file)
            self.user_id = json_data["user_id"]
            self.user_name = json_data["user_name"]
            self.token = json_data["token"]

        self.headers = { "Authorization" : f"token {self.token}" }

    def get_status(self):
        return requests.get(f"{self.api_url}/api/users/{self.user_id}", headers=self.headers).json()

    def get_games(self):
        return requests.get(f"{self.api_url}/api/games", headers=self.headers).json()

    def get_proposed_games(self):
        return requests.get(f"{self.api_url}/api/games?game_state_id=0", headers=self.headers).json()

    def get_games_my_turn(self):
        return requests.get(f"{self.api_url}/api/games?next_user_id={self.user_id}", headers=self.headers).json()

    def get_game(self, game_id):
        return requests.get(f"{self.api_url}/api/games/{game_id}", headers=self.headers).json()

    def propose(self, game_type_id):
        return requests.post(f"{self.api_url}/api/games", headers=self.headers, json={ "game_type_id" : game_type_id })

    def accept(self, game_id):
        return requests.put(f"{self.api_url}/api/games/{game_id}", headers=self.headers, json={ "game_state_id" : 1 })

    def action(self, game_id, action):
        return requests.post(f"{self.api_url}/api/games/{game_id}/turns", headers=self.headers, json={ "action" : action })