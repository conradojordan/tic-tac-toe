import board, random

def AIMove(gameBoard, difficulty):
    print('\n\n\nThe computer has made its move!')
    if difficulty == 'easy':
        move = random.choice(gameBoard.availableTiles())
    elif difficulty == 'medium':
        move = random.choice(gameBoard.availableTiles())
    else: #difficulty == 'hard'
        move = random.choice(gameBoard.availableTiles())
    return move

def humanChooseSymbol():
    symbolOptions = ['x', 'o']
    humanSymbol = input("Do you want to play with 'x' or 'o': ").lower()
    while humanSymbol not in symbolOptions:
        humanSymbol = input("Not a valid option, try again ('x' or 'o'): ").lower()
    if humanSymbol == 'x':
        return symbolOptions
    else:
        return symbolOptions[1], symbolOptions[0]

def humanChooseDifficulty():
    difficultyOptions = ['easy', 'medium', 'hard']
    difficulty = int(input('What difficulty do you want to play (1 - easy, 2 - medium, 3 - hard)? '))
    while difficulty not in [1, 2, 3]:
        difficulty = int(input('Invalid option. Please type 1, 2 or 3 (1 - easy, 2 - medium, 3 - hard): '))
    return difficultyOptions[difficulty-1]

def humanMove(gameBoard):
    humanTile = input(f"It is your turn - playing as '{humanSymbol}'. \nMake your move (topL, topM, topR, midL, midM, midR, botL, botM, botR): ")
    while not humanTile in gameBoard.availableTiles():
        humanTile = input('Not a valid choice! Try again: ')
    return humanTile

def isGameFinished(gameBoard,currentPlayer):
    if gameBoard.hasWinner():
        gameBoard.printBoard()
        if currentPlayer == 'human':
            print('You won! Congratulations!!')
        else:
            print('The computer won! You suck, go do something else that you suck less...')
        return True
    if len(gameBoard.availableTiles()) == 0:
        print('The game is a draw.')
        return True
    return False

def askHumanToContinue():
    keepPlaying = input('Do you want to continue playing (y/n)? ')
    if keepPlaying.lower() == 'y':
        return True
    else:
        return False

if __name__ == "__main__":
    gameBoard = board.Board()
    humanWantsToKeepPlaying = True
    gameIsNotOver = True

    while humanWantsToKeepPlaying:
        print('Tic-tac-toe began!')
        humanSymbol, computerSymbol = humanChooseSymbol()
        difficulty = humanChooseDifficulty()

        while gameIsNotOver:
            gameBoard.printBoard()

            #Human plays
            humanTile = humanMove(gameBoard)
            gameBoard.makeMove(humanTile,humanSymbol)
            if isGameFinished(gameBoard,'human'):
                break

            #Computer plays
            computerTile = AIMove(gameBoard, difficulty)
            gameBoard.makeMove(computerTile,computerSymbol)
            if isGameFinished(gameBoard,'computer'):
                break

        gameBoard.endGame()
        gameBoard.resetBoard()
        humanWantsToKeepPlaying = askHumanToContinue()
