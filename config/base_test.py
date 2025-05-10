from services.api_users import UserApi
from services.games.games_api import GamesApi

class BaseTest:
    def setup_method(self):
        self.api_users = UserApi()
        self.api_games = GamesApi()