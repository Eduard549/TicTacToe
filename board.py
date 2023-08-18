

class GameBoard:

    def __init__(self):
        self.board = [' ' for x in range(10)]
        self.turn = 'Player'

    def print_board(self):
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('-----------')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('-----------')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])


    def check_empty_pos(self, pos):
        return self.board[pos] == ' '


    def is_board_full(self):
        if ' ' in self.board:
            return False


    def is_winner(self, xo):
        brd = self.board
        return ((brd[1] == xo and brd[2] == xo and brd[3] == xo) or
                (brd[4] == xo and brd[5] == xo and brd[6] == xo) or
                (brd[7] == xo and brd[8] == xo and brd[9] == xo) or
                (brd[1] == xo and brd[4] == xo and brd[7] == xo) or
                (brd[2] == xo and brd[5] == xo and brd[8] == xo) or
                (brd[3] == xo and brd[6] == xo and brd[9] == xo) or
                (brd[1] == xo and brd[5] == xo and brd[9] == xo) or
                (brd[3] == xo and brd[5] == xo and brd[7] == xo))


    def make_move(self, pos, symbol):
        self.board[pos] = symbol
        self.is_winner(symbol)
        if self.turn == 'Player':
            self.turn = 'Cpu'
        else:
            self.turn = 'Player'



