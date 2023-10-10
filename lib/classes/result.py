class Result:
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score


# @property
# def score(self):
#     return self._score

# @score.setter
# def score(self, new_score):
#     if new_score >= 1 and new_score <= 5000:
#         self._score = new_score
#     else:
#         raise ValueError("It should be btwn 1 and 5000 chars")


    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if new_score >= 1 and new_score <= 5000:
            self._score = new_score
        else:
            raise ValueError('score must be between 1 and 5000')


    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        from classes.player import Player
        if (new_player, Player):
            self._player = new_player
        else:
            raise ValueError('player must be of type Player')


    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        from classes.game import Game
        if (new_game, Game):
            self._game = new_game
        else:
            raise ValueError('game must be of type Game')