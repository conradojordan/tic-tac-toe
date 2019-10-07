import pytest
import boardGUI, tictactoe


def test_board_available_tiles():
    assert boardGUI.Board('x','','o','o','x','','','x','').availableTiles() == ['topM','midR','botL','botR']
    assert boardGUI.Board('','o','','o','x','x','','x','o').availableTiles() == ['topL','topR','botL']
    assert boardGUI.Board('x','x','','x','x','x','','x','x').availableTiles() == ['topR','botL']
    assert boardGUI.Board('o','o','o','','','x','o','','o').availableTiles() == ['midL','midM','botM']
    assert boardGUI.Board().availableTiles() == ['topL','topM','topR','midL','midM','midR','botL','botM','botR']
    assert boardGUI.Board('x','x','x','o','o','o','x','x','x').availableTiles() == []


def test_board_has_winner():
    assert boardGUI.Board('x','x','x','','','','','','').hasWinner() == ('x', ['topL', 'topR'])
    assert boardGUI.Board('o','o','o','','','','','','').hasWinner() == ('o', ['topL', 'topR'])
    assert boardGUI.Board('x','','','x','','','x','','').hasWinner() == ('x', ['topL', 'botL'])
    assert boardGUI.Board('','','x','','','x','','','x').hasWinner() == ('x', ['topR', 'botR'])
    assert boardGUI.Board('x','','','','x','','','','x').hasWinner() == ('x', ['topL', 'botR'])
    assert boardGUI.Board('','','o','','o','','o','','').hasWinner() == ('o', ['topR', 'botL'])
    assert boardGUI.Board('x','x','o','o','o','x','x','o','x').hasWinner() == False
    assert boardGUI.Board().hasWinner() == False


def test_tictactoe_AI_medium():
    assert tictactoe.AIMedium(boardGUI.Board('x','','o','','','','','','x'), 'o', 'x') == 'midM'
    assert tictactoe.AIMedium(boardGUI.Board('x','o','x','','o','','x','',''), 'o', 'x') == 'botM'
    assert tictactoe.AIMedium(boardGUI.Board('','','','','o','','x','x','o'), 'o', 'x') == 'topL'
    assert tictactoe.AIMedium(boardGUI.Board('x','o','x','','o','','x','',''), 'x', 'o') == 'midL'

def test_tictactoe_AI_hard():
    assert tictactoe.AIHard(boardGUI.Board('x','','o','','','','','','x'), 'o', 'x') == 'midM'
    assert tictactoe.AIHard(boardGUI.Board('x','o','x','','o','','x','',''), 'o', 'x') == 'botM'
    assert tictactoe.AIHard(boardGUI.Board('','','','','o','','x','x','o'), 'o', 'x') == 'topL'
    assert tictactoe.AIHard(boardGUI.Board('x','o','x','','o','','x','',''), 'x', 'o') == 'midL'
    assert tictactoe.AIHard(boardGUI.Board('x','','','','','','','',''), 'o', 'x') == 'midM'
    assert tictactoe.AIHard(boardGUI.Board('','','x','','','','','',''), 'o', 'x') == 'midM'
    assert tictactoe.AIHard(boardGUI.Board('','','','','','','x','',''), 'o', 'x') == 'midM'

def test_tictactoe_evaluate_board():
    assert tictactoe.evaluateBoard(boardGUI.Board('x','','','x','','','x','',''), 'x', 'x') == 1
    assert tictactoe.evaluateBoard(boardGUI.Board('x','','','x','','','x','',''), 'o', 'x') == -1
    assert tictactoe.evaluateBoard(boardGUI.Board('x','x','o','o','o','x','x','o','x'), 'x', 'x') == 0
    assert tictactoe.evaluateBoard(boardGUI.Board('o','x','o','x','o','','x','','o'), 'o', 'o') == 1
    assert tictactoe.evaluateBoard(boardGUI.Board('o','x','o','x','o','','x','','o'), 'o', 'x') == 1
