# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k=int(input('Введите натуральную степень '))+1
# lst1 = list(random.randint(0, 100) for i in range(0,k))
# print(lst1)
# for i in range(k):
#     print(f'{lst1[i]}x**{i}', end=" ")
def get_odds(num):
    x=None
    lst1 = list(random.randint(0, 100) for i in range(num))
    print(lst1)
    lst2 = []
    i=1
    while i < len(lst1):
        # lst2.append(lst1[i]*x**i)
        print(f'{lst1[i]}*x**{i}')
        i+=1
    # lst2[0]=lst1[0]
    return i
result = get_odds(k)
print(result)
