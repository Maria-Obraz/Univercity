import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.winner = None

    def display_board(self):
        print(f' {self.board[0]} | {self.board[1]} | {self.board[2]} ')
        print('-----------')
        print(f' {self.board[3]} | {self.board[4]} | {self.board[5]} ')
        print('-----------')
        print(f' {self.board[6]} | {self.board[7]} | {self.board[8]} ')

    def is_winner(self):
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                self.winner = self.board[i]
                return True
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                self.winner = self.board[i]
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            self.winner = self.board[0]
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            self.winner = self.board[2]
            return True
        return False

    def is_tie(self):
        return ' ' not in self.board

    def make_move(self, index):
        if self.board[index] == ' ':
            self.board[index] = self.current_player
            return True
        else:
            return False

    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    def play_with_human(self):
        while not self.is_winner() and not self.is_tie():
            self.display_board()
            print(f"Player {self.current_player}'s turn")
            index = int(input('Enter a number from 1-9 to place your mark: ')) - 1
            if self.make_move(index):
                self.switch_player()
            else:
                print('That spot is already taken. Try again.')
        self.display_board()
        if self.winner:
            print(f'Player {self.winner} wins!')
        else:
            print('Tie game!')

    def play_with_computer(self):
        while not self.is_winner() and not self.is_tie():
            self.display_board()
            if self.current_player == 'X':
                index = int(input('Enter a number from 1-9 to place your mark: ')) - 1
                if self.make_move(index):
                    self.switch_player()
                else:
                    print('That spot is already taken. Try again.')
            else:
                available_spots = [i for i in range(9) if self.board[i] == ' ']
                index = random.choice(available_spots)
                self.make_move(index)
                self.switch_player()
        self.display_board()
        if self.winner:
            print(f'Player {self.winner} wins!')
        else:
            print('Tie game!')

game = TicTacToe()
game.play_with_computer()