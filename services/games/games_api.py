import allure
import requests
from utils.helper import Helper
from services.payloads import GamePayloads
from services.endpoints import GameEndpoints
from config.headers import Headers
from services.users.models.game_model import GameListModel

class GamesApi(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = GamePayloads()
        self.endpoints = GameEndpoints()
        self.headers = Headers()

    @allure.step("Get all games")
    def get_all_games(self):
        response = requests.get(
            url=self.endpoints.games,
            headers=self.headers.search
        )
        assert response.status_code == 200, response.json()
        self.atach_response(response.json())
        return GameListModel(**response.json())

    @allure.step("Search games")
    def search_games(self, query):
        response = requests.get(
            url=self.endpoints.search_games,
            headers=self.headers.search,
            params={"query": query}
        )
        assert response.status_code == 200, response.json()
        self.atach_response(response.json())
        return GameListModel(**response.json())