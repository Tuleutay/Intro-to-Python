# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#  Пример:
#  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
numbers = [2, 3, 5, 9, 3]
n=len(numbers)
sum=0
for i in numbers[1:n:2]:
    sum+=i
print(sum)