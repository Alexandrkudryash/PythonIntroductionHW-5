# Домашнее задание 5.
# Задача 3.
# Создайте программу для игры в ""Крестики-нолики"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from random import randint as ri

def draw_board(board):
    print("-"*13)
    for i in range(3):
      print ("|", board [0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-"*13)

def win_combination(list):
    one = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[3,6,9],[2,5,8],[1,5,9],[3,5,7]]
    count = 0
    for i in one:
        for n in i:
           for k in list:
              if n == k:
                  count+=1
           if count >=3:
              return True
        count = 0

def corrective_input():
    if lottery == 1:
        place = int(input(f'{player_1} укажите клетку, где Вы хотите поставить крестик: '))
    else:
        place = int(input(f'{player_2} укажите клетку, где Вы хотите поставить нолик: '))
    while place <=0 or place > 9:
         place = int(input('некорректный ввод, пожалуйста попробуйте снова: '))
    while str(board[place-1]) in 'XO':
        place = int(input('эта клетка уже занята, выберите другую: '))
    while place <= 0 or place > 9:
        place = int (input('некорректный ввод, попробуйте снова: '))
    return place

board = [i for i in range(1, 10)]
player_1= input('введите имя Игрока1: ').capitalize()
player_2= input('введите имя Игрока2: ').capitalize()
lottery= ri(0,1)
if lottery ==1:
    print(f'{player_1} делает первый ход.')
else:
    print(f'{player_2} делает первый ход.')

step=1
list_one=[]
list_two=[]
list_winner=[]
while step <=9:
    draw_board(board)       
    if win_combination(list_winner)==True:
        print(f'Поздравляем {winner}, Вы выиграли')
        break
    else:
        if lottery == 1:
            sign= corrective_input()
            list_one.append(sign)
            list_winner= list_one
            winner=player_1
            lottery=0
            board[sign-1]='X'
        else:
            sign=corrective_input()
            list_two.append(sign)
            list_winner=list_two
            winner=player_2
            lottery=1
            board[sign-1]='O'
    step+=1
# else:
#     print('Никто не выиграл')




    
