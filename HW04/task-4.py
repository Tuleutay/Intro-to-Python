# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень ')) + 1

def get_odds(num):
    randomNumbersList = list(random.randint(0, 100) for i in range(num))
    stringa = ''
    # while i < len(randomNumbersList):
    for i in range(len(randomNumbersList) - 1, -1, -1):
        if i == 1:
            stringa += f'{randomNumbersList[i]}*x + '
        elif i == 0:
            stringa += str(randomNumbersList[0])
        else:
            stringa += f'{randomNumbersList[i]}*x**{i} + '
    return stringa

result = get_odds(k)
print(result)

with open("result.txt", 'w') as test_file:
    test_file.write(result)


