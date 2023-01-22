# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите натуральную степень '))


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

# rewenie 2

# file = open('file.txt', 'w')
# res = ''
#
# for i in range(k, -1, -1):
#     f = ''
#     a = random.randrange(0, 100)
#     if a > 0:
#         f = str(a) + '*x^' + str(i) + ' + '
#     res += f
# if len(res) > 0:
#     res += ' = 0'
# else:
#     print('No argument')
#
# res = res.replace(" 1*", '').replace('^1', "").replace('*x^0', "").replace('+  ', "").replace('+ +', "+")
# file.write(res)
# file.close()
