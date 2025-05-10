import allure
import pytest

from config.base_test import BaseTest


@allure.epic("Game Store API")
class TestGameStore(BaseTest):
    @allure.feature("Game Search")
    @allure.story("Search by keyword")
    @allure.title("Search games by title part")
    @pytest.mark.regression
    def test_search_games(self):
        """Тест поиска игр по части названия"""
        # 1. Получаем список всех игр
        all_games = self.api_games.get_all_games()
        assert len(all_games.games) > 0

        # 2. Выбираем игру и готовим запрос
        first_game = all_games.games[0]
        search_query = first_game.title.split()[0]

        # 3. Выполняем поиск
        search_results = self.api_games.search_games(search_query)

        # 4. Проверяем результаты
        assert len(search_results.games) > 0
        assert search_query.lower() in search_results.games[0].title.lower()