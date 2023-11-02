import unittest
from statistics_service import StatisticsService
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        self.assertEqual(self.stats.search("Semenko"), self.stats._players[0])
    
    def test_search_returns_none_if_no_players(self):
        self.assertEqual(self.stats.search("Tikkanen"), None)

    def test_team_finds_all_players(self):
        self.assertEqual(self.stats.team("EDM"), [self.stats._players[0], self.stats._players[2], self.stats._players[4]])
    
    def test_top_finds_most_points(self):
        self.assertEqual(self.stats.top(1)[0], self.stats._players[4])
    
    def test_top_sorted_by_goals(self):
        self.assertEqual(self.stats.top(1,SortBy.GOALS)[0], self.stats._players[1])
    
    def test_top_sorted_by_assists(self):
        self.assertEqual(self.stats.top(1,SortBy.ASSISTS)[0], self.stats._players[4])
