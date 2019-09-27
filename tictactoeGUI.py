import boardGUI, random
from appJar import gui

#Initial game parameters
gameIsRunning = False
computerIsMakingMove = False
humanSymbol = 'x'
computerSymbol = 'o'
computerStarts = False
difficulty = 'easy'
gameBoard = boardGUI.Board()

def AIMove():
    global gameIsRunning, computerIsMakingMove, computerSymbol, difficulty, gameBoard
    computerIsMakingMove = True
    if difficulty == 'easy':
        move = AIEasy()
    elif difficulty == 'medium':
        move = AIMedium()
    else: #difficulty == 'hard'
        move = AIHard()
    gameBoard.makeMove(move, computerSymbol)
    drawMove(move, computerSymbol)
    if isGameFinished('computer'):
        gameIsRunning = False
    computerIsMakingMove = False


def AIEasy():
    global gameBoard
    return random.choice(gameBoard.availableTiles())


def AIMedium():
    global gameBoard, humanSymbol, computerSymbol
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


def AIHard():
    global gameBoard, computerSymbol
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


def evaluateBoard(currentBoard, symbolToEvaluate, currentPlayer):
    nextPlayer = 'o' if currentPlayer == 'x' else 'x'
    winner = currentBoard.hasWinner()
    #Evaluate if game was win (1), loss(-1) or draw(0)
    if winner:
        if winner[0] == symbolToEvaluate:
            return 1
        else:
            return -1
    elif len(currentBoard.availableTiles()) == 0:
        return 0
    #If evaluation is not immediate, use recursion to make all possible moves and evalute those
    else:
        evaluations = list()
        for tile in currentBoard.availableTiles():
            gameBoardCopy = currentBoard.makeCopy()
            gameBoardCopy.makeMove(tile,currentPlayer)
            evaluations.append(evaluateBoard(gameBoardCopy,symbolToEvaluate,nextPlayer))
        if symbolToEvaluate == currentPlayer:
            return max(evaluations)
        else:
            return min(evaluations)


def doesComputerStart():
    whoStarts = app.getRadioButton('first')
    if whoStarts == "You":
        return False
    elif whoStarts == "Random":
        return random.randint(0,1) == 0
    else:
        return True


def humanMove(move):
    global humanSymbol
    gameBoard.makeMove(move,humanSymbol)
    drawMove(move,humanSymbol)


def isGameFinished(currentPlayer):
    global gameBoard, app
    gameHasWinner = gameBoard.hasWinner()
    if gameHasWinner:
        drawRedline(gameHasWinner[1][0], gameHasWinner[1][1])
        if currentPlayer == 'human':
            app.setLabel('announcement', 'You won! Congratulations!!')
        else:
            app.setLabel('announcement', 'The computer won... you suck!')
        return True
    if len(gameBoard.availableTiles()) == 0:
        app.setLabel('announcement', 'The game was a draw.')
        return True
    return False


################################# GUI ####################################
###GUI Constants
GAP = 80
HALFGAP = GAP//2
STARTCOORD = 20
OSIZE = 50
XSIZE = 50
X = [STARTCOORD, STARTCOORD+GAP, STARTCOORD+2*GAP, STARTCOORD+3*GAP]
Y = [i for i in X]
TILESMIDCOORD = {'topL': (X[0]+HALFGAP,Y[0]+HALFGAP), 'topM': (X[0]+3*HALFGAP,Y[0]+HALFGAP), 'topR': (X[0]+5*HALFGAP,Y[0]+HALFGAP),
         'midL': (X[0]+HALFGAP,Y[0]+3*HALFGAP), 'midM': (X[0]+3*HALFGAP,Y[0]+3*HALFGAP), 'midR': (X[0]+5*HALFGAP,Y[0]+3*HALFGAP),
         'botL': (X[0]+HALFGAP,Y[0]+5*HALFGAP), 'botM': (X[0]+3*HALFGAP,Y[0]+5*HALFGAP), 'botR': (X[0]+5*HALFGAP,Y[0]+5*HALFGAP)}

###Event Handlers

