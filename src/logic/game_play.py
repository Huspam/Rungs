from game_board import GameBoard

def run_game():
    rungs = GameBoard()
    rungs.show_board()
    rungs.timer('start')

    while rungs.check_board():
        if not rungs.get_index() and rungs.check_last():
            top_bottom = input('Solve top or bottom? ')
            while rungs.update_index(top_bottom):
                top_bottom = input('Invalid; Solve top or bottom? ')
        elif not rungs.check_last():
            rungs.update_index('t')

        guess = input('\nGuess: ').title()
        if rungs.guess_word(guess):
            print("\nNice\n")
            rungs.increment_score()
        else:
            print('\nYeowch\n')
            rungs.increment_wrong()
            rungs.increment_word()

        rungs.update_board()
        rungs.show_board()
    
    rungs.timer('end')
    print('\nThanks for playing\n')
    rungs.show_analytics()
        


if __name__ == '__main__':
    run_game()