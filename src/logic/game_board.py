from timeit import default_timer as stopwatch

class GameBoard():
    '''
    5 rung game board
    '''
    def __init__(self) -> None:
        self.board = [['Apple', 5], ['Tree', 0], ['House', 0], ['Pet', 0], ['Sitter', 6]]
        self.wrong_guesses = 0
        self.num_solved = 2
        self.score = 0

        self.cur_index = None
        self.top_bottom_index = [1, -2]

        self.time = 0
        self.cur_guess = False

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
        self.cur_guess = self.board[self.cur_index][0] == guess
        return self.cur_guess
    
    def increment_word(self):
        self.board[self.cur_index][1] += 1

    def increment_wrong(self):
        self.wrong_guesses += 1
    
    def increment_score(self):
        self.score += (len(self.board[self.cur_index][0])-self.board[self.cur_index][1])/len(self.board[self.cur_index][0])

    def update_board(self):
        if self.cur_guess or self.board[self.cur_index][1] == len(self.board[self.cur_index][0]):
            self._update_top_bottom()
            self.board[self.cur_index][1] = len(self.board[self.cur_index][0])
            self.cur_index = None
            self.num_solved += 1
            self.cur_guess = False
    
    def show_board(self):
        for word, state in self.board:
            print(word[:state])

    def check_board(self):
        return self.num_solved != len(self.board)
    
    def show_analytics(self):
        print(f'Wrong guesses: {self.wrong_guesses}')
        print(f'Score: {round(self.score/(len(self.board)-2), 4)*100}')
        print(f'Time elapsed: {self.time} seconds')
    





