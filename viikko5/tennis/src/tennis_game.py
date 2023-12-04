class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        if player_name == self.player2_name:
            self.player2_points += 1

    def get_score(self):

        if self.player1_points == self.player2_points:
            score = self.tie_game()
            
        elif self.over_three_points():
            score = self.vantage()
            
        else:
            score = self.count_points()

        return score

    def vantage(self):
        difference = self.player1_points - self. player2_points

        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def count_points(self):
        points_dict = {0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty"}
        score = f"{points_dict[self.player1_points]}-{points_dict[self.player2_points]}"
        
        return score

    def tie_game(self):
        if self.player1_points == 0:
            score = "Love-All"
        elif self.player1_points == 1:
            score = "Fifteen-All"
        elif self.player1_points == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        
        return score

    def over_three_points(self):
        if self.player1_points >= 4 or self.player2_points >= 4:
            return True
        else:
            return False