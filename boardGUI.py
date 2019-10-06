class Board:
    """Class that represents the board of the game."""

    def __init__(self,topL = '',topM = '',topR = '',midL = '',midM = '',midR = '',botL = '',botM = '',botR = ''):
        self.tiles = {'topL': topL, 'topM': topM, 'topR': topR,
                      'midL': midL, 'midM': midM, 'midR': midR,
                      'botL': botL, 'botM': botM, 'botR': botR}


    def availableTiles(self):
        """Returns a list of available tiles in the board (example: ['topL', 'midR', 'botM'])"""
        availableTiles = list()
        for tile, symbol in self.tiles.items():
            if not symbol:
                availableTiles.append(tile)
        return availableTiles


    def makeMove(self, tile, symbol):
        self.tiles[tile] = symbol


    def resetTile(self, tile):
        self.tiles[tile] = ''


    def resetBoard(self):
        for tile in self.tiles:
            self.tiles[tile] = ''


    def hasWinner(self):
        """If the board has winner, returns the winning symbol and the starting and end point of the winning move.
        Example: return 'x', ['topL', 'topR']
        """
        if self.tiles['topL'] and self.tiles['topL'] == self.tiles['topM'] and self.tiles['topM'] == self.tiles['topR']:
            return self.tiles['topL'], ['topL', 'topR'] #Across the top
        elif self.tiles['midL'] and self.tiles['midL'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['midR']:
            return self.tiles['midL'], ['midL', 'midR'] #Across the middle
        elif self.tiles['botL'] and self.tiles['botL'] == self.tiles['botM'] and self.tiles['botM'] == self.tiles['botR']:
            return self.tiles['botL'], ['botL', 'botR'] #Across the bottom
        elif self.tiles['topL'] and self.tiles['topL'] == self.tiles['midL'] and self.tiles['midL'] == self.tiles['botL']:
            return self.tiles['topL'], ['topL', 'botL'] #Left column
        elif self.tiles['topM'] and self.tiles['topM'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['botM']:
            return self.tiles['topM'], ['topM', 'botM'] #Middle column
        elif self.tiles['topR'] and self.tiles['topR'] == self.tiles['midR'] and self.tiles['midR'] == self.tiles['botR']:
            return self.tiles['topR'], ['topR', 'botR'] #Right column
        elif self.tiles['topL'] and self.tiles['topL'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['botR']:
            return self.tiles['topL'], ['topL', 'botR'] #Diagonal \
        elif self.tiles['topR'] and self.tiles['topR'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['botL']:
            return self.tiles['topR'], ['topR', 'botL'] #Diagonal /
        else:
            return False

    def makeCopy(self):
        """Return a Board object that is a copy of the current Board object. """
        return Board(self.tiles['topL'], self.tiles['topM'], self.tiles['topR'],
                     self.tiles['midL'], self.tiles['midM'], self.tiles['midR'],
                     self.tiles['botL'], self.tiles['botM'], self.tiles['botR'])
