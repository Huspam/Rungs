from pathlib import Path
import pyprojroot
import random
root = pyprojroot.here()

def _parse():
    board_file = Path(root, 'data', 'gameboards.txt')
    lines = open(board_file).read().splitlines()
    return random.choice(lines)

def get_board():
    board = _parse()
    board = [[word.title(), 0] for word in board.split('-')]
    board[0][1] = len(board[0][0])
    board[-1][1] = len(board[-1][0])
    return board
