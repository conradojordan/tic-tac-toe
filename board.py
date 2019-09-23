class Board:

    def __init__(self,topL = '',topM = '',topR = '',midL = '',midM = '',midR = '',botL = '',botM = '',botR = ''):
        self.tiles = {'topL': topL, 'topM': topM, 'topR': topR,
                      'midL': midL, 'midM': midM, 'midR': midR,
                      'botL': botL, 'botM': botM, 'botR': botR}


    def printBoard(self):
        print(self.tiles['topL'].ljust(1), self.tiles['topM'].ljust(1), self.tiles['topR'].ljust(1), sep=' |')
        print('--+--+--')
        print(self.tiles['midL'].ljust(1), self.tiles['midM'].ljust(1), self.tiles['midR'].ljust(1), sep=' |')
        print('--+--+--')
        print(self.tiles['botL'].ljust(1), self.tiles['botM'].ljust(1), self.tiles['botR'].ljust(1), sep=' |')


    def availableTiles(self):
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
        if self.tiles['topL'] and self.tiles['topL'] == self.tiles['topM'] and self.tiles['topM'] == self.tiles['topR']:
            return self.tiles['topL'] #Across the top
        elif self.tiles['midL'] and self.tiles['midL'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['midR']:
            return self.tiles['midL'] #Across the middle
        elif self.tiles['botL'] and self.tiles['botL'] == self.tiles['botM'] and self.tiles['botM'] == self.tiles['botR']:
            return self.tiles['botL'] #Across the bottom
        elif self.tiles['topL'] and self.tiles['topL'] == self.tiles['midL'] and self.tiles['midL'] == self.tiles['botL']:
            return self.tiles['topL'] #Left column
        elif self.tiles['topM'] and self.tiles['topM'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['botM']:
            return self.tiles['topM'] #Middle column
        elif self.tiles['topR'] and self.tiles['topR'] == self.tiles['midR'] and self.tiles['midR'] == self.tiles['botR']:
            return self.tiles['topR'] #Right column
        elif self.tiles['topL'] and self.tiles['topL'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['botR']:
            return self.tiles['topL'] #Diagonal \
        elif self.tiles['topR'] and self.tiles['topR'] == self.tiles['midM'] and self.tiles['midM'] == self.tiles['botL']:
            return self.tiles['topR'] #Diagonal /
        else:
            return False

    def makeCopy(self):
        return Board(self.tiles['topL'], self.tiles['topM'], self.tiles['topR'],
                     self.tiles['midL'], self.tiles['midM'], self.tiles['midR'],
                     self.tiles['botL'], self.tiles['botM'], self.tiles['botR'])

    def endGame(self):
        print('Final game board:')
        self.printBoard()
