from tkinter import *
import random


def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(state='disabled')


def winner(w):
    global game
    if (game[0] == w and game[1] == w and game[2] == w) or \
            (game[3] == w and game[4] == w and game[5] == w) or \
            (game[6] == w and game[7] == w and game[8] == w) or \
            (game[0] == w and game[3] == w and game[6] == w) or \
            (game[1] == w and game[4] == w and game[7] == w) or \
            (game[2] == w and game[5] == w and game[8] == w) or \
            (game[0] == w and game[4] == w and game[8] == w) or \
            (game[6] == w and game[4] == w and game[2] == w):
        return True


def push(t):
    global game
    global game_left
    global turn

    if turn % 2 == 0:
        game[t] = 'X'  # b ход пользователя
        buttons[t].config(text='X', state='disabled')  # ложим Х в ячейку и делаем неактивной
    else:
        game[t] = '0'
        buttons[t].config(text='0', state='disabled')
    turn += 1
    if winner("X"):
        lbl['text'] = "X победили!"
        stop_game()
    elif winner('0'):
        lbl['text'] = "0 победили!"
        stop_game()
    else:
        if (len(game_left) > 1):
            game_left.remove(t)
        else:
            lbl['text'] = "Игра окончена"
            stop_game()

    print(game)
    print(game_left)


game = [None] * 9  # список 9 ходов
game_left = list(range(9))  # список ячеек,которые пустые-можно туда ходить
turn = 0  # счетчик ходов

# создаем игравое окно
window = Tk()
window.title("Игра крестики нолики")
lbl = Label(width=20, text="Игра крестики нолики", font=("Arial", 18, 'bold'))
buttons = [Button(width=5, height=2, font=("Arial", 18, 'bold'), command=lambda s=i: push(s)) for i in range(9)]

# размещаем ячейки на экране
lbl.grid(row=0, column=0, columnspan=3)
x = 1;
y = 0
for i in range(9):
    buttons[i].grid(row=x, column=y)
    y += 1
    if y == 3:
        x += 1
        y = 0

window.mainloop()
