board = {'7':'', '8':'', '9':'', 
         '4':'', '5':'', '6':'',
         '1':'', '2':'', '3':''}
board_keys = []
for key in board:
    board_keys.append(key)
def print_board(board):
    print(board['7'] +  '|' + board['8'] + '|' + board['9'])
    print(" --++-- ")
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print("--+--")
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print("--++--")
def game():
    turn = 'x'
    count = 0

    for i in range(10):
        print_board(board)
        print("It's your turn,", turn, "where will you move to")

        position = input()

        if board[position] == '':
            board[position] = turn
            count += 1
        else:
            print(position, "is already filled there")
            continue
        
        if count>=5:
            if board['7'] == board['8'] == board['9'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break
            
            elif board['4'] == board['5'] == board['6'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

            elif board['1'] == board['2'] == board['3'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

            elif board['7'] == board['4'] == board['1'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

            elif board['8'] == board['5'] == board['2'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

            elif board['9'] == board['6'] == board['3'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

            elif board['7'] == board['5'] == board['3'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

            elif board['9'] == board['5'] == board['1'] != '':
                print_board(board)
                print("Game over", turn, "won")
                break

        if count == 9:
            print("The game is over, it is a tie")
        if turn == 'x':
            turn = '0'
        else:
            turn = 'x'
if __name__ == "__main__":
    game()


        