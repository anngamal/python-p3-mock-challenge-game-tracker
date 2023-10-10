class Game:
    def __init__(self, title):
        self.title = title
        self.results = []


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self , new_title):
        if len(new_title) <= 0:
             raise ValueError(f"Title is not accepted")
            
        else:
            self._title = new_title




    def get_players(self):
        return [result.player for result in self.results]
    
    def average_score(self, player):
        return sum([r.score for r in self.results if r.player == player]) / len(self.results)