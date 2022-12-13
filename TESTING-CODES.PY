# Ex1
# from datetime import datetime as dt
# time = dt.now()#.strftime('%D  %H:%M')
# print(dt)
# print(time)

# Ex2
# n=input('нужно ввести любое значение: ')
# print(f'ты ввел такое значение = {n}')
# if not n.isdigit():
#     print('это не цифра')
# else:
#     print('это цифра')

# Ex3 (разбираю часть кода из Задачи-2)
def player_move(max_per_move: int, current_count: int, player: str):
    print(f"Ход игрока: {player}")
    print("~" * 25)
    max_ = current_count if max_per_move > current_count else max_per_move
    print(f"Сейчас: {current_count} конфет")
    move = input(f"Введите количество конфет, которые вы хотите взять (максимум - {max_}): ")
    if not move.isdigit() or max_ < int(move) or 1 > int(move):
        print("\n")
        #print("\033[31mЭто число не подходит!!!!!\033[0m")
        print("\033[Это число не подходит!!!!!\033[")
        print("\n")
        move = player_move(max_per_move, current_count, player)
    return int(move)

player_move(28, 200, 'player1')
print(max_per_move)





