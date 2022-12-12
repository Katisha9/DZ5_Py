# Задача 1. Создайте программу для игры с конфетами человек против компьютера.
# Условие задачи: На столе лежит 150 конфет. Играют игрок против компьютера.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Подумайте, как наделить бота "интеллектом".

from random import randint


def input_number_lollipops(name):
    loll = int(input(f"{name}, сколько конфет возьмете? Введите число от 1 до 28: "))
    while loll < 1 or lollipops > 28:
        loll = int(input(f"{name}, Вы хотите взять больше, чем следует. Введите число от 1 до 28: "))
    return loll


def subtotal_print(name, loll, counter, remainder):
    print(f"{name} взял {loll}, сумма его конфет равна {counter}, а на столе осталось {remainder}.")


def bot_move(loll_on_table):
    loll: int = randint(1, 29)
    while loll_on_table-loll <= 28 and loll_on_table > 29:
        loll = randint(1, 29)
    return loll


player1 = input("Введите имя игрока: ")
player2 = "Bot"


lollipopsOnTable = 150
sequence = randint(0, 2)  # жеребьевка очередности
if sequence == 1:
    print(f"Первый ход у {player1}")
else:
    print(f"Первый ход у {player2}")

counterLollipops1 = 0
counterLollipops2 = 0

while lollipopsOnTable > 28:
    if sequence == 1:
        lollipops = input_number_lollipops(player1)
        counterLollipops1 += lollipops
        lollipopsOnTable -= lollipops
        sequence = False
        subtotal_print(player1, lollipops, counterLollipops1, lollipopsOnTable)
    else:
        lollipops = bot_move(lollipopsOnTable)
        counterLollipops2 += lollipops
        lollipopsOnTable -= lollipops
        sequence = True
        subtotal_print(player2, lollipops, counterLollipops2, lollipopsOnTable)

if sequence:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
