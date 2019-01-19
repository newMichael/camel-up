from .Player import Player

class Game():

    def __init__(self, player_names):
        self.game_over = False
        self.players = []
        self.spaces = {}
        self.pyramid = []
        for name in player_names:
            player = Player(name)
            self.players.append(player)
        self.randomly_set_first_player()
        #TODO initalize 5 dice
        #roll each dice and place camel on space
        #add dice to pyramid

    #TODO
    def advance_game(self):
        return False
        
    #TODO
    def is_round_over(self):
        return False

    #TODO
    def randomly_set_first_player(self):
        return False

    #TODO
    def set_next_first_player(self):
        return False



    