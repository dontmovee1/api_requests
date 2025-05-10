import os



HOST = "https://dev-gs.qa-playground.com/api/v1"

class Endpoints:
    create_user=f"{HOST}/users"
    get_user_by_id=lambda self, uuid: f"{HOST}/users/{uuid}"


class GameEndpoints:
    games = f"{HOST}/games"
    search_games = f"{HOST}/games/search"