# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень ')) + 1

def get_odds(num):
    x = None
    lst1 = list(random.randint(0, 100) for i in range(num))
    stringa = ''
    # while i < len(lst1):
    for i in range(len(lst1) - 1, -1, -1):
        if i == 1:
            stringa += f'{lst1[i]}*x + '
        elif i == 0:
            stringa += str(lst1[0])
        else:
            stringa += f'{lst1[i]}*x**{i} + '
    return stringa

result = get_odds(k)
print(result)

with open("result.txt", 'w') as test_file:
    test_file.write(result)


