''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import random
import oxo_data

class Game:
    def __init__(self):
        self.board = self.new_game()

    def new_game(self):
        """Return a new empty game board"""
        return list(" " * 9)

    def save_game(self):
        """Save game to disk"""
        oxo_data.saveGame(self.board)
    
    def restore_game(self):
        """Restore previously saved game"""
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self.board = game
            else:
                self.board = self.new_game()
        except IOError:
            self.board = self.new_game()
    
    def _generate_move(self):
        """Generate a random cell from those available"""
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1
    
    def _is_winning_move(self):
        """Check if the last move was a winning move"""
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        """Process a user move"""
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        self.board[cell] = 'X'
        return 'X' if self._is_winning_move() else ""

    def computer_move(self):
        """Process a computer move"""
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        return 'O' if self._is_winning_move() else ""

def test():
    game = Game()
    result = ""
    while not result:
        print(game.board)
        try:
           result = game.user_move(game._generate_move())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computer_move()
            
        if not result: 
            continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Winner is:", result)
        print(game.board)

if __name__ == "__main__":
    test()