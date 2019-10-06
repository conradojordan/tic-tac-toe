import boardGUI

class BoardText(boardGUI.Board):
    """Class that represents the board of the game.
    Inherits from the boardGUI class and adds some text functionalities."""


    def printBoard(self):
        """Prints the current state of the board."""
        print(self.tiles['topL'].ljust(1), self.tiles['topM'].ljust(1), self.tiles['topR'].ljust(1), sep=' |')
        print('--+--+--')
        print(self.tiles['midL'].ljust(1), self.tiles['midM'].ljust(1), self.tiles['midR'].ljust(1), sep=' |')
        print('--+--+--')
        print(self.tiles['botL'].ljust(1), self.tiles['botM'].ljust(1), self.tiles['botR'].ljust(1), sep=' |')


    def endGame(self):
        print('Final game board:')
        self.printBoard()
