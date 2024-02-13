from timeit import default_timer as stopwatch
import sys
import pyprojroot
root = pyprojroot.here()
sys.path.append(str(root))
from src.parsing.parser import get_board

class GameBoard():
    '''
    Rungs gameboard
    '''
    def __init__(self) -> None:
        self.board = get_board() # random board from text file
        self.wrong_guesses = 0
        self._num_solved = 2 # first and last word are already solved
        self.score = 0

        self.cur_index = None
        self.top_bottom_index = [1, -2]

        self.time = 0
        self._cur_guess = False

    def _update_top_bottom(self):
        if self.cur_index > 0:
            self.top_bottom_index[0] += 1
        else:
            self.top_bottom_index[1] -= 1

    def timer(self, flag):
        if flag == 'start':
            self.time = stopwatch()
        if flag == 'end':
            self.time = round(stopwatch() - self.time, 2)
    
    def check_last(self):
        return len(self.board) + self.top_bottom_index[1] != self.top_bottom_index[0]
    
    def get_index(self):
        return self.cur_index
    
    def update_index(self, index):
        invalid = True
        if index.lower() in {'top', 't', 'up', 'u'}:
            self.cur_index = self.top_bottom_index[0]
            invalid = False
        elif index.lower() in {'bottom', 'b', 'bot', 'down', 'd'}:
            self.cur_index = self.top_bottom_index[1]
            invalid = False
        return invalid

    def guess_word(self, guess):
        self._cur_guess = self.board[self.cur_index][0] == guess
        return self._cur_guess
    
    def increment_word(self):
        self.board[self.cur_index][1] += 1

    def increment_wrong(self):
        self.wrong_guesses += 1
    
    def increment_score(self):
        self.score += (len(self.board[self.cur_index][0])-self.board[self.cur_index][1])/len(self.board[self.cur_index][0])

    def update_board(self):
        if self.board[self.cur_index][1] == len(self.board[self.cur_index][0]):
            print("Nice Try\n")
        if self._cur_guess or self.board[self.cur_index][1] == len(self.board[self.cur_index][0]):
            self._update_top_bottom()
            self.board[self.cur_index][1] = len(self.board[self.cur_index][0])
            self.cur_index = None
            self._num_solved += 1
            self._cur_guess = False
    
    def show_board(self):
        for i, (word, state) in enumerate(self.board):
            print(f'{i+1}. {word[:state].upper()}')

    def check_board(self):
        return self._num_solved != len(self.board)
    
    def show_analytics(self):
        self._calc_score()
        print(f'Wrong guesses: {self.wrong_guesses}')
        print(f'Score: {self.score}')
        print(f'Time elapsed: {self.time} seconds')

    def _calc_score(self):
        self.score = round(100*self.score/(len(self.board)-2), 2)