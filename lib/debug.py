#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    
    player =Player("Ann")
    print(player.get_username())


    p= Player("suha")
    g = Game("GTA")
    Result(player,g, 50)
    p.return_all_games() 

        
    game = Game("GTA")
    print(game.get_title())

    
    score =Result("PlayerName", "GameName",50)
    print(score.get_score())    

    ipdb.set_trace()


