# Задача 2. Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))


def board_layout(board):
    print('-' * 13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-' * 13)


def take_input(player_turn):
    valid = False
    while not valid:
        player_answer = input('Куда ставить ' + player_turn + ' ?  ')
        try:
            player_answer = int(player_answer)
        except:
            print('Некорректный ввод. Введите число')
            continue
        if player_answer >= 1 and player_answer <= 9:
            if str(board[player_answer-1]) not in 'XO':
                board[player_answer-1] = player_turn
                valid = True
            else:
                print('Эта клетка занята, сделайте другой выбор.')
        else:
            print('Неверный ввод: введите число от 1 до 9.')


def check_winning_options(board):
    winning_options = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in winning_options:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def base_game(board):
    counter = 0
    win = False
    while not win:
        board_layout(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            tmp = check_winning_options(board)
            if tmp:
                print(tmp, 'выиграл!')
                win = True
                break
        if counter == 9:
            print('Ничья!')
            break
    board_layout(board)


base_game(board)

input('Нажмите Enter для выхода/')