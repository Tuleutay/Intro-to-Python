# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
import random

sweets = 100

# for gamers
# a = random.randint(1, 2)
# print(f'Ходит игрок № {a}')
# if a == 1:
#     user = 1
# else:
#     user = 2
#
# count = user
# while sweets > 0:
#     x = int(input(f"Oсталось {sweets} конфет. Сколько конфет хотите взять? "))
#     sweets -= x
#     count += 1
# if count % 2 == 0:
#     user = 1
# else:
#     user = 2
# print(f'Выиграл игрок {user}')


# with bot

a = random.randint(1, 2)

if a == 1:
    a = 'player'
    user = 1
else:
    a = 'Ben'
    user = 2
print(f'Ходит {a}')

while sweets > 0:
    if user % 2 != 0:
        x = int(input(f"Oсталось {sweets} конфет. Сколько конфет хотите взять? "))
    else:
        if sweets % 29 != 0:
            x = sweets % 29
        else:
            x = random.randint(1, 28)
        print(f'Ben берёт {x} конфет')
    sweets -= x
    user += 1
if user % 2 != 0:
    user = 'Ben'
else:
    user = 'player'
print(f'Выиграл {user}')
