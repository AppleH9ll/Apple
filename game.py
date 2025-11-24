import random

class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = None
        self.game_mode = None
        self.move_history = []

    def reset(self):
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.move_history = []

    def random_first_player(self):
        self.current_player = random.choice(['X', 'O'])

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.move_history.append((row, col, self.current_player))
            return True
        return False

    def check_winner(self):
        for i in range(self.size):
            if all(self.board[i][j] == self.current_player for j in range(self.size)) or \
               all(self.board[j][i] == self.current_player for j in range(self.size)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(self.size)) or \
           all(self.board[i][self.size-1-i] == self.current_player for i in range(self.size)):
            return True
        return False

    def is_draw(self):
        return all(self.board[i][j] != ' ' for i in range(self.size) for j in range(self.size))

    def get_empty_cells(self):
        return [(i, j) for i in range(self.size) for j in range(self.size) if self.board[i][j] == ' ']

    def bot_move(self):
        empty_cells = self.get_empty_cells()
        return random.choice(empty_cells) if empty_cells else (None, None)