def returnClickedTile(event):
    rows = ['top', 'mid', 'bot']
    columns = ['L', 'M', 'R']
    if event.x > 260 or event.x < 20 or event.y > 260 or event.y < 20:
        return False
    else:
        return rows[(event.y-20)//80] + columns[(event.x-20)//80]

def humanClicksCanvas(event):
    global gameIsRunning, computerIsMakingMove, gameBoard
    if gameIsRunning and not computerIsMakingMove:
        clickedTile = returnClickedTile(event)
        if clickedTile in gameBoard.availableTiles():
            humanMove(clickedTile)
            if isGameFinished('human'):
                gameIsRunning = False
            else:
                AIMove()
    else:
        app.setLabel('announcement',"Press button below to start game.")

def press(button):
    if button == "Quit":
        app.stop()
    else:
        playGame()


def changeBackground(OptionBox):
    colorOptions = {"Blue": "#ade4ff", "Green": "#abff9e", "Orange": "#ffab61",
                    "Pink": "#ffc4f1", "Yellow": "#fff870", "Red": "#ff4d4d"}
    color = app.getOptionBox(OptionBox)
    app.setBg(colorOptions[color])
    app.setLabelBg("title", "lightblue")

###Widgets
app = gui("Conrado's Tic-Tac-Toe", "700x400", showIcon=False)
app.setBg("#ade4ff")
app.setFont(14)

app.addLabel("title", "Welcome to the awesomest Tic-Tac-Toe game", row=0, column=0, colspan=2)
app.setLabelBg("title", "lightblue")

boardCanvas = app.addCanvas("boardCanvas", row=2, rowspan=9, column=0)
boardCanvas.bind("<Button-1>", humanClicksCanvas)

app.addLabel("difficultyTitle", "Select difficulty:", row=1, column=1)
app.addRadioButton("difficulty", "Easy", row=2, column=1)
app.addRadioButton("difficulty", "Medium", row=3, column=1)
app.addRadioButton("difficulty", "Hard", row=4, column=1)

app.addLabel("symbolTitle", "Select symbol to play as:", row=5, column=1)
app.addRadioButton("symbol", "X", row=6, column=1)
app.addRadioButton("symbol", "O", row=7, column=1)

app.addLabel("firstTitle", "Select who makes the first move:", row=8, column=1)
app.addRadioButton("first", "You", row=9, column=1)
app.addRadioButton("first", "The super advanced AI", row=10, column=1)
app.addRadioButton("first", "Random", row=11, column=1)

app.addLabelOptionBox("Background color", ["Blue",
                    "Green", "Orange", "Pink", "Yellow", "Red"], row=13, column=1)
app.setOptionBoxChangeFunction("Background color", changeBackground)

app.addLabel("announcement","", row = 11, rowspan=2, column = 0)
app.addButtons(["Start/reset game", "Quit"], press, row = 13, column = 0)


def resetCanvasAndBoard():
    global gameBoard, app
    gameBoard.resetBoard()
    app.clearCanvas('boardCanvas')
    boardCanvas.create_line(X[1],Y[0],X[1],Y[3], width=3)
    boardCanvas.create_line(X[2],Y[0],X[2],Y[3], width=3)
    boardCanvas.create_line(X[0],Y[1],X[3],Y[1], width=3)
    boardCanvas.create_line(X[0],Y[2],X[3],Y[2], width=3)


def drawX(tile, xSize):
    global boardCanvas, TILESMIDCOORD
    boardCanvas.create_line(TILESMIDCOORD[tile][0]-xSize//2,TILESMIDCOORD[tile][1]-xSize//2,
                            TILESMIDCOORD[tile][0]+xSize//2,TILESMIDCOORD[tile][1]+xSize//2,
                            width=3, fill='blue')
    boardCanvas.create_line(TILESMIDCOORD[tile][0]-xSize//2,TILESMIDCOORD[tile][1]+xSize//2,
                            TILESMIDCOORD[tile][0]+xSize//2,TILESMIDCOORD[tile][1]-xSize//2,
                            width=3, fill='blue')


def drawO(tile, oSize):
    global boardCanvas, TILESMIDCOORD
    boardCanvas.create_oval(TILESMIDCOORD[tile][0]-oSize//2,TILESMIDCOORD[tile][1]-oSize//2,
                            TILESMIDCOORD[tile][0]+oSize//2,TILESMIDCOORD[tile][1]+oSize//2, width=3, outline='blue')

def drawMove(move, symbol):
    if symbol == 'x':
        drawX(move,XSIZE)
    else:
        drawO(move,OSIZE)


def drawRedline(begin, end):
    boardCanvas.create_line(TILESMIDCOORD[begin][0], TILESMIDCOORD[begin][1],
                            TILESMIDCOORD[end][0], TILESMIDCOORD[end][1],
                            width=7, fill='red')


#########################################################################
def playGame():
    global gameIsRunning, computerIsMakingMove, humanSymbol, computerSymbol, difficulty
    gameIsRunning = True
    resetCanvasAndBoard()

    humanSymbol = app.getRadioButton('symbol').lower()
    computerSymbol = 'o' if humanSymbol == 'x' else 'x'
    difficulty = app.getRadioButton('difficulty').lower()
    computerStarts = doesComputerStart()

    app.setLabel('announcement','Game started! Playing as ' + humanSymbol.upper())
    #Computer's first move is random
    if computerStarts:
        currentDifficulty = difficulty
        difficulty = 'easy'
        AIMove()
        difficulty = currentDifficulty


if __name__ == '__main__':
    resetCanvasAndBoard()
    app.go()
