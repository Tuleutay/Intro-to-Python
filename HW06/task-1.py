# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# БЫЛО
# lst1 = [2, 3, 4, 5, 6]
# n = math.ceil(len(lst1) / 2)
# lst2 = []
# for i in range(0, n):
#     num = lst1[i] * lst1[len(lst1)-1 - i]
#     lst2.append(num)
# print(lst2)
import math

lst1 = [2, 3, 4, 5, 8]

lst2 = list(map(lambda i: lst1[i] * lst1[len(lst1)-1 - i], range(math.ceil(len(lst1)/2))))

print(lst2)
