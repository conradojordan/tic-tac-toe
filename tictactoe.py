import board, random


def AIMove(gameBoard, difficulty, computerSymbol, humanSymbol):
    print('\n\n\nThe computer is thinking...')
    if difficulty == 'easy':
        move = AIEasy(gameBoard)
    elif difficulty == 'medium':
        move = AIMedium(gameBoard, computerSymbol, humanSymbol)
    else: #difficulty == 'hard'
        move = AIHard(gameBoard, computerSymbol, humanSymbol)
    print('The computer has made its move!')
    return move


def AIEasy(gameBoard):
    return random.choice(gameBoard.availableTiles())


def AIMedium(gameBoard, computerSymbol, humanSymbol):
    gameBoardCopy = gameBoard.makeCopy()
    #Find winning tile
    for move in gameBoard.availableTiles():
        gameBoardCopy.makeMove(move, computerSymbol)
        if gameBoardCopy.hasWinner():
            return move
        gameBoardCopy.resetTile(move)
    #Block opponent winning tile
    for move in gameBoard.availableTiles():
        gameBoardCopy.makeMove(move, humanSymbol)
        if gameBoardCopy.hasWinner():
            return move
        gameBoardCopy.resetTile(move)
    #If found none of above, make random move
    return random.choice(gameBoard.availableTiles())


def AIHard(gameBoard, computerSymbol, humanSymbol):
    gameBoardCopy = gameBoard.makeCopy()
    moveOptions = []
    #Find immediate win
    for move in gameBoard.availableTiles():
        gameBoardCopy.makeMove(move, computerSymbol)
        if gameBoardCopy.hasWinner():
            return move
        gameBoardCopy.resetTile(move)
    #Compare evaluation of possible moves
    for move in gameBoard.availableTiles():
        gameBoardCopy.makeMove(move,computerSymbol)
        currentMoveEvaluation = evaluateBoard(gameBoardCopy,computerSymbol,humanSymbol)
        #Return move guaranteed to win, if possible
        if  currentMoveEvaluation == 1:
            return move
        #Make a list of draw moves
        elif currentMoveEvaluation == 0:
            moveOptions.append(move)
        gameBoardCopy.resetTile(move)
    #Pick random from list of draws
    if len(moveOptions) > 0:
        return random.choice(moveOptions)
    #If there are only losing moves, pick a random one
    else:
        return random.choice(gameBoard.availableTiles())


def evaluateBoard(gameBoard, symbolToEvaluate, currentPlayer):
    nextPlayer = 'o' if currentPlayer == 'x' else 'x'
    winner = gameBoard.hasWinner()
    #Evaluate if game was win (1), loss(-1) or draw(0)
    if winner:
        if winner == symbolToEvaluate:
            return 1
        else:
            return -1
    elif len(gameBoard.availableTiles()) == 0:
        return 0
    #If evaluation is not immediate, use recursion to make all possible moves and evalute those
    else:
        evaluations = list()
        for tile in gameBoard.availableTiles():
            gameBoardCopy = gameBoard.makeCopy()
            gameBoardCopy.makeMove(tile,currentPlayer)
            evaluations.append(evaluateBoard(gameBoardCopy,symbolToEvaluate,nextPlayer))
        if symbolToEvaluate == currentPlayer:
            return max(evaluations)
        else:
            return min(evaluations)


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
    difficulty = int(input('What difficulty do you want to play (1) - easy, (2) - medium, (3) - hard? '))
    while difficulty not in [1, 2, 3]:
        difficulty = int(input('Invalid option. Please type 1, 2 or 3 (1 - easy, 2 - medium, 3 - hard): '))
    return difficultyOptions[difficulty-1]


def doesComputerStart():
    whoStarts = int(input('Who shall start the game (1) - you, (2) - computer, (3) - random? '))
    while whoStarts not in [1, 2, 3]:
        whoStarts = int(input('Invalid option. Please type 1, 2 or 3 (1 - you, 2 - computer, 3 - random): '))
    if whoStarts == 3:
        return random.choice([True, False])
    else:
        return whoStarts == 2


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
        computerStarts = doesComputerStart()

        if computerStarts:
            gameBoard.makeMove(AIEasy(gameBoard),computerSymbol)

        while gameIsNotOver:
            gameBoard.printBoard()

            #Human plays
            humanTile = humanMove(gameBoard)
            gameBoard.makeMove(humanTile,humanSymbol)
            if isGameFinished(gameBoard,'human'):
                break

            #Computer plays
            computerTile = AIMove(gameBoard, difficulty, computerSymbol, humanSymbol)
            gameBoard.makeMove(computerTile,computerSymbol)
            if isGameFinished(gameBoard,'computer'):
                break

        gameBoard.endGame()
        gameBoard.resetBoard()
        humanWantsToKeepPlaying = askHumanToContinue()
