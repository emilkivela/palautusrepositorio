import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.players = []

    def get_players(self):  
        response = requests.get(self.url).json()
        for player_dict in response:
            player = Player(player_dict)
            self.players.append(player)
        return self.players
        

class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()
    
    def top_scorers_by_nationality(self, nationality):
        self.nationality = nationality
        self.top_scorers = []
        for player in self.players:
            if player.nationality == self.nationality:
                self.top_scorers.append(player)
        self.top_scorers.sort(key=lambda x:x.points, reverse=True)
        return self.top_scorers



def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality('FIN')
    for player in players:
        print(player)

main()