import random
from board import GameBoard


def play():
    print('Enjoy the game!')
    gameboard = GameBoard()
    gameboard.print_board()
    game_on = True
    while game_on:
        if not gameboard.is_winner('X'):
            if not gameboard.is_winner('0'):
                if not gameboard.is_board_full():
                    if gameboard.turn == 'Player':
                        choice = int(input('Where do you want to put X ? Insert a choice between 1 - 9: '))
                        if 0 < choice and choice < 10 and gameboard.check_empty_pos(choice):
                            gameboard.make_move(pos=choice, symbol='X')
                            print('\n' * 20)
                            gameboard.print_board()
                    else:
                        empty_spaces = [x for x in range(len(gameboard.board)) if x == ' ' or x != 0]
                        cpu_choice = random.choice(empty_spaces)
                        if gameboard.check_empty_pos(cpu_choice):
                            gameboard.make_move(cpu_choice, '0')
                            print('\n' * 20)
                            gameboard.print_board()
                            print(f'Computer choice: {cpu_choice}')
                else:
                    game_on = False
                    print('Game finished in a tie.')
            else:
                print('Game Finished. Cpu won!')
                game_on = False
        else:
            print('Game Finished. Player won!')
            game_on = False


play()