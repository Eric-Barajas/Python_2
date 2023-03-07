from players import players

class Player:


    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

    @classmethod
    def player_list(cls, players):
        new_team = []
        for player in players:
            new_player = Player(player)
            new_team.append(new_player)
        return new_team

    def __repr__(self):
        return f'player: {self.name}, age:{self.age}, position {self.position}, team:{self.team} |'
# challenge 1
# player1 = Player (players[0])
# player2 = Player (players[1])

# challenge 2
kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???
# player_kevin = Player(kevin)
# print(player_kevin)
# # challenge 3
# new_list = []
# for player in players:
#     new_player = Player(player)
#     new_list.append(new_player)
# print(new_list)


    

team = Player.player_list(players)
print(team